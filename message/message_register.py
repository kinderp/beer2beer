from .message_base import MessageBase
from server.storage import Content


class MessageRegisterOk(MessageBase):
    def __init__(self, mtype, data):
        super().__init__(mtype, data)
        self.message_response = None
        self.id = None

    def set_payload(self):
        super().set_payload()

    def set_header(self):
        super().set_header()
    
    def pack(self):
        return super().pack()

    def unpack(self):
        register_tokens = self._data.split()
        if register_tokens:
            # TODO: we'd like to check out of index
            # in case our client is sending  a  bad
            # formatted input message (e.g. missing
            # id)
            self.message_response = register_tokens.pop(0)
            self.id = register_tokens.pop(0)
             

class MessageRegister(MessageBase):
    def __init__(self, mtype, data):
        super().__init__(mtype, data)
        self.username = None
        self.md5pwd = None 
        self.contents_list = []

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
        register_tokens = self._data.split()
        if register_tokens:
            # TODO: we'd like to check out of index
            # in case our client is sending  a  bad
            # formatted inout message (e.g. missing
            # id or username)
            self.username = register_tokens.pop(0)
            self.md5pwd = register_tokens.pop(0)
            for content in register_tokens:
                content_tokens = content.split("|")
                filename, dimension, sha1 = (content_tokens[0], content_tokens[1], content_tokens[2])
                self.contents_list.append(Content(filename, dimension, sha1))
             

