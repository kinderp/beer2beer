from message.messages_codes import LOGOUT
from message.messages_factory import MessagesFactory
from util.session import Session

class ReceiverLogout:
    def __init__(self, host, port, payload):
        self._host = host
        self._port = port
        self._payload = payload

    def logout(self, args = None):
        logout_message = MessagesFactory.create(message_type=LOGOUT, data=self._payload)
        session = Session(self._host,self._port)
        Session.connect()
        Session.send_message(logout_message)
        response = Session.recv_message()
        return response
