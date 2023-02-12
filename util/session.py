import socket
from message.messages_factory import MessagesFactory


class Session:
    def __init__(self, host, port, sock=None):
        self._host = host
        self._port = port
        if sock is None:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.connect((self._host, self._port))
        else:
            self._sock = sock

    def connect(self):
        if self._sock is None:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.connect((self._host, self._port))
            print("[*] New Session connected to {} on port {}".format(self._host, self._port))

    def disconnect(self):
        self._sock.close()

    def send_message(self, message):
        #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        #sock.connect((self._host, self._port))
        #print("[*] New Session, Peer Connected to server")
        self._sock.sendall(message.pack())

    def recv_message(self):
        first_chunk = self._sock.recv(2) # read first 2 bytes (payload len)
        if not first_chunk: return None
        second_chunk = self._sock.recv(2) # read second 2 bytes (type of mes)
        payload_len = int.from_bytes(first_chunk, "little")
        type_of_message = int.from_bytes(second_chunk, "little")
        payload = self._sock.recv(payload_len)
        m = MessagesFactory.create(type_of_message, payload.decode('utf-8'))
        print(payload.decode('utf-8'))
        return m

