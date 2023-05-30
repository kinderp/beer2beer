from .command import Command
from receiver.receiver_keepalive import ReceiverAlive


class CommandAlive(Command):
    def __init__(self, host, port, payload):
        self.__receiver = ReceiverAlive(host, port, payload)

    def execute(self, args=None):
        response = self.__receiver.alive()
        # add here some login to check response
        # and return something to the caller
        pass