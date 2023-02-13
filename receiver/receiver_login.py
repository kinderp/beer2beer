from message.messages_codes import LOGIN
from message.messages_factory import MessagesFactory
from util.session import Session


class ReceiverLogin:
    def __init__(self, host, port, payload):
        self._host = host
        self._port = port
        self._payload = payload

    def login(self, args=None):
        login_message = MessagesFactory.create(
                message_type=LOGIN, 
                data=self._payload
        )
        session = Session(self._host, self._port)
        session.connect()
        session.send_message(login_message)
        response = session.recv_message()
        return response

