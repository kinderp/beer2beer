from message.messages_codes import KEEP_ALIVE
from message.messages_factory import MessagesFactory
from util.session import Session


class ReceiverAlive:
    def __init__(self, host, port, payload):
        self._host = host
        self._port = port
        self._payload = payload

    def alive(self, args=None):
        alive_message = MessagesFactory.create(
                message_type=KEEP_ALIVE,
                data=self._payload
        )
        session = Session(self._host, self._port)
        session.connect()
        session.send_message(alive_message)
        response = session.recv_message()
        return response

