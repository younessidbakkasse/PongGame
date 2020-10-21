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
playerX = screenWidthX/2
playerY = screenWidthY/2
radius = 10
playerSpeedX = 0
playerSpeedY = -1

Clock = pygame.time.Clock()

def player(x, y, r):
    pygame.draw.circle(screen, orange, (int(x), int(y)), r)

# the main game loop
while True:
    # maintain the game screen open
    screen = pygame.display.set_mode((screenWidthX, screenWidthY))
    
    # pygame display events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerSpeedX = -1
            elif event.key == pygame.K_RIGHT:
                playerSpeedX = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerSpeedX = 0

    playerX += playerSpeedX
    Clock.tick(60)
    player(playerX, playerY, radius)
    pygame.display.update()
