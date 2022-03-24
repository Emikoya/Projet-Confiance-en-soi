# PROJET "CONFIANCE"
#
# GROUPE :
# AMA Aymerick
# ANCELE Corentin
# DUTAS Louis
# PRUVOST Elisa
#


# ~~~~IMPORT~~~~
import os
import pygame
from pygame.locals import *
import random


# ~~~~FUNCTION~~~~
def fade(width, height, img):
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


def affichage():
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

        fade(1000, 800, img)

        diff = True
        while (diff):
            verifImage = image
            image = random.randint(1, lastNumber)
            if verifImage != image:
                diff = False


def mainMenu():
    pygame.init()
    # Fonction creabouton : permet de créer un bouton et son texte selon ces paramètres :
    # posx = position en abscisse du bouton
    # posy = position en ordonnée du bouton
    # tx = longueur du bouton
    # ty = largeur du bouton
    # color = couleur du bouton
    # text = le texte accompagnant le bouton

    def creabouton(posx, posy, tx, ty, color, text):
        # Création du bouton
        pygame.draw.rect(screen, color, [posx, posy, tx, ty])
        # Position du texte
        screen.blit(text, (posx+110, posy*1.8))

    # Création de l'écran
    res = (800, 480)
    screen = pygame.display.set_mode(res)
    width = screen.get_width()
    # Couleur de fond
    screen.fill((208, 243, 188))

    # Texte de bienvenue
    color_text = (0, 0, 0)
    font = pygame.font.SysFont('Corbel', 50)
    text = font.render('Bonjour !', True, color_text)
    screen.blit(text, (320, 20))
    font = pygame.font.SysFont('Corbel', 35)
    text = font.render("Que voulez-vous faire aujourd'hui?", True, color_text)
    screen.blit(text, (180, 80))

    # taille des boutons
    tx = width/2.5
    ty = width/3

    ##############
    ## BOUTON 1 ##
    ##############
    # Couleur et police du texte pour les boutons
    color_text = (255, 255, 255)
    text = font.render('Sourire', True, color_text)
    # Création du bouton
    creabouton(50, 140, tx, ty, (217, 104, 104), text)

    ##############
    ## BOUTON 2 ##
    ##############
    # Couleur et police du texte pour les boutons
    color_text = (255, 255, 255)
    text = font.render('Créer', True, color_text)
    # Création du bouton
    creabouton(430, 140, tx, ty, (94, 176, 72), text)

    pygame.display.update()

    # Boucle permettant d'obtenir la position de la souris en temps réel
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Condition sur la position de la souris
                if 50 <= mouse[0] <= 50+tx and 140 <= mouse[1] <= 140+ty:
                    affichage()
                elif 430 <= mouse[0] <= 430+tx and 140 <= mouse[1] <= 140+ty:
                    print("au revoir.")
                    pygame.quit()


# ~~~~MAIN~~~~
screen = pygame.display.set_mode((800, 480))
mainMenu()
