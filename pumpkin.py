import RPi.GPIO as GPIO
import time
import datetime
import pygame
import random
import os
import sys
import logging

logging.basicConfig(filename='/tmp/pumpkinpi.log',level=logging.INFO)

DIR = os.path.dirname(__file__)

GREEN_LED_1 = 25
GREEN_LED_2 = 24
RED_LED = 23

MOTION_SENSOR = 21

SCREAM_SOUND_FILE = os.path.join(DIR, "l1.wav")
H3_SOUND_FILE = os.path.join(DIR, "halloween-3-short.mp3")

SOUNDS = [os.path.join(DIR, "halloween-3-short.mp3"),
          os.path.join(DIR, "halloween-3-short.mp3"),
	  os.path.join(DIR, "stranger.mp3")]

PAUSE_TIME = 30

BLINK_PATTERNS = [
    [GREEN_LED_1, GREEN_LED_2],
    [GREEN_LED_1, GREEN_LED_2],
    [GREEN_LED_1, GREEN_LED_2, RED_LED],
    [RED_LED], [RED_LED],
    [GREEN_LED_1, RED_LED]
]



# BLINK MULTIPLE LEDS
def blink_led(led_pins=[], blink_time=0.25):
    for x in range(6):
    	for led_pin in led_pins:
        	GPIO.output(led_pin, GPIO.HIGH)
    	time.sleep(blink_time)

    	for led_pin in led_pins:
        	GPIO.output(led_pin, GPIO.LOW)
    	time.sleep(blink_time+0.05)


# SCARE ACTION
def boo():
    logging.info("Boo {0}".format(datetime.datetime.now()))
    pygame.mixer.music.load(SCREAM_SOUND_FILE)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        blink_led(random.choice(BLINK_PATTERNS), blink_time=0.1)

    pygame.mixer.music.load(random.choice(SOUNDS))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
	blink_led(random.choice(BLINK_PATTERNS))
   

def init():
	# INIT GPIO
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(GREEN_LED_1, GPIO.OUT)
	GPIO.setup(GREEN_LED_2, GPIO.OUT)
	GPIO.setup(RED_LED, GPIO.OUT)

	GPIO.setup(MOTION_SENSOR, GPIO.IN)


	# INIT PYGAME
	pygame.init()
	pygame.mixer.init()

	# TURN OFF LEDS 
	for led in [GREEN_LED_1, GREEN_LED_2, RED_LED]:
    		GPIO.output(led, GPIO.LOW)

if __name__ == '__main__':
	time.sleep(20)
	init()

	logging.info("Launching {0}".format(datetime.datetime.now()))

	while True:
    		if GPIO.input(MOTION_SENSOR):
        		boo()
        		time.sleep(PAUSE_TIME)
    		else:
    			time.sleep(0.5)
  
	GPIO.cleanup()
