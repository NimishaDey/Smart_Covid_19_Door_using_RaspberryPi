import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A=36
Motor1B=38
Motor1E=40

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

try:
	print ("Turning motor on")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	
	sleep(15)
	print("Stopping motor")
	GPIO.output(Motor1E,GPIO.LOW)
	
finally:
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.cleanup()
