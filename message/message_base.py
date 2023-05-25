from .message import Message


class MessageBase(Message):
    def __init__(self, mtype,  data):
        super().__init__(mtype, data)
        self.set_payload()
        self.set_header()

    def get_payload(self):
        pass

    def get_header(self):
        pass

    def set_payload(self):
        payload_in_bytes = bytes(self._data, 'utf-8')
        self._payload = payload_in_bytes

    def set_header(self):
        message_number = self._mtype
        padding_message_number = message_number.to_bytes(2, byteorder='little')

        # We need to send as  first elem of our message the length of
        # message's payload.  This integer (obtained from len() func)
        # must be converted in its byte representation (bytes() func)
        # The lenght of the payload is the  first elem in our message
        # and it (in protocol message) is 16bit (2 bytes) so if it is
        # less than 2 bytes (just 1 byte) we need to add 8 zeros bits
        # in other words we have to add padding
        padding_payload_size = len(self._payload).to_bytes(2, byteorder='little')
        header_in_bytes = padding_payload_size + padding_message_number
        self._header = header_in_bytes

    def pack(self):
        return self._header + self._payload
