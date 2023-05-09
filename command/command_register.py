from .command import Command
from receiver.receiver_register import ReceiverRegister
from message.messages_codes import REGISTER_OK, REGISTER_KO
from settings import ShellSettings


class CommandRegister(Command):
    def __init__(self, host, port, payload):
        self.__receiver = ReceiverRegister(host, port, payload)

    def execute(self, args=None):
        response = self.__receiver.register()
        response.unpack() # we need to convert raw payload into high-level one
        if response._mtype == REGISTER_OK:
            if response.id:
                ShellSettings.USER_ID = response.id
                return True
            return False
        if response._mtype == REGISTER_KO:
            return False

