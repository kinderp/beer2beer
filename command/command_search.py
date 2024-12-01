from .command import Command
from receiver.receiver_search import ReceiverSearch


class CommandSearch(Command):
    def __init__(self, host, port, payload):
        self.__receiver = ReceiverSearch(host, port, payload)

    def execute(self, args=None):
        response = self.__receiver.search()
        # add here some login to check response
        # and return something to the caller
        return response
        

