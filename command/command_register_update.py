from .command import Command
from receiver.receiver_register_update import ReceiverRegisterUpdate


class CommandRegisterUpdate(Command):
    def __init__(self, host, port, payload):
        self.__receiver = ReceiverRegisterUpdate(host, port, payload)

    def execute(self, args=None):
        response = self.__receiver.register_update()
        # add here some login to check response
        # and return something to the caller
        pass


