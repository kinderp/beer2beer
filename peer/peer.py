import socket

from util.session import Session
from command.command_login import CommandLogin

class Peer:
    def __init__(self, host='localhost', port=8888):
        self._host = host # server hostname
        self._port = port # server port number

    def run(self):
        login_payload = "antonio\npassword\n1234\nprovaprova"
        login_command = CommandLogin(self._host, self._port, login_payload)
        response = login_command.execute()

