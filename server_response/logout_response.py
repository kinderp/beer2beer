from .server_response import ServerResponse
from message.messages_codes import LOGOUT, LOGOUT_OK, LOGOUT_KO
from message.messages_factory import MessagesFactory

class LogoutResponse(ServerResponse):
    def __init__(self, message):
        super().__init__(message)

    def reply(self, args = None):
        self.message.unpack()
        username = self.message.username
        md5pwd = self.message.md5pwd
        user_id = self.message.id
        if username is None or md5pwd is None or user_id is None:
            output_message = MessagesFactory.create(LOGOUT_KO, "LOGOUT_KO")
        else:
            output_message = MessagesFactory.create(LOGOUT_OK, "LOGOUT_OK")
        return output_message
