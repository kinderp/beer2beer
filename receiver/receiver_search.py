from message.messages_codes import SEARCH_FILE
from message.messages_factory import MessagesFactory
from util.session import Session


class ReceiverSearch:
    def __init__(self, host, port, payload):
        self._host = host
        self._port = port
        self._payload = payload

    def search(self, args=None):
        search_message = MessagesFactory.create(
                message_type=SEARCH_FILE,
                data=self._payload
        )
        session = Session(self._host, self._port)
        session.connect()
        session.send_message(search_message)
        response = session.recv_message()
        return response
