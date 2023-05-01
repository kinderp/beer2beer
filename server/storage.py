import shelve

from settings import ShellSettings

DB_NAME = "storage.bin"
DB_SETTINGS = ShellSettings.DIRECTORY_SETTINGS + "/" + DB_NAME


class Peer:
    def __init__(self, username, md5pwd, status, contents_list=[]):
        self.username = username
        self.md5pwd = md5pwd
        self.status = status
        self.contents_list = contents_list

    def set_status(self, status):
        self.status = status

    def set_contents_list(self, c_list):
        self.contents_list = c_list


class Content:
    def __init__(self, filename, dimension, sha1):
        self.filename = filename
        self.dimension = dimension
        self.sha1 = sha1


class Storage:
    db = None

    @classmethod
    def load(cls):
        cls.db = shelve.open(DB_SETTINGS)

    @classmethod
    def save(cls):
        if cls.db:
            cls.db.close()

    @classmethod
    def get_row(cls, index):
        if index in cls.db:
            return cls.db[index]
        return None

    @classmethod
    def add_row(cls, index, row):
        cls.db[index] = row

    @classmethod
    def del_row(cls, index):
        del cls.db[index]
