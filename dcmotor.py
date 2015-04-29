import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
i=0
while(i<10000) :
    try:
	i+=1
    #MOTOR1A=16
    	MOTOR1B=18
    	MOTOR1E=22


    #MOTOR2A=23
    	MOTOR2B=40
    	MOTOR2E=32

    #GPIO.setup(MOTOR1A, GPIO.OUT)
    	GPIO.setup(MOTOR1B, GPIO.OUT)
    	GPIO.setup(MOTOR1E, GPIO.OUT)

    #GPIO.setup(MOTOR2A, GPIO.OUT)
    	GPIO.setup(MOTOR2B, GPIO.OUT)
    	GPIO.setup(MOTOR2E, GPIO.OUT)

    
    	print "turning motor on"

    
    	GPIO.output(MOTOR1B, GPIO.HIGH)
    	GPIO.output(MOTOR1E, GPIO.LOW)

    
    	GPIO.output(MOTOR2B, GPIO.HIGH)
    	GPIO.output(MOTOR2E, GPIO.LOW)

    	sleep(2)

    	print "stopping motor"

    	#GPIO.output(MOTOR1E, GPIO.LOW)
    except KeyboardInterrupt:	
		GPIO.output(MOTOR1E,GPIO.LOW)
            	GPIO.output(MOTOR1B,GPIO.LOW)
            	GPIO.output(MOTOR2E,GPIO.LOW)
            	GPIO.output(MOTOR2B,GPIO.LOW)
            	GPIO.cleanup()

GPIO.cleanup()

            
