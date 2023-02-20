from .command import Command
from receiver.receiver_register import ReceiverRegister


class CommandRegister(Command):
    def __init__(self, host, port, payload):
        self.__receiver = ReceiverRegister(host, port, payload)

    def execute(self, args=None):
        response = self.__receiver.register()
        # add here some login to check response
        # and return something to the caller
        pass
        

