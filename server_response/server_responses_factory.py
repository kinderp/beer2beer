from message.messages_codes import LOGIN
from message.messages_codes import REGISTER
from .login_response import LoginResponse
from .register_response import RegisterResponse


class ServerResponsesFactory:
    MESSAGES = {
        LOGIN : LoginResponse,
        REGISTER : RegisterResponse,
    }

    @classmethod
    def create(cls, message):
        return cls.MESSAGES[message._mtype](message)


