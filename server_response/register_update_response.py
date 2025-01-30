from .server_response import ServerResponse
from server.storage import Storage, Peer
from message.messages_codes import REGISTER_UPDATE, REGISTER_UPDATE_OK, REGISTER_UPDATE_KO
from message.messages_factory import MessagesFactory


class RegisterUpdateResponse(ServerResponse):
    def __init__(self, message):
        super().__init__(message)

    def reply(self, args=None):
        self.message.unpack() # set payload's items
        # after unpack we should have a ready message
        # let's get single item
        username = self.message.username
        md5pwd = self.message.md5pwd
        contents_list = self.message.contents_list
        user_id = self.message.user_id
        Storage.del_row(user_id)
        Storage.add_row(user_id, Peer(username, md5pwd, 0, contents_list))
        payload = "{}\n{}".format("REGISTER_UPDATE_OK", str(user_id))
        return MessagesFactory.create(REGISTER_UPDATE_OK, payload)
