import sys #Para usar exit
import pygame

width, height = 640, 480

#Inicializamos pantalla
screen = pygame.display.set_mode((width, height))

#Título de pantalla
pygame.display.set_caption('Primer juego')

while True:
    #Revisar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    pygame.display.flip()