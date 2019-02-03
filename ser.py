import serial
from threading import Thread

keyDown = None

def thread1(threadname):
    s = serial.Serial("/dev/ttyUSB1", 1200, timeout=5)
    while True:
        global keyDown
        line = s.readline()
        if "Port" in line and "down" in line:
            if "0" in line: keyDown = 0
            elif ":" in line: keyDown = 1
            elif "2" in line: keyDown = 2
            elif "3" in line: keyDown = 3
            elif "4" in line: keyDown = 4
            elif "5" in line: keyDown = 5
            elif "6" in line: keyDown = 6
            elif "7" in line: keyDown = 7
            elif "8" in line: keyDown = 8
            elif "9" in line: keyDown = 9
            elif ";" in line: keyDown = 10
            elif ">" in line: keyDown = 11
            elif "<" in line: keyDown = 12

