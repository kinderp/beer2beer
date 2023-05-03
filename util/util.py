import os
import random

from server.storage import Storage


MAX_USERS = 1000

class Util:
    def __init__(self):
        pass

    @classmethod
    def generate_userid(self):
        return str(Storage.free_ids.pop())
