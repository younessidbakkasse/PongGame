import pygame, sys

# init all pygame modules 
pygame.init()

# game title and logo
pygame.display.set_caption("Snaky")
pygame.display.set_icon(pygame.image.load("./assets/favicon.png"))

# screen dimensions
screenWidthX = 250
screenWidthY = 540
orange = pygame.Color(255, 127, 80)

# Player coords
playerX = 50
playerY = 10
radius = 10

Clock = pygame.time.Clock()

def player(x, y, r):
    pygame.draw.circle(screen, orange, (x, y), r)

# the main game loop
while True:
    # maintain the game screen open
    screen = pygame.display.set_mode((screenWidthX, screenWidthY))
    
    # closing the pygame display event 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    playerX += 1
    Clock.tick(60)
    player(playerX, playerY, radius)
    pygame.display.update()
