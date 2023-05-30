from message.messages_codes import REGISTER_UPDATE
from message.messages_factory import MessagesFactory
from util.session import Session


class ReceiverRegisterUpdate:
    def __init__(self, host, port, payload):
        self._host = host
        self._port = port
        self._payload = payload

    def register_update(self, args=None):
        register_update_message = MessagesFactory.create(
                message_type=REGISTER_UPDATE,
                data=self._payload
        )
        session = Session(self._host, self._port)
        session.connect()
        session.send_message(register_update_message)
        response = session.recv_message()
        return response
