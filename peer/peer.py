import socket


class Peer:
    def __init__(self):
        pass

    def connect(self, host='localhost', port=8888):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            print("[*] Peer Connected to server")
            payload = "user\npassword\n1234"
            payload_in_bytes = bytes(payload, 'utf-8')
            payload_size = len(payload_in_bytes)
            header = [payload_size, 2]
            header_in_bytes = bytes([payload_size, 2])
            message = header_in_bytes + payload_in_bytes
            print(message)
            sock.sendall(message)
            
