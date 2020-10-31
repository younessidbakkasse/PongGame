import pygame, sys, random

# init all pygame modules 
pygame.init()
clock = pygame.time.Clock()

def rand(min, max):
    return random.randint(min, max) * random.choice((1, -1))

playerSpeed = 0
opponentSpeed = 0

# score
playerScore = 0
opponentScore = 0

# game font
gameFont = pygame.font.Font("./assets/MinecraftTen-VGORe.ttf", 25)

# animations and speed
ballSpeedX = rand(3, 6)
ballSpeedY = rand(2, 4)

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
        playerScore += 1
        resetBall()

    elif ball.right >= screenWidthX:
        opponentScore += 1
        resetBall()

    # ball collision with objects
    if ball.colliderect(player) and ballSpeedX > 0:
        ballSpeedX *= -1.05
        if abs(ball.bottom - player.top) < 5 and ballSpeedY > 0:
            ballSpeedY *= -1.05
        elif abs(ball.top - player.bottom) < 5 and ballSpeedY < 0:
            ballSpeedY *= -1.05

    if ball.colliderect(opponent) and ballSpeedX < 0:
        ballSpeedX *= -1.05
        if abs(ball.bottom - opponent.top) < 5 and ballSpeedY > 0:
            ballSpeedY *= -1.05
        elif abs(ball.top - opponent.bottom) < 5 and ballSpeedY < 0:
            ballSpeedY *= -1.05

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
    ballSpeedX, ballSpeedY = 0, 0
    ball.center = (screenWidthX/2, screenWidthY/2)

# game title and logo
pygame.display.set_caption("Ping Pong")

# screen dimensions
screenWidthX = 700
screenWidthY = 400
screen = pygame.display.set_mode((screenWidthX, screenWidthY))

# color palette
backgroundColor = (0, 190, 105)
objectColor = (250, 250, 250) 

# game objects
# the rect pos (x, y) is defined by top-left corner coords (x, y)
ball = pygame.Rect(screenWidthX/2 - 7, screenWidthY/2 - 7, 14, 14)
player = pygame.Rect(screenWidthX - 20, screenWidthY/2 - 40, 14, 80)
opponent = pygame.Rect(8, screenWidthY/2 - 40, 14, 80)

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
    pygame.draw.rect(screen, objectColor, ball)
    pygame.draw.line(screen, objectColor, (screenWidthX/2, 0), (screenWidthX/2, screenWidthY), 5)

    playerText = gameFont.render(f"{playerScore}", False, objectColor)
    opponentText = gameFont.render(f"{opponentScore}", False, objectColor)
    screen.blit(playerText, (screenWidthX/2 + 25, 10))
    screen.blit(opponentText, (screenWidthX/2 - 35, 10))

    #waiting to lunch the ball
    if (playerSpeed != 0 or opponentSpeed != 0) and (ballSpeedX == 0 and ballSpeedY == 0):
            ballSpeedX = rand(2, 5) 
            ballSpeedY = rand(1, 4)

    # updating the display window
    clock.tick(60)
    pygame.display.flip()