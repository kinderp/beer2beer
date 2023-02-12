from .messages_codes import LOGIN
from .messages_codes import LOGIN_OK
from .messages_codes import LOGIN_KO
from .message_login import MessageLogin


class MessagesFactory:
    MESSAGES = {
        LOGIN : MessageLogin,
        LOGIN_OK: MessageLogin,
        LOGIN_KO: MessageLogin,
    }

    @classmethod
    def create(cls, message_type, data):
        return cls.MESSAGES[message_type](message_type, data)

