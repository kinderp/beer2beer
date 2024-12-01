from .server_response import ServerResponse
from util.util import Util
from server.storage import Storage, Peer
from message.messages_codes import SEARCH_FILE, SEARCH_FILE_OK, SEARCH_FILE_KO
from message.messages_factory import MessagesFactory


class SearchResponse(ServerResponse):
    def __init__(self, message):
        super().__init__(message)

    def reply(self, args=None):
        self.message.unpack() # set payload's items
        # after unpack we should have a ready message
        # let's get single item
        search_string = self.message.search_string
        results = Util.find_search_string(search_string)
        payload = "{}\n{}".format("SEARCH_FILE_OK", results)
        return MessagesFactory.create(SEARCH_FILE_OK, payload)
