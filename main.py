import pygame, sys, random

# init all pygame modules 
pygame.init()
clock = pygame.time.Clock()

# animations and speed
ballSpeedX = random.randint(5, 8)
ballSpeedY = random.randint(1, 4)

playerSpeed = 0
opponentSpeed = 0

# score
playerScore = 0
opponentScore = 0

# game font
gameFont = pygame.font.Font("freesansbold.ttf", 25)

# ball function
def ballAnimate():
    global ballSpeedX, ballSpeedY, opponentScore, playerScore

    # moving the ball
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # display ball borders
    if ball.top <= 0 or ball.bottom >= screenWidthY:
        ballSpeedY *= -1
    if ball.left <= 0:
        resetBall()
        playerScore += 1
    elif ball.right >= screenWidthX:
        resetBall()
        opponentScore += 1


    # ball collision with objects
    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeedX *= -1

def playerAnimation():
    player.y += playerSpeed
    if player.top <= 0: 
        player.top = 0
    if player.bottom >= screenWidthY:
        player.bottom = screenWidthY

def opponentAnimation():
    opponent.y += opponentSpeed
    if opponent.top <= 0: 
        opponent.top = 0
    if opponent .bottom >= screenWidthY:
        opponent.bottom = screenWidthY

def resetBall():
        global ballSpeedX, ballSpeedY
        ball.center = (screenWidthX/2, screenWidthY/2)
        ballSpeedX *= random.choice((1, -1))
        ballSpeedY *= random.choice((1, -1))
    
# game title and logo
pygame.display.set_caption("Ping Pong")
pygame.display.set_icon(pygame.image.load("./assets/favicon.png"))

# screen dimensions
screenWidthX = 700
screenWidthY = 400
screen = pygame.display.set_mode((screenWidthX, screenWidthY))

# color palette
backgroundColor = (30, 30, 30) # dark grey
objectColor = (210, 210, 210) # light grey

# game objects
ball = pygame.Rect(screenWidthX/2 - 10, screenWidthY/2 - 10, 20, 20)
player = pygame.Rect(screenWidthX - 16, screenWidthY/2 - 40, 8, 80)
opponent = pygame.Rect(8, screenWidthY/2 - 40, 8, 80)

# the main game loop
while True:
    # pygame display events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 5
            if event.key == pygame.K_UP:
                playerSpeed -= 5 
            if event.key == pygame.K_a:
                opponentSpeed += 5
            if event.key == pygame.K_q:
                opponentSpeed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 5
            if event.key == pygame.K_UP:
                playerSpeed += 5
            if event.key == pygame.K_a:
                opponentSpeed -= 5
            if event.key == pygame.K_q:
                opponentSpeed += 5
  
    ballAnimate()
    playerAnimation()
    opponentAnimation()

    #drawing 
    screen.fill(backgroundColor)
    pygame.draw.rect(screen, objectColor, player)
    pygame.draw.rect(screen, objectColor, opponent)
    pygame.draw.ellipse(screen, objectColor, ball)
    pygame.draw.aaline(screen, objectColor, (screenWidthX/2, 0), (screenWidthX/2, screenWidthY))

    playerText = gameFont.render(f"{playerScore}", False, objectColor)
    opponentText = gameFont.render(f"{opponentScore}", False, objectColor)
    screen.blit(playerText, (screenWidthX/2 + 25, 10))
    screen.blit(opponentText, (screenWidthX/2 - 45, 10))


    # updating the display window
    clock.tick(60)
    pygame.display.flip()
