from message.messages_factory import MessagesFactory

from . import LOGGER

import socket


class BinSession:
    def __init__(self, sock):
        if not sock:
            return False
        self._sock = sock

    def disconnect(self):
        self._sock.close()

    def send_file(self, filename):
        LOGGER.info("[->] Sending bin file => {}".format(filename))
        with open(filename, 'rb') as f:
            filename_in_bytes = bytes(filename, 'utf-8')
            self._sock.sendall(len(filename_in_bytes).to_bytes(8, 'big'))
            self._sock.sendall(filename_in_bytes)
            raw = f.read()
            # Send actual length ahead of data, with fixed byteorder and size
            self._sock.sendall(len(raw).to_bytes(8, 'big'))
            # You have the whole thing in memory anyway; don't bother chunking
            self._sock.sendall(raw)

    def recv_file(self):
        expected_size = b""
        while len(expected_size) < 8:
            more_size = self._sock.recv(8 - len(expected_size))
            if not more_size:
                raise Exception("Short file length received")
            expected_size += more_size

        # Convert to str, the expected file length
        expected_size = int.from_bytes(expected_size, 'big')

        # Until we've received the expected amount of data, keep receiving
        packet = b""  # Use bytes, not str, to accumulate
        while len(packet) < expected_size:
            buffer = self._sock.recv(expected_size - len(packet))
            if not buffer:
                raise Exception("Incomplete file received")
            packet += buffer
        filename = packet.decode('utf-8')

        LOGGER.info("[<-] Receiving bin file => {}".format(filename))
        # Get the expected length (eight bytes long, always)
        expected_size = b""
        while len(expected_size) < 8:
            more_size = self._sock.recv(8 - len(expected_size))
            if not more_size:
                raise Exception("Short file length received")
            expected_size += more_size

        # Convert to int, the expected file length
        expected_size = int.from_bytes(expected_size, 'big')

        # Until we've received the expected amount of data, keep receiving
        packet = b""  # Use bytes, not str, to accumulate
        while len(packet) < expected_size:
            buffer = self._sock.recv(expected_size - len(packet))
            if not buffer:
                raise Exception("Incomplete file received")
            packet += buffer
        with open(filename.split("/")[-1], 'wb') as f:
            f.write(packet)


class Session:
    def __init__(self, host, port, sock=None):
        self._host = host
        self._port = int(port) if port else None
        if sock is None:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.connect((self._host, self._port))
        else:
            self._sock = sock
        self._remote_host, self._remote_port = self._sock.getpeername()

    def connect(self):
        if self._sock is None:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.connect((self._host, self._port))
            #print("[*] New Session connected to {} on port {}".format(self._host, self._port))

    def disconnect(self):
        self._sock.close()

    def send_message(self, message):
        #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        #sock.connect((self._host, self._port))
        #print("[*] New Session, Peer Connected to server")
        LOGGER.info( "[->] {} Sending msg id   => {}".format(self._remote_port, message._mtype))
        LOGGER.debug("[->] {} Sending msg data => (payload down below)\n{}".format(
            self._remote_port, message._data))
        self._sock.sendall(message.pack())

    def recv_message(self):
        first_chunk = self._sock.recv(2) # read first 2 bytes (payload len)
        if not first_chunk: return None
        second_chunk = self._sock.recv(2) # read second 2 bytes (type of mes)
        payload_len = int.from_bytes(first_chunk, "little")
        type_of_message = int.from_bytes(second_chunk, "little")
        payload = self._sock.recv(payload_len)
        m = MessagesFactory.create(type_of_message, payload.decode('utf-8'))
        #print(payload.decode('utf-8'))
        LOGGER.info("[<-] {} Received msg id   => {}".format(self._remote_port, m._mtype))
        LOGGER.info("[<-] {} Received msg data => (payload down below)\n{}".format(
            self._remote_port, m._data))
        return m

