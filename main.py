import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fiktivní firma")

FPS = 60

DARK_BLUE = (52, 90, 115)

def draw_window():
    screen.fill(DARK_BLUE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            elif event.type == pygame.KEYDOWN:
                # Zpracování stisknutí klávesy
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        draw_window()
    
    
    pygame.quit()

if __name__ == "__main__":
    main()