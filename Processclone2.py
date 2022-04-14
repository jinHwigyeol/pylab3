import os
import sys

new_pid = os.fork()

if new_pid ==0:
    pid = os.getpid()
    ppid = os.Getppid()
    print("child process : PID = %d PPID %d" %(pid, ppid))

else:
    pid = os.getpid()
    ppid = os.Getppid()
    print("parent process : PID = %d PPID = %d" %(pid,ppid))

sys.exit(0)