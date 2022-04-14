import signal
import time

def handler(signum, frame):
    print("signalhandler called with signal {}".format(signum))
    signal.signal(signal.SIGINT, signal.SIG_DFL)

signal.signal(signal.SIGINT, handler)

while True:
    print("waiting...")
    time.sleep(5)