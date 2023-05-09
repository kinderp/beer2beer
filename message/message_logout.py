from .message_base import MessageBase

class MessageLogout(MessageBase):
    def __init__(self, mtype, data):
        super().__init__(mtype, data)
        self.username = None
        self.md5pwd = None
        self.id = None

    def set_payload(self):
        super().set_payload()

    def set_header(self):
        super().set_header()

    def pack(self):
        return super().pack()

    def unpack(self):
        self.username = None
        self.md5pwd = None
        self.id = None