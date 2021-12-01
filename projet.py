#import
import pygame
from pygame.locals import *
import time
import random
import sys

#initialisation du cadre
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.mouse.set_visible(False)
pygame.display.set_caption("Photo")

i = 1

#affichage aléatoire
while (True):

    img = pygame.image.load(str(random.randint(1, 20))+".png")
    img = pygame.transform.scale(img, (400, 300))
    rect_img = img.get_rect()
    screen.fill((0, 0, 0))
    screen.blit(img, rect_img)
    pygame.display.update()
    # if i == 20:
    #     i = 1
    # i = i+1
    time.sleep(1)
