from .message_base import MessageBase


class MessageAlive(MessageBase):
    def __init__(self, mtype, data):
        super().__init__(mtype, data)
        self.id = None

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
        """login_tokens = self._data.split()
        if login_tokens:
            # TODO: we'd like to check out of index
            # in case our client is sending  a  bad
            # formatted inout message (e.g. missing
            # id or username)"""

        pass

