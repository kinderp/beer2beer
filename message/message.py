from abc import ABCMeta, abstractmethod


class Message:
    __metaclass__ = ABCMeta

    def __init__(self, mtype, data):
        self._mtype = mtype # message type (LOGIN, REGISTER...)
        self._data = data   # data payload
        self._header = None
        self._payload = None

    @abstractmethod
    def pack():
        pass

    @abstractmethod
    def unpack():
        pass

    @abstractmethod
    def set_payload():
        pass

    @abstractmethod
    def set_header():
        pass

    @abstractmethod
    def get_payload():
        pass

    @abstractmethod
    def get_header():
        pass
