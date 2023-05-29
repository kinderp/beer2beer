import argparse

from server.server import Server
from peer.peer import Peer
from shell.shell import Beer2BeerShell
from settings import ShellSettings

MODE_SERVER = "server"
MODE_PEER = "client"
MODE_SHELL = "shell"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Beer2Beer', 
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=ShellSettings.LOGO,
                                     epilog='Beer2Beer help')
    parser.add_argument('mode', choices=[MODE_SERVER, MODE_PEER, MODE_SHELL])
    args = parser.parse_args()
    if args.mode == MODE_SERVER:
        # run here a server instance
        s = Server()
        s.run() 
    elif args.mode == MODE_SHELL:
        # run peer (it's just a server on peer side)
        p = Peer()
        p.start()
        # run here b2b shell cmd loop
        Beer2BeerShell().cmdloop()
