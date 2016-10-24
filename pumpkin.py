import RPi.GPIO as GPIO
import time
import pygame

GREEN_LED_1 = 25
GREEN_LED_2 = 24
RED_LED = 23

MOTION_SENSOR = 21

H3_SOUND_FILE = "halloween-3-short.mp3"



# BLINK MULTIPLE LEDS
def blink_led(led_pins=[]):
    for led_pin in led_pins:
        GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.25)

    for led_pin in led_pins:
        GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.25)


# SCARE ACTION
def boo():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        blink_led([GREEN_LED_1, GREEN_LED_2])
        blink_led([RED_LED])
    
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
pygame.mixer.music.load(H3_SOUND_FILE)

# TURN OFF LEDS 
for led in [GREEN_LED_1, GREEN_LED_2, RED_LED]:
    GPIO.output(led, GPIO.LOW)
    
while True:
    if GPIO.input(MOTION_SENSOR):
        boo()
        time.sleep(3)
    time.sleep(0.5)
  
GPIO.cleanup()
