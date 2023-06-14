from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
 #----Now comes the sockets part----
HOST = '172.16.254.13'
PORT = 33000



BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
client_socket.send(bytes("Barrera 3", "utf8"))