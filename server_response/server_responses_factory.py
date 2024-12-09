from message.messages_codes import LOGIN
from message.messages_codes import LOGOUT
from message.messages_codes import REGISTER
from message.messages_codes import REGISTER_UPDATE
from message.messages_codes import SEARCH_FILE
from .login_response import LoginResponse
from .register_response import RegisterResponse
from .register_update_response import RegisterUpdateResponse
from .logout_response import LogoutResponse
from .search_response import SearchResponse


class ServerResponsesFactory:
    MESSAGES = {
        LOGIN : LoginResponse,
        LOGOUT: LogoutResponse,
        REGISTER : RegisterResponse,
        REGISTER_UPDATE: RegisterUpdateResponse,
        SEARCH_FILE: SearchResponse,
    }

    @classmethod
    def create(cls, message):
        return cls.MESSAGES[message._mtype](message)


