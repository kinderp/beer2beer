from .command import Command
from receiver.receiver_login import ReceiverLogin


class CommandLogin(Command):
    def __init__(self, host, port, payload):
        self.__receiver = ReceiverLogin(host, port, payload)

    def execute(self, args=None):
        response = self.__receiver.login()
        # add here some login to check response
        # and return something to the caller
        return response
        

