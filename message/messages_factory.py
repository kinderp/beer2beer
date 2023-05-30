from .messages_codes import LOGIN
from .messages_codes import LOGIN_OK
from .messages_codes import LOGIN_KO
from .messages_codes import REGISTER
from .messages_codes import REGISTER_UPDATE
from .messages_codes import REGISTER_OK
from .messages_codes import REGISTER_KO
from .messages_codes import REGISTER_UPDATE_OK
from .messages_codes import REGISTER_UPDATE_KO
from .messages_codes import KEEP_ALIVE_OK
from .messages_codes import KEEP_ALIVE_KO
from .message_login import MessageLogin
from .message_register_update import MessageRegisterUpdate
from .message_register import MessageRegister, MessageRegisterOk
from .message_alive import MessageAlive


class MessagesFactory:
    MESSAGES = {
        LOGIN : MessageLogin,
        LOGIN_OK: MessageLogin,
        LOGIN_KO: MessageLogin,
        REGISTER: MessageRegister,
        REGISTER_UPDATE: MessageRegisterUpdate,
        REGISTER_OK: MessageRegisterOk,
        REGISTER_KO: MessageRegister,
        REGISTER_UPDATE_OK: MessageRegisterUpdate,
        REGISTER_UPDATE_KO: MessageRegisterUpdate,
        KEEP_ALIVE_OK: MessageAlive,
        KEEP_ALIVE_KO: MessageAlive,
    }

    @classmethod
    def create(cls, message_type, data):
        return cls.MESSAGES[message_type](message_type, data)

