from .server_response import ServerResponse
from util.util import Util
from server.storage import Storage, Peer
from message.messages_codes import REGISTER, REGISTER_OK, REGISTER_KO
from message.messages_factory import MessagesFactory


class RegisterResponse(ServerResponse):
    def __init__(self, message):
        super().__init__(message)

    def reply(self, args=None):
        self.message.unpack() # set payload's items
        # after unpack we should have a ready message
        # let's get single item
        username = self.message.username
        md5pwd = self.message.md5pwd
        contents_list = self.message.contents_list
        Storage.add_row(Util.generate_userid(), Peer(username, md5pwd, 0, contents_list))
        return MessagesFactory.create(REGISTER_OK, "REGISTER_OK")
