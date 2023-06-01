from .server_response import ServerResponse
from message.messages_codes import LOGIN, LOGIN_OK, LOGIN_KO
from message.messages_factory import MessagesFactory

from server.storage import Storage

class LoginResponse(ServerResponse):
    def __init__(self, message):
        super().__init__(message)

    def reply(self, args=None):
        self.message.unpack() # set payload's items
        # after unpack we should have a ready message
        # let's get single item
        username = self.message.username
        md5pwd = self.message.md5pwd
        user_id = self.message.id
        user_ip = self.message.ip
        db_response = Storage.get_row(user_id)
        if db_response:
            if db_response.username == username and db_response.md5pwd == md5pwd:
                output_message = MessagesFactory.create(LOGIN_OK, "LOGIN_OK")
                current_user = Storage.get_row(str(user_id))
                current_user.status = 1
                current_user.ip = user_ip
                Storage.add_row(str(user_id), current_user)
            else:
                output_message = MessagesFactory.create(LOGIN_KO, "LOGIN_KO_BAD_USER_OR_PWD")
            return output_message
        return MessagesFactory.create(LOGIN_KO, "LOGIN_KO_ID_NOT_FOUND")
