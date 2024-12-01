from .message_base import MessageBase


class MessageSearch(MessageBase):
    def __init__(self, mtype, data):
        super().__init__(mtype, data)
        self.search_string = None

    def set_payload(self):
        # ovveride this method if you need to do
        # something new or different than normal
        # cases
        super().set_payload()

    def set_header(self):
        # ovveride this method if you need to do
        # something new or different than normal
        # cases
        super().set_header()
    
    def pack(self):
        # ovveride this method if you need to do
        # something new or different than normal
        # cases
        return super().pack()

    def unpack(self):
        self.search_string = self._data
