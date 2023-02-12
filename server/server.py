from concurrent import futures as cf
import socket


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

    def handle(self, new_sock, address):
        while True:
            first_chunk = new_sock.recv(2) # read first 2 bytes (payload len)
            if not first_chunk: break
            second_chunk = new_sock.recv(2) # read second 2 bytes (type of mes)
            payload_len = int.from_bytes(first_chunk, "little")
            type_of_message = int.from_bytes(second_chunk, "little")
            payload = new_sock.recv(payload_len)
            print(payload.decode('utf-8'))
        new_sock.close()
        print("[*] Disconnected from ", address)

    def run(self):
        with cf.ThreadPoolExecutor(self._threads) as e:
            try:
                while True:
                    new_sock, address = self._servsock.accept()
                    e.submit(self.handle, new_sock, address)
            except KeyboardInterrupt:
                pass
            finally:
                self._servsock.close()
