import os
import sys

pid = os.fork()
print("Hello, world")

sys.exit(0)