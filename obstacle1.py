# sonar obstacle avoiding bot in python
 
# Import required Python libraries
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)
 
GPIO_TRIGGER1 = 29
GPIO_ECHO1 = 31
 
GPIO_TRIGGER2 = 36
GPIO_ECHO2 = 37
 
GPIO_TRIGGER3 = 33
GPIO_ECHO3 = 35
 
MOTOR1B=18
MOTOR1E=22
 
MOTOR2B=40
MOTOR2E=32
 
# Set pins as output and input
GPIO.setup(GPIO_TRIGGER1,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO1,GPIO.IN)      # Echo
GPIO.setup(GPIO_TRIGGER2,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO2,GPIO.IN)
GPIO.setup(GPIO_TRIGGER3,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO3,GPIO.IN)
# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER2, False)
GPIO.output(GPIO_TRIGGER1, False)
GPIO.output(GPIO_TRIGGER3, False)
 
def sonar(GPIO_TRIGGER,GPIO_ECHO):
                # Send 10us pulse to trigger
                GPIO.output(GPIO_TRIGGER, False)
                time.sleep(0.01)
                GPIO.output(GPIO_TRIGGER, True)
                time.sleep(0.00001)
                GPIO.output(GPIO_TRIGGER, False)
 
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
 
GPIO.setup(MOTOR1B, GPIO.OUT)
GPIO.setup(MOTOR1E, GPIO.OUT)
 
GPIO.setup(MOTOR2B, GPIO.OUT)
GPIO.setup(MOTOR2E, GPIO.OUT)
def forward():
        GPIO.output(MOTOR1B, GPIO.HIGH)
        GPIO.output(MOTOR1E, GPIO.LOW)
        GPIO.output(MOTOR2B, GPIO.LOW)
        GPIO.output(MOTOR2E, GPIO.HIGH)
 
def reverse():
        GPIO.output(MOTOR1B, GPIO.LOW)
        GPIO.output(MOTOR1E, GPIO.HIGH)
        GPIO.output(MOTOR2B, GPIO.HIGH)
        GPIO.output(MOTOR2E, GPIO.LOW)
 
def rightturn():
        GPIO.output(MOTOR1B,GPIO.LOW)
        GPIO.output(MOTOR1E,GPIO.HIGH)
        GPIO.output(MOTOR2B,GPIO.LOW)
        GPIO.output(MOTOR2E,GPIO.HIGH)
 
def leftturn():
        GPIO.output(MOTOR1E,GPIO.HIGH)
        GPIO.output(MOTOR1B,GPIO.LOW)
        GPIO.output(MOTOR2E,GPIO.HIGH)
        GPIO.output(MOTOR2B,GPIO.LOW)
 
while True:
    try:
        distance2= sonar(GPIO_TRIGGER2,GPIO_ECHO2)
        distance1= sonar(GPIO_TRIGGER1,GPIO_ECHO1)
        distance3= sonar(GPIO_TRIGGER3,GPIO_ECHO3)
	print distance2, distance1, distance3  
	if(distance3<20 and distance2>20 and distance1>20):
		rightturn()
		time.sleep(0.3)
		forward()
		time.sleep(0.3)
	elif(distance1<20 and distance2>20 and distance3>20):
		leftturn()
		time.sleep(0.3)
		forward()
		time.sleep(0.3)
	elif(distance2>20 and distance3>20 and distance1>20):
		forward()
		time.sleep(0.3)
	elif(distance2<20 and distance3>20 and distance1<20):
		reverse()
		time.sleep(0.3)
		leftturn()
		time.sleep(0.3)
	elif(distance2<20 and distance1>20 and distance3<20):
		reverse()
		time.sleep(0.3)
		rightturn()
		time.sleep(0.3)
	elif(distance2<20 and distance1>20 and distance3>20):
		reverse()
		time.sleep(0.3)
		leftturn()
		time.sleep(0.3)
	elif(distance2>20 and distance1<20 and distance3<20):
		forward()
		time.sleep(0.5)
        else:
                forward()
    except KeyboardInterrupt:
        GPIO.output(MOTOR1E,GPIO.LOW)
        GPIO.output(MOTOR1B,GPIO.LOW)
        GPIO.output(MOTOR2E,GPIO.LOW)
        GPIO.output(MOTOR2B,GPIO.LOW)
        GPIO.cleanup()