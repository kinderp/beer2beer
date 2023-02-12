import socket

from util.session import Session


class Peer:
    def __init__(self, host='localhost', port=8888):
        self._host = host # server hostname
        self._port = port # server port number

   
    def send_message(self, message):
        s = Session(self._host, self._port)
        s.connect()
        s.send_message(message)
        return s.recv_message()

