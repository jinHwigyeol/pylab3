import os
import sys
import errno
import signal
import socket

BACKLOG = 5
host =''
port = 10002

def collect_zombie(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid ==0:
                break
        except:
            break

def do_echo(sock):
    while True:
        message = sock.recv(1024)
        if message:
            sock.sendall(message)
        else:
            return

signal.signal(signal.SIGCHLD, collect_zombie)

#conn_sock : 연결용으로 사용

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#인수 생략으로 인해 TCP 사용

conn_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#reuse the port : REUSEADDR

conn_sock.bind((host, port))
conn_sock.listen(BACKLOG)
#BACKLOG = 대기열의 숫자

print('Listening on port %d...' % port)

while True:
    try:
        data_sock, client_address = conn_sock.accept()
        print('Got request from %s port %s...' %client_address)

    except IOError as e:
        code, msg =e.args
        if code == errno.EINTR:
            continue
        else:
            raise

    pid = os.fork()
    if pid == 0:
        conn_sock.close()
        do_echo(data_sock)
        os._exit(0)

    data_sock.close()