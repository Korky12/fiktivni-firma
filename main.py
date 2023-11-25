import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fiktivní firma")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.KEYDOWN:
            # Zpracování stisknutí klávesy
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

pygame.quit()