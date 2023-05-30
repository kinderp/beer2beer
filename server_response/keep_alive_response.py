from server_response import ServerResponse
from message.messages_codes import  KEEP_ALIVE_OK, KEEP_ALIVE_KO
from message.messages_factory import MessagesFactory
from server.storage import Storage


class Keep_Alive_Response(ServerResponse):
    def __init__(self, message):
        super().__init__(message)

    def reply(self, args = None):
        self.message.unpack()
        user_id = self.message.id
        if Storage.get_row(str(user_id)) is not None:
            output_message = MessagesFactory.create(KEEP_ALIVE_OK, "KEEP_ALIVE_OK")
        else:
            output_message = MessagesFactory.create(KEEP_ALIVE_KO, "KEEP_ALIVE_KO")
        return output_message