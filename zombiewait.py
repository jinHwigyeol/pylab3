import os
import sys
import time

pid = os.fork()

if pid ==0:
    time.sleep(10)
    print("child process exit...")
    os._exit(0)

time.sleep(20)

os.waitpid(pid, os.WNOHANG)
print("zombie process removed...")

time.sleep(20)
sys.exit(0)
