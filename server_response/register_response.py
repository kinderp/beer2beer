from .server_response import ServerResponse
from message.messages_codes import REGISTER, REGISTER_OK, REGISTER_KO
from message.messages_factory import MessagesFactory


class RegisterResponse(ServerResponse):
    def __init__(self, message):
        super().__init__(message)

    def reply(args=None):
        import random
        register_or_not_register = random.randint(0,99)
        if register_or_not_register <= 49:
            # ok register
            output_message = MessagesFactory.create(REGISTER_OK, "REGISTER_OK")
        else:
            output_message = MessagesFactory.create(REGISTER_KO, "REGISTER_KO")
        return output_message
        
