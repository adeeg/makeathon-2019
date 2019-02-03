import serial
from threading import Thread

keyDown = None

def thread1(threadname):
    s = serial.Serial("/dev/ttyUSB0", 1200, timeout=5)
    while True:
        global keyDown
        keyDown = s.readline()

