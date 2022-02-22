import cv2 as cv
import numpy as np
import time

# import pygame
# from pygame.locals import *
# import time
import random
# import sys

# pygame.init()
# screen = pygame.display.set_mode((400, 300))  # , FULLSCREEN
# pygame.mouse.set_visible(False)
# pygame.display.set_caption("Confiance")

image = random.randint(1, 20)

# while (True):

#     img = pygame.image.load(".\img\\"+str(image)+".png")
#     img = pygame.transform.scale(img, (400, 300))

#     rect_img = img.get_rect()
#     screen.fill((0, 0, 0))
#     screen.blit(img, rect_img)
#     pygame.display.update()

#     # start = time.time()
#     # finish = start+4
#     # while time.time() < finish:
#     #     pass
#     time.sleep(1)

#     diff = True
#     while (diff):
#         verifImage = image
#         image = random.randint(1, 20)
#         if verifImage != image:
#             diff = False

while True:
    img1 = cv.imread(".\img\\"+str(image)+".png")
    image = random.randint(1, 20)
    img2 = cv.imread(".\img\\"+str(image)+".png")
    for i in np.linspace(0, 1, 100):
        alpha = i
        beta = 1 - alpha
        output = cv.addWeighted(img1, alpha, img2, beta, 0)
        cv.imshow('Transition Effect ', output)
        time.sleep(0.02)
        if cv.waitKey(1) == 27:
            break
    cv.destroyAllWindow()
