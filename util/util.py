import os.path
from os import listdir, stat, path
import random
import hashlib
from pathlib import Path
from server.storage import Storage
from server.storage import Content


MAX_USERS = 1000

class Util:
    def __init__(self):
        pass

    @classmethod
    def generate_userid(cls):
        return str(Storage.free_ids.pop())

    @classmethod
    def browse_dir(cls, dir_name):
        results = []
        list_of_files=listdir(dir_name)
        for elem in list_of_files:
            if path.isdir(Path(dir_name, elem)): continue
            dim=stat(elem).st_size
            sha1 = cls.sha1sum(dir_name, elem)
            tmp = Content(elem, dim, sha1)
            results.append(tmp)
        return results

    @classmethod
    def sha1sum(cls, dir_name, file_name):
        BUF_SIZE = 65536
        sha1 = hashlib.sha1()
        absolute_filename = Path(dir_name, file_name)
        with open(absolute_filename, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
        return sha1.hexdigest()
