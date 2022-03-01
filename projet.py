# PROJET "CONFIANCE"
#
# GROUPE :
# AMA Aymerick
# ANCELE Corentin
# DUTAS Louis
# PRUVOST Elisa
#
#
# #

# ~~~~IMPORT~~~~
import os
import pygame
from pygame.locals import *
import time
import random
import sys

# ~~~~FUNCTION~~~~


def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    for alpha in range(0, 200, 1):  # Change 1 to modifie the speed of fade (4 or 5)
        fade.set_alpha(alpha)
        redrawWindow()
        screen.blit(img, (0, 0))    # Image in "background"
        screen.blit(fade, (0, 0))   # Fade image
        pygame.display.update()     # update screen
        pygame.time.delay(5)


def redrawWindow():
    screen.fill((255, 255, 255))


def lastImageNumber():
    last = 0
    dir = "./img"
    for path in os.listdir(dir):
        last = last + 1
    return last


# ~~~~MAIN~~~~
pygame.init()
screen = pygame.display.set_mode((800, 480))  # , FULLSCREEN
pygame.mouse.set_visible(False)
pygame.display.set_caption("Confiance")

lastNumber = lastImageNumber()

image = random.randint(1, lastNumber)

while (True):

    # img = pygame.image.load(".\img\\"+str(image)+".png")    # For windows user
    img = pygame.image.load("./img//"+str(image)+".png")  # For Linux user
    img = pygame.transform.scale(img, (800, 480))

    fade(1000, 800)

    diff = True
    while (diff):
        verifImage = image
        image = random.randint(1, lastNumber)
        if verifImage != image:
            diff = False
