import pygame, sys

# init all pygame modules 
pygame.init()
clock = pygame.time.Clock()

# game title and logo
pygame.display.set_caption("Ping Pong")
pygame.display.set_icon(pygame.image.load("./assets/favicon.png"))

# screen dimensions
screenWidthX = 700
screenWidthY = 400

# color palette
backgroundColor = (30, 30, 30) # dark grey
objectColor = (210, 210, 210) # light grey

# game objects
ball = pygame.Rect(screenWidthX/2 - 10, screenWidthY/2 - 10, 20, 20)
player = pygame.Rect(screenWidthX - 16, screenWidthY/2 - 40, 8, 80)
opponent = pygame.Rect(8, screenWidthY/2 - 40, 8, 80)

# the main game loop
while True:
    # maintain the game screen open
    screen = pygame.display.set_mode((screenWidthX, screenWidthY))
    
    # pygame display events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Game ended by user")
            sys.exit()
    #drawing 
    screen.fill(backgroundColor)
    pygame.draw.rect(screen, objectColor, player)
    pygame.draw.rect(screen, objectColor, opponent)
    pygame.draw.ellipse(screen, objectColor, ball)
    pygame.draw.aaline(screen, objectColor, (screenWidthX/2, 0), (screenWidthX/2, screenWidthY))

    # updating the display window
    clock.tick(60)
    pygame.display.flip()
