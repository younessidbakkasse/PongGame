import pygame, sys, random
from main import * 

class Player:
    def __init__(self, posX, speed, score):
        self.rect = pygame.Rect(int(posX), int(displayHeight/2 - 40), 14, 80)
        self.speed = speed
        self.score = score

    def collisions(self):
        self.mouvement()
        if self.rect.top <= 0: 
            self.rect.top = 0
        if self.rect.bottom >= displayHeight:
            self.rect.bottom = displayHeight

    def mouvement(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(display, objectColor, self.rect)

class Ball:
    def __init__(self, speedX, speedY):
        self.rect = pygame.Rect(int(displayWidth/2 - 8), int(displayHeight/2 - 8), 16, 16)
        self.speedX = speedX
        self.speedY = speedY

    def reset(self):
        self.speedX, self.speedY = 0, 0
        self.rect.center = (int(displayWidth/2), int(displayHeight/2))

    def draw(self):
        pygame.draw.rect(display, objectColor, self.rect)

    def mouvement(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY

class Game:
    # Creating game objects : Three object --------------------------------------#
    def __init__(self):
        self.player = Player(displayWidth - 22, 0, 0)
        self.opponent = Player(8, 0, 0)
        self.ball = Ball(random.randint(-6, 6), random.randint(-4, 4))

    def collisions(self):
        self.ball.mouvement()
        self.lunch()
        # Ball collisions with borders -------------------------------------------#
        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= displayHeight:
            self.ball.speedY *= -1

        if self.ball.rect.left <= 0:
            self.player.score += 1
            self.ball.reset()

        elif self.ball.rect.right >= displayWidth:
            self.opponent.score += 1
            self.ball.reset()

         # Ball collisions with borders -------------------------------------------#
        if self.ball.rect.colliderect(self.player.rect) and self.ball.speedX > 0:
            self.ball.speedX *= -1.05
            if abs(self.ball.rect.bottom - self.player.rect.top) < 5 and self.ball.speedY > 0:
                self.ball.speedY *= -1.05
            elif abs(self.ball.rect.top - self.player.rect.bottom) < 5 and self.ball.speedY < 0:
                self.ball.speedY *= -1.05

        if self.ball.rect.colliderect(self.opponent.rect) and self.ball.speedX < 0:
            self.ball.speedX *= -1.05
            if abs(self.ball.rect.bottom - self.opponent.rect.top) < 5 and self.ball.speedY > 0:
                self.ball.speedY *= -1.05
            elif abs(self.ball.rect.top - self.opponent.rect.bottom) < 5 and self.ball.speedY < 0:
                self.ball.speedY *= -1.05

    def constraints(self):
        self.player.collisions()
        self.opponent.collisions()
        self.collisions()

    def score(self):
        playerScore = mainFont.render(f"{self.player.score}", False, objectColor)
        opponentScore = mainFont.render(f"{self.opponent.score}", False, objectColor)
        display.blit(playerScore, (displayWidth/2 + 25, 10))
        display.blit(opponentScore, (displayWidth/2 - 35, 10))

    def draw(self):
        display.fill(backgroundColor)
        pygame.draw.line(display, objectColor, (int(displayWidth/2), 0), (int(displayWidth/2), displayHeight), 5)
        self.player.draw()
        self.opponent.draw()
        self.ball.draw()
        self.score()

    def lunch(self):
        if (self.player.speed != 0 or self.opponent.speed != 0) and (self.ball.speedX == 0 and self.ball.speedY == 0):
            self.ball.speedX = random.randint(2, 5) 
            self.ball.speedY = random.randint(1, 4)

    def run(self):
        self.constraints()
        self.draw()

# Naming the game
pygame.display.set_caption("Pong Game")

# creating the game
game = Game()

# Pong game Main loop
while True:
    # pygame display controle events ------------------------------------------# 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                game.player.speed += 5
            if event.key == pygame.K_UP:
                game.player.speed -= 5 
            if event.key == pygame.K_a:
                game.opponent.speed += 5
            if event.key == pygame.K_q:
                game.opponent.speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                game.player.speed -= 5
            if event.key == pygame.K_UP:
                game.player.speed += 5
            if event.key == pygame.K_a:
                game.opponent.speed -= 5
            if event.key == pygame.K_q:
                game.opponent.speed += 5

    # updating the display window
    game.run()
    frameRates.tick(60)
    pygame.display.flip()