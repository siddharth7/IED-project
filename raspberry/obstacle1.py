# sonar obstacle avoiding bot in python

# Import required Python libraries
import time
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 24
GPIO_ECHO = 25

MLEFT = 17
MRIGHT =18

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
time.sleep(0.5)

def sonar(n):
        # Send 10us pulse to trigger
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        start = time.time()

       # this doesn't allow for timeouts !

        while GPIO.input(GPIO_ECHO)==0:
                start = time.time()

        while GPIO.input(GPIO_ECHO)==1:
                stop = time.time()

        # Calculate pulse length
        elapsed = stop-start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * 34000

        # That was the distance there and back so halve the value
        distance = distance / 2

        return distance

GPIO.setup(MLEFT, GPIO.OUT)
GPIO.setup(MRIGHT, GPIO.OUT)

sleep (1)

# both motors forward
GPIO.output(MLEFT, 1)
GPIO.output(MRIGHT, 1)

while True:

        time.sleep(0.3)

        distance = sonar (0)
        print distance

        if (distance < 10):
                # spin right
                GPIO.output(MRIGHT, 0)
                time.sleep(0.7)
                # forwards again
                GPIO.output(MRIGHT, 1)
