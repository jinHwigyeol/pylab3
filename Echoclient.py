import socket
import sys

host ='203.250.133.88'
port = 10002
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print("connecting to %s port %s" % server_address)
sock.connect(server_address)

message = input("Enter message :")

while message != "quit":
    try:
        data = bytes(message, encoding='utf-8')
        sock.sendall(data)
        data = sock.recv(BUFF_SIZE)
        print("received from server : %s" % data.decode())

    except Exception as e:
        print("Exception: %s" %str(e))
        sys.exit(0)

    message = input("Enter message : ")

sock.close()