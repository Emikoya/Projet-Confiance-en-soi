import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.mouse.set_visible(False)
pygame.display.set_caption("Photo")

img = pygame.image.load("5.png")
img = pygame.transform.scale(img,(400,300))
rect_img = img.get_rect()
screen.fill((0,0,0))
screen.blit(img,rect_img)
pygame.display.update()