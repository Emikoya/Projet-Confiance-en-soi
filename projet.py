import pygame
from pygame.locals import *
import time
import random
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))  # , FULLSCREEN
pygame.mouse.set_visible(False)
pygame.display.set_caption("Confiance")

image = random.randint(1, 20)

while (True):

    img = pygame.image.load(".\img\\"+str(image)+".png")
    img = pygame.transform.scale(img, (400, 300))

    rect_img = img.get_rect()
    screen.fill((0, 0, 0))
    screen.blit(img, rect_img)
    pygame.display.update()

    # start = time.time()
    # finish = start+4
    # while time.time() < finish:
    #     pass
    time.sleep(1)

    diff = True
    while (diff):
        verifImage = image
        image = random.randint(1, 20)
        if verifImage != image:
            image = random.randint(1, 20)
        else:
            diff = False
