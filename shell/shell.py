import cmd
import os
import pickle
import socket

from settings import ShellSettings
from command.command_login import CommandLogin
from command.command_logout import CommandLogout
from command.command_register import CommandRegister
from command.command_search import CommandSearch
from command.command_register_update import CommandRegisterUpdate
from util.util import Util
from command.command_keepalive import  CommandAlive


FILE_SETTINGS = ShellSettings.DIRECTORY_SETTINGS + "/" + "settings.bin"


class Beer2BeerShell(cmd.Cmd):
    intro = ShellSettings.LOGO
    prompt = ">"
    file = None

    def parse(self, arg):
        return arg.split()

    def do_save(self, arg):
        if not os.path.exists(ShellSettings.DIRECTORY_SETTINGS):
            os.makedirs(ShellSettings.DIRECTORY_SETTINGS)
        with open(FILE_SETTINGS, "wb") as f:
            pickle.dump(ShellSettings.dict_from_class(), f)

    def help_save(self):
        help_string = """
        DESCRIPTION:
            Save all settings.

        USAGE:
            >save
        """
        print(help_string)

    def do_load(self, arg):
        with open(FILE_SETTINGS, "rb") as f:
            records = pickle.load(f)
            ShellSettings.load(records)

    def help_load(self):
        help_string = """
        DESCRIPTION:
            Load all settings.

        USAGE:
            >load
        """
        print(help_string)

    def do_show(self, arg):
        print("USERNAME  => ", ShellSettings.USERNAME)
        print("PASSWORD  => ", ShellSettings.PASSWORD)
        print("USER_ID => ", ShellSettings.USER_ID)
        print("DIRECTORY => ", ShellSettings.DIRECTORY)
        print("DIRECTORY SETTINGS => ", ShellSettings.DIRECTORY_SETTINGS)
        print("SERVER HOSTNAME => ", ShellSettings.SERVER_HOST)
        print("SERVER PORT => ", ShellSettings.SERVER_PORT)

    def help_show(self):
        help_string = """
        DESCRIPTION:
            Show all settings.

        USAGE:
            >show
        """
        print(help_string)

    def do_quit(self, arg):
        return True

    def help_quit(self):
        help_string  = """
        DESCRIPTION:
            Quit Beer2Beer shell.

        USAGE:
            >quit
        """
        print(help_string)

    def do_set(self, arg):
        self.parse_set(arg)

    def parse_set(self, arg):
        parsed = self.parse(arg)
        if len(parsed) <= 1: return
        sub_cmd, value = parsed
        if sub_cmd in ('user', 'pwd', 'path', 'host', 'port'):
            if sub_cmd == 'user':
                ShellSettings.USERNAME = value
            elif sub_cmd == 'pwd':
                ShellSettings.PASSWORD = value
            elif sub_cmd == 'path':
                ShellSettings.DIRECTORY = value
            elif sub_cmd == 'host':
                ShellSettings.SERVER_HOST = value
            elif sub_cmd == 'port':
                ShellSettings.SERVER_PORT = value
            return True
        print("ERROR: {} is not recognized, please run >help set".format(sub_cmd))
        return False

    def help_set(self):
        help_string = """
        DESCRIPTION:
            Set different user's options and client's parameters.
            Here a list of available options
            * host - set server hostname to conect  to
            * port - set server port to connect to
            * user - set username to  use  in the network
            * pwd  - set password for your username
            * path - set dir where you are storing all data you
                     want to share.
                     *WARNING*: it must be an absolute path

            See USAGE section for more details

        USAGE:
            >set host <hostanme>
            >set port <port>
            >set user <username>
            >set pwd  <password>
            >set path <directory>
        """
        print(help_string)

    def get_peer_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip, port = s.getsockname()
        s.close()
        return ip

    def do_login(self, arg):
        if not ShellSettings.USER_ID:
            print("ERROR: id not set, did you make a registration?!")
            return False
        arg = self.parse(arg)
        result, user, pwd = self.parse_login(arg)
        if not result: return False
        ip = self.get_peer_ip()
        login_payload = "{}\n{}\n{}\n{}\n".format(user, pwd, ShellSettings.USER_ID, ip)
        login_command = CommandLogin(
                ShellSettings.SERVER_HOST, ShellSettings.SERVER_PORT, login_payload)
        response = login_command.execute()

    def parse_login(self, arg):
        if len(arg) == 2:
            user = arg[0]
            pwd = arg[1]
            return (True, user, pwd)
        elif len(arg) == 0:
            user = ShellSettings.USERNAME
            pwd = ShellSettings.PASSWORD
            if user is None or pwd is None:
                print("ERROR: username or password not set, please run >help set")
                return (False, user, pwd)
            return (True, user, pwd)
        else:
            print("ERROR: username or password not set, please run >help set")
            return (False, None, None)
 
    def help_login(self):
        help_string = """
        DESCRIPTION:
            Enter to the network.

        USAGE:
            >login
            >login <username> <password>

        NOTE:
            You can omit both  <usarname> and  <password>
            if you have already set them with set command
        """
        print(help_string)

    def do_register(self, arg):
        arg = self.parse(arg)
        result, user, pwd, share_dir = self.parse_register(arg)
        if not result: return False
        data = Util.browse_dir(share_dir)
        register_payload = "{}\n{}\n".format(user, pwd)
        for elem in data:
            register_payload = register_payload + "{}|{}|{}\n".format(elem.filename, elem.dimension, elem.sha1)
        register_command = CommandRegister(
                ShellSettings.SERVER_HOST, ShellSettings.SERVER_PORT, register_payload)
        response = register_command.execute()

    def do_register_update(self, arg):
        arg = self.parse(arg)
        result, user, pwd, share_dir = self.parse_register(arg)
        if not result: return False
        data = Util.browse_dir(share_dir)
        register_update_payload = "{}\n{}\n{}\n".format(user, pwd, ShellSettings.USER_ID)
        for elem in data:
            register_update_payload = register_update_payload + "{}|{}|{}\n".format(elem.filename, elem.dimension, elem.sha1)
        register_update_command = CommandRegisterUpdate(
                ShellSettings.SERVER_HOST, ShellSettings.SERVER_PORT, register_update_payload)
        response = register_update_command.execute()

    def parse_register(self, arg):
        if len(arg) == 3:
            user = arg[0]
            pwd = arg[1]
            share_dir = arg[2]
            return (True, user, pwd, share_dir)
        elif len(arg) == 0:
            user = ShellSettings.USERNAME
            pwd = ShellSettings.PASSWORD
            share_dir = ShellSettings.DIRECTORY
            if user is None or pwd is None or share_dir is None:
                print("ERROR: username, password or sharing dir not set, please run >help set")
                return (False, user, pwd, share_dir)
            return (True, user, pwd, share_dir)
        else:
            print("ERROR: username, password or sharing dir not set, please run >help set")
            return (False, None, None, None)
 

    def help_register(self):
        help_string = """
        DESCRIPTION:
            Register all shared contents to the network.

        USAGE:
            >register
            >register <username> <password> <directory>
        
        NOTE:
            You can omit arguments <username> <password>
            and <directory> if you have already set them
            with set command
        """
        print(help_string)

    def help_register_update(self):
        help_string = """
        DESCRIPTION:
            Register update all shared contents to the network.

        USAGE:
            >register update
            >register update <username> <password> <directory>
        
        NOTE:
            You can omit arguments <username> <password>
            and <directory> if you have already set them
            with set command
        """
        print(help_string)

    def help_logout(self):
        help_string = """
        DESCRIPTION:
            Logout to the network.
            
        USAGE:
            >logout
            >logout <username> <password>
        
        NOTE:
            You can omit both  <usarname> and  <password>
            if you have already set them with set command
        """
        print(help_string)

    def help_keepalive(self):
        help_string="""
        DESCRIPTION:
           Transmitting a periodic signal to the indexing server can help sustain alive connection and ensure an ongoin presence on the network.
        USAGE:
            >keep_alive
        """
        print(help_string)

    def do_keepalive(self, arg):
        if not ShellSettings.USER_ID: return False
        keep_alive_payload = "{}\n".format(ShellSettings.USER_ID)
        keep_alive_command = CommandAlive(
        ShellSettings.SERVER_HOST, ShellSettings.SERVER_PORT, keep_alive_payload)
        response = keep_alive_command.execute()
   
    def do_search(self, arg): 
        search_payload = "{}\n".format(arg)
        # TODO: CommandSearch
        search_command = CommandSearch(
        ShellSettings.SERVER_HOST, ShellSettings.SERVER_PORT, search_payload)
        response = search_command.execute()

    def help_search(self):
        help_string="""
        DESCRIPTION:
           Search something on the network.
        USAGE:
            >search Learning Python.pdf
        """
        print(help_string)

    def do_logout(self, arg):
        arg = self.parse(arg)
        result, user, pwd = self.parse_logout(arg)
        if not result: return False
        logout_payload = "{}\n{}\n".format(user, pwd)
        logout_command = CommandLogout(
            ShellSettings.SERVER_HOST, ShellSettings.SERVER_PORT, logout_payload)
        response = logout_command.execute()

    def parse_logout(self, arg):
        user = None
        pwd = None
        if len(arg) == 2:
            user = arg[0]
            pwd = arg[1]
            return (True, user, pwd)
        elif user is None or pwd is None:
            user = ShellSettings.USERNAME
            pwd = ShellSettings.PASSWORD
            if user is None or pwd is None:
                print("ERROR: username or password not set")
                return (False, None, None)
            return (True, user, pwd)
