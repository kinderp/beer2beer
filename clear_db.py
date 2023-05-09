from server.storage import *
Storage.load()
for elem in Storage.db.keys():
    del Storage.db[elem]