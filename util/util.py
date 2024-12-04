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
            dim=stat(Path(dir_name, elem)).st_size
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

    @classmethod
    def find_search_string(cls, search_string):
        results = {}
        words = [w.lower() for w in search_string.split()]
        from server.storage import Storage
        for uid, peer in Storage.db.items():
               for content in peer.contents_list:
                  value = 0 
                  filename = content.filename.lower()
                  score = sum([filename.count(w) for w in words])
                  tmp = {
                    'uid': uid,
                    'username': peer.username,
                    'ip': peer.ip,
                    'filename': content.filename,
                    'dimension': content.dimension,
                    'sha1': content.sha1,
                  }
                  if score == 0: continue
                  if score in results:
                      results[score].append('{filename}\n{dimension}\n{sha1}\n{username}\n{uid}\n{ip}\n'.format(**tmp))
                  else:
                      results[score] = ['{filename}\n{dimension}\n{sha1}\n{username}\n{uid}\n{ip}\n'.format(**tmp)]
        data = []
        for list_position in dict(sorted(results.items())).values():
             for l in list_position:
                 data.append(l)
        #return "".join(dict(sorted(results.items())).values())
        return "".join(data)
