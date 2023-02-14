from message.messages_codes import LOGIN
from message.messages_codes import REGISTER
from .login_strategy import LoginStrategy
from .register_strategy import RegisterStrategy


class StrategiesFactory:
    MESSAGES = {
        LOGIN : LoginStrategy,
        REGISTER : RegisterStrategy,
    }

    @classmethod
    def create(cls, message):
        return cls.MESSAGES[message._mtype](message)


