from concurrent import futures as cf
import socket

from util.session import Session
from message.messages_factory import MessagesFactory
from message.messages_codes import LOGIN, LOGIN_OK, LOGIN_KO


class Server:
    def __init__(self, host='localhost', port=8888, queue=5, threads=20):
        self._host = host
        self._port = port
        self._queue = queue
        self._threads= threads

        self._servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._servsock.bind((self._host,self._port))
        self._servsock.listen(self._queue)
        print("[*] Starting Indexing Server...")
        print("[*] Serving at {}".format(self._servsock.getsockname()))
        print("[*] queue = {}".format(queue))
        print("[*] thread = {}".format(threads))

    def handle(self, new_session):
        while True:
            message_from_peer = new_session.recv_message()
            if not message_from_peer: break
            # process message from peer (decode and do some actions) and sent 
            # back a response
            output_message = MessagesFactory.create(LOGIN_OK, "LOGIN_OK")
            output_message.set_payload()
            output_message.set_header()
            new_session.send_message(output_message)
        new_session.disconnect()
        print("[*] Disconnected sesssion")

    def run(self):
        with cf.ThreadPoolExecutor(self._threads) as e:
            try:
                while True:
                    new_sock, address = self._servsock.accept()
                    new_session = Session(host=None, port=None, sock=new_sock)
                    e.submit(self.handle, new_session)
            except KeyboardInterrupt:
                pass
            finally:
                self._servsock.close()
