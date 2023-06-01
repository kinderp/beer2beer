from .command import Command
from receiver.receiver_logout import ReceiverLogout

class CommandLogout(Command):
    def __init__(self, host, port, payload):
        self._receiver = ReceiverLogout(host, port, payload)

    def execute(self, args = None):
        response = self._receiver.logout()
        pass
