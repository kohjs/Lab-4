import RPi.GPIO as GPIO

from time import sleep

def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN)
    GPIO.setup(24, GPIO.OUT)


def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        ret = 1


    return ret
def led_blink():
    while True:
        if read_slide_switch():
            GPIO.output(24, GPIO.HIGH)
            sleep(5)
            GPIO.output(24, GPIO.LOW)
            sleep(5)
        else:
            GPIO.output(24, GPIO.LOW)
        

def main():
    init()
