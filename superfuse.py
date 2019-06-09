import sys, RPi.GPIO as GPIO, pylirc, mutex, datetime
from gpiozero import MotionSensor
from time import sleep
from threading import Thread
import signal

# Setup
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

pir = MotionSensor(24)
pylirc.init("webflash", "~/.lircrc")

def off():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
def on():
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
def toggle():
    global state
    if state:
        state = False
        off()
    elif not state:
        state = True
        on()
def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

def motion():
    global state
    while True:
        if pir.motion_detected:
            state = True
            on()
            timeout = 0
            timeoutLen = 5
            print "Entering timeout for", timeoutLen, "seconds at", datetime.datetime.now()
            while timeout < timeoutLen:
                if not state:
                    print "Non-motion source got OFF at", datetime.datetime.now()
                    break
                sleep(1)
                timeout += 1
            print "Exiting timeout at", datetime.datetime.now(), "and entering cooldown for", timeoutLen * 0.25, "seconds."
            state = False
            off()
            sleep(timeoutLen * 0.25)
def infrared():
    while True:
        if pylirc.nextcode():
            print "Detected IR. Toggling at", datetime.datetime.now()
            toggle()

if __name__ == "__main__":
    off()
    state = False
    motionThread = Thread(target = motion)
    infraredThread = Thread(target = infrared)
    motionThread.start()
    infraredThread.start()
    signal.signal(signal.SIGINT, signal_handler) # Not Working!!!
