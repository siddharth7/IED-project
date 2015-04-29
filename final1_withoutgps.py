# sonar obstacle avoiding bot in python
 
# Import required Python libraries
import time
import RPi.GPIO as GPIO
from pynmea import nmea
import subprocess
import os
 
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

time.sleep(100)
 
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
		print "wewewewewe"
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
    GPIO.output(MOTOR1B,GPIO.HIGH)
    GPIO.output(MOTOR1E,GPIO.LOW)
    GPIO.output(MOTOR2B,GPIO.HIGH)
    GPIO.output(MOTOR2E,GPIO.LOW)
f1=open("finalwaypoints.txt","r")
for line in f1:
    while True:
        try:
            os.chmod('script.sh',0o755)
            subprocess.call("./script.sh")
            s1=0
            s2=0
            n=0
            file1=open('input.txt','r')
            for line1 in file1:
                if(line1[1:6]=="GPGGA"):
                    gpgga=nmea.GPGGA()
                    gpgga=nmea.GPGGA()
                    gpgga.parse(line1)
                    l1=str(gpgga.latitude)[0:2]
                    l2=str(gpgga.latitude)[2:]
                    l2=float(l2)/60
                    l3=str(gpgga.longitude)[1:3]
                    l4=str(gpgga.longitude)[3:]
                    l4=float(l4)/60
                    s1+=float(l1)+l2
                    s2+=float(l3)+l4
                    #print float(l1)+l2,float(l3)+l4
                    n+=1
            var1=s1/n
            var2=s2/n
	    print var1,var2
	    finalline=line.split() 
            lat1=finalline[0]
            long1=finalline[1]
            lat2=finalline[2]
            long2=finalline[3]
	    print lat1,long1,lat2,long2
            distance2= sonar(GPIO_TRIGGER2,GPIO_ECHO2)
            distance1= sonar(GPIO_TRIGGER1,GPIO_ECHO1)
            distance3= sonar(GPIO_TRIGGER3,GPIO_ECHO3)
            print "lets go"
	    if(lat1>var1 and lat2>var1 and long1>var2 and long2>var2):
		print "if condition 1 "
                if(distance3<20 and distance2>20 and distance1>20):
			print "if condition 1 part 1"
			rightturn()
			time.sleep(0.3)
			forward()
			time.sleep(0.3)
	    	elif(distance1<20 and distance2>20 and distance3>20):
			print "if condition 1 part 2"
			leftturn()
			time.sleep(0.3)
			forward()
			time.sleep(0.3)
		elif(distance2>20 and distance3>20 and distance1>20):
			print "if condition 1 part 3"
			forward()
			time.sleep(0.3)
		elif(distance2<20 and distance3>20 and distance1<20):
			print "if condition 1 part 4"
			reverse()
			time.sleep(0.3)
			leftturn()
			time.sleep(0.3)
		elif(distance2<20 and distance1>20 and distance3<20):
			print "if condition 1 part 5"
			reverse()
			time.sleep(0.3)
			rightturn()
			time.sleep(0.3)
		elif(distance2<20 and distance1>20 and distance3>20):
			print "if condition 1 part 6"
			reverse()
			time.sleep(0.3)
			leftturn()
			time.sleep(0.3)
		elif(distance2>20 and distance1<20 and distance3<20):
			print "if condition 1 part 7"
			forward()
			time.sleep(0.5)
        	else:
                	print "if condition 1 part 8"
			forward()
            elif(lat1<var1 and var1<lat2 and long1<var2 and var2<long2):
                print "print "elif condition 1"
            else:
                print "in else condition at last"
        except KeyboardInterrupt:
            GPIO.output(MOTOR1E,GPIO.LOW)
            GPIO.output(MOTOR1B,GPIO.LOW)
            GPIO.output(MOTOR2E,GPIO.LOW)
            GPIO.output(MOTOR2B,GPIO.LOW)
            GPIO.cleanup() 