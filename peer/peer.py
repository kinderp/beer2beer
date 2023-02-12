import socket


class Peer:
    def __init__(self):
        pass

    def connect(self, host='localhost', port=8888):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            print("[*] Peer Connected to server")
            payload = "user\npassword\n1234"
            # Right here we transform a string (payload) in a sequence of
            # bytes using utf-8 encoding. So payload_in_bytes will host a
            # sequence  of bytes  representing in utf-8 our origin string
            payload_in_bytes = bytes(payload, 'utf-8')
            # We need to send as  first elem of our message the length of
            # message's payload.  This integer (obtained from len() func)
            # must be converted in its byte representation (bytes() func)
            payload_size_in_bytes = bytes([len(payload_in_bytes)])
            # The lenght of the payload is the  first elem in our message
            # and it (in protocol message) is 16bit (2 bytes) so if it is
            # less than 2 bytes (just 1 byte) we need to add 8 zeros bits
            # in other words we have to add padding
            padding_payload_size = payload_size_in_bytes + bytes(2 - len(payload_size_in_bytes))

            message_number = 2
            message_number_in_bytes = bytes([message_number])
            padding_message_number = message_number_in_bytes + bytes(2 - len(message_number_in_bytes))
            header_in_bytes = padding_payload_size + padding_message_number
            message = header_in_bytes + payload_in_bytes
            print(message)
            sock.sendall(message)
            
