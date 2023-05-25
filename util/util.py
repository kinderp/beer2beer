import os.path
from os import listdir, stat
import random

from server.storage import Storage
from server.storage import Content


MAX_USERS = 1000

class Util:
    def __init__(self):
        pass

    @classmethod
    def generate_userid(self):
        return str(Storage.free_ids.pop())

    def browse_dir(self, dir_name):
        results = []
        list_of_files=listdir(dir_name)
        for elem in list_of_files:
            dim=stat(elem).st_size
            # TODO add sha1
            tmp = Content(elem, dim, "...")
            results.append(tmp)
        return results



