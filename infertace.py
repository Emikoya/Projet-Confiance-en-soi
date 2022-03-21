import pygame
from pygame.locals import *

import sys 
  
pygame.init() 

def creabouton(posx, posy, tx, ty, color_light, color_dark, text):
    while True: 
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                pygame.quit() 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                #Condition sur la position de la souris 
                if posx <= mouse[0] <= posx+tx and posy <= mouse[1] <= posy+ty: 
                    pygame.quit()
        # Couleur de fond
        screen.fill((208,243,188)) 
        #Condition sur la position de la souris 
        mouse = pygame.mouse.get_pos() 
        if posx <= mouse[0] <= posx+tx and posy <= mouse[1] <= posy+ty: 
            pygame.draw.rect(screen,color_light,[posx,posy,tx,ty]) 
        else: 
            pygame.draw.rect(screen,color_dark,[posx,posy,tx,ty]) 
        # Position du texte
        screen.blit(text , (posx*3.2,posy*1.8)) 
        pygame.display.update()

# Création de l'écran
res = (800,480) 
screen = pygame.display.set_mode(res)  

width = screen.get_width() 
height = screen.get_height() 



##############
## BOUTON 1 ##
##############

#Coordonnée bouton + taille
posx = 50
posy = 140
tx = width/2.5
ty = width/3
#Couleur et police du texte pour les boutons
color_text = (255,255,255) 
font = pygame.font.SysFont('Corbel',35) 
text = font.render('Sourire' , True , color_text) 
# Couleurs du bouton changeantes
color_light = (255,183,183) 
color_dark = (217,104,104)

creabouton(posx, posy, tx, ty, color_light, color_dark, text)

#Coordonnée bouton + taille
posx = 140
posy = 200
tx = width/2.5
ty = width/3
#Couleur et police du texte pour les boutons
color_text = (255,255,255) 
font = pygame.font.SysFont('Corbel',35) 
text = font.render('Sourire' , True , color_text) 
# Couleurs du bouton changeantes
color_light = (255,183,183) 
color_dark = (217,104,104)

creabouton(posx, posy, tx, ty, color_light, color_dark, text)