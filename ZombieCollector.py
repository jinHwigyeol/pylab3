import signal
import time
import os
import sys

def collect_zombie(signum, frame):
    print("SIGCHILD dilivered... ")
    time.sleep(10)
    pid, status = os.waitpid(-1, os.WNOHANG)
    print("zombie process removed...")

signal.signal(signal.SIGCHLD, collect_zombie)
pid = os.fork()

if pid==0:
    print("child process running...")
    time.sleep(10)
    print("child process exiting...")
    os._exit(0)

time.sleep(30)
sys.exit(0)