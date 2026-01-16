import time
from random import uniform
import sys

def slowPrint(text, delay=uniform(0.01,0.3)):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
