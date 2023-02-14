import socket

from util.session import Session
from command.command_login import CommandLogin
from command.command_register import CommandRegister


class Peer:
    def __init__(self, host='localhost', port=8888):
        self._host = host # server hostname
        self._port = port # server port number

    def run(self):
        # let's send a register
        register_payload = "antonio\nmypassword\n" \
                           "filename1|3|abcd\n" \
                           "filename2|2|3df5\n" \
                           "filename3|3|jl9g\n"
        register_command = CommandRegister(self._host, self._port, register_payload)
        response = register_command.execute()

        login_payload = "antonio\npassword\n1234\nprovaprova"
        login_command = CommandLogin(self._host, self._port, login_payload)
        response = login_command.execute()

