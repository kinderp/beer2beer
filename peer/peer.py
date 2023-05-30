import socket
from concurrent import futures as cf
from multiprocessing import Process

from util.session import BinSession
from command.command_login import CommandLogin
from command.command_register import CommandRegister

from . import LOGGER


class Peer(Process):
    def __init__(self, host='localhost', port=9999, queue=1, threads=2):
        super().__init__()
        self._host = host # server hostname
        self._port = port # server port number
        self._queue = queue
        self._threads= threads
        
        self._servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._servsock.bind((self._host,self._port))
        self._servsock.listen(self._queue)


    def handle(self, new_session, address):
        LOGGER.info("[<-] Opened - Session - {} ".format(address))
        new_session.recv_file()
        new_session.disconnect()
        LOGGER.info("[<-] Closed - Session - {}".format(address))


    def run(self):
        with cf.ThreadPoolExecutor(self._threads) as e:
            try:
                while True:
                    new_sock, address = self._servsock.accept()
                    new_session = BinSession(sock=new_sock)
                    e.submit(self.handle, new_session, address)
            except KeyboardInterrupt:
                LOGGER.info("[!] Quit - Closing socket - {}").format(address)
            finally:
                self._servsock.close()

