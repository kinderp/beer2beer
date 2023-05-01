import hashlib

from server.storage import *


Storage.load() # load or create (if it does not exist)

uno_contents_list = []

file1 = "a.mp3"
dimension1 = 1000

file2 = "b.mp3"
dimension2 = 10000

file3 = "c.avi"
dimension3 = 5000

file4 = "d.pdf"
dimension4 = 200

c1 = Content(file1, dimension1, hashlib.sha1(bytes(file1, "utf-8")).hexdigest())
c2 = Content(file2, dimension2, hashlib.sha1(bytes(file2, "utf-8")).hexdigest())
c3 = Content(file3, dimension3, hashlib.sha1(bytes(file3, "utf-8")).hexdigest())
c4 = Content(file4, dimension4, hashlib.sha1(bytes(file4, "utf-8")).hexdigest())

uno_id = "1"
username = "uno"
pwd = "1234"
contents_list = [c1, c2, c3, c4]
uno = Peer(username, pwd, contents_list)

due_id = "3"
username = "due"
pwd = "9876"
contents_list = [c1, c4]
due = Peer(username, pwd, contents_list)

Storage.add_row(uno_id, uno)
uno_from_db = Storage.get_row(uno_id)

Storage.add_row(due_id, due)
due_from_db = Storage.get_row(due_id)

Storage.save()

Storage.load()
#print(Storage.db)
#print(Storage.db[uno_id])
#print(Storage.db[due_id])
