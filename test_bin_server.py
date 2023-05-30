from util.session import BinSession
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9999))
session = BinSession(sock)
session.send_file("/home/antonio/Downloads/music.mp3")
