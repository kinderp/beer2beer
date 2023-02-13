import argparse

from server.server import Server
from peer.peer import Peer


LOGO = """
         _.._..,_,_
        (          )
         ]~,"-.-~~[
       .=])' (;  ([     Beer2Beer is a 4b Inf project
       | ]:: '    [     ITET Leonardo da Vinci, Milazzo (ME)
       '=]): .)  ([     A working demo of a p2p system!!!
         |:: '    |
          ~~----~~

"""

MODE_SERVER = "server"
MODE_PEER = "client"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Beer2Beer', 
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=LOGO,
                                     epilog='Beer2Beer help')
    parser.add_argument('mode', choices=[MODE_SERVER, MODE_PEER])
    args = parser.parse_args()
    if args.mode == MODE_SERVER:
        # run here a server instance
        s = Server()
        s.run()
    elif args.mode == MODE_PEER:
        # run here a peer instance
        p = Peer()
        p.run()
