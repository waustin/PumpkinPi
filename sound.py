import pygame

SOUND = "l1.wav"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(SOUND)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
