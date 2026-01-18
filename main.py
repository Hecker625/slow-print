import time
from random import uniform
import sys

def Print(text, delay=uniform(0,0.1)):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
