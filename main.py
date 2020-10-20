import pygame, sys

# init all pygame modules 
pygame.init()

# game title and logo
pygame.display.set_caption("Snaky")
pygame.display.set_icon(pygame.image.load("./assets/favicon.png"))

# screen dimensions
screenWidthX = 400
screenWidthY = 400

# the main game loop
while True:
    screen = pygame.display.set_mode((screenWidthX, screenWidthY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
