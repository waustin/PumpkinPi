import RPi.GPIO as GPIO
import time
import pygame
import random
import os

DIR = os.path.dirname(__file__)

GREEN_LED_1 = 25
GREEN_LED_2 = 24
RED_LED = 23

MOTION_SENSOR = 21

H3_SOUND_FILE = os.path.join(DIR, "halloween-3-short.mp3")

SOUNDS = [os.path.join(DIR, "halloween-3-short.mp3"),
          os.path.join(DIR, "halloween-3-short.mp3"),
	  os.path.join(DIR, "alive.wav"),
	  os.path.join(DIR, "l1.wav"),
	  os.path.join(DIR, "wolfhowl.wav")]

PAUSE_TIME = 6666660

BLINK_PATTERNS = [
    [GREEN_LED_1, GREEN_LED_2],
    [GREEN_LED_1, GREEN_LED_2],
    [GREEN_LED_1, GREEN_LED_2, RED_LED],
    [RED_LED], [RED_LED],
    [GREEN_LED_1, RED_LED]
]



# BLINK MULTIPLE LEDS
def blink_led(led_pins=[]):
    for x in range(5):
    	for led_pin in led_pins:
        	GPIO.output(led_pin, GPIO.HIGH)
    	time.sleep(0.25)

    	for led_pin in led_pins:
        	GPIO.output(led_pin, GPIO.LOW)
    	time.sleep(0.30)


# SCARE ACTION
def boo():
    pygame.mixer.music.load(random.choice(SOUNDS))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
	blink_led(random.choice(BLINK_PATTERNS))
   
 
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
#pygame.mixer.music.load(H3_SOUND_FILE)

# TURN OFF LEDS 
for led in [GREEN_LED_1, GREEN_LED_2, RED_LED]:
    GPIO.output(led, GPIO.LOW)
    
while True:
    if GPIO.input(MOTION_SENSOR):
        boo()
        time.sleep(PAUSE_TIME)
    else:
    	time.sleep(5)
  
GPIO.cleanup()
