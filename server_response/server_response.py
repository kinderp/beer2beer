from abc import ABCMeta, abstractmethod

class ServerResponse:
    __metaclass__ = ABCMeta

    def __init__(self, message):
        self.message = message

    @abstractmethod
    def reply(args):
        pass

