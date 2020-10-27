from pygame import *
from random import *
from sys import exit

class gameObject:
    def __init__(self, posX, posY, widthX, widthY):
        self.obj = Rect(posX, posY, widthX, widthY)

class Player(gameObject):
    def __init__(self, posX, posY, widthX, widthY, speedChange):
        super().__init__(posX, posY, widthX, widthY)
        self.speed = 0
        self.speedChange = speedChange

    def screenConstraints():
        if self.obj.top <= 0: 
            self.obj.top = 0
        if self.obj.bottom >= screenWidthY:
            self.obj.bottom = screenWidthY
        
    def mouvement():
        self.obj.y += self.speed
        screenConstraints()

class Ball(gameObject):
    def __init__(self, posX, posY, widthX, widthY, speedX, speedY)
        super().__init__(posX, posY, widthX, widthY)
        self.speedX = speedX * choice((-1,1))
        self.speedY = speedY * choice((-1,1))

    def reset(self):
        self.speedX, self.speedY = 0, 0
        self.obj.center = (screenWidthX/2, screenWidthY/2)

    def constraints(self):
        if self.obj.top <= 0 or self.obj.bottom >= screenWidthY:
            self.speedY *= -1

        if self.obj.x <= 0 or self.obj.x >= screenWidthX:
            reset()

    def collisions(self, playerOne, playerTwo):
       if self.obj.colliderect(playerOne) and self.speedX > 0:
            self.speedX *= -1.05

        if self.obj.colliderect(playerTwo) and self.speedX < 0:
            self.speedX *= -1.05

    def mouvement(self, playerOne, playerTwo):
        self.obj.x += self.speedX
        self.obj.y += self.speedY
        constraints()
        collisions(playerOne, playerTwo)

class Game:
    def __init__(self, playerOne, playerTwo, ball):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.ball= ball

    def drawObjects(self):
        draw.rect(gameFrame, objectColor, self.playerOne)
        draw.rect(gameFrame, objectColor, self.playerTwo)
        draw.rect(gameFrame, objectColor, self.ball)

    def run():
        self.playerOne.mouvement()
        self.playerTwo.mouvement()
        self.ball.mouvement(self.playerOne, self.playerTwo)
        drawObjects()


# module init
init()
frameRates = time.Clock()

# global variables
screenWidthX = 700
screenWidthY = 400

# generals
gameFrame = display.set_mode((screenWidthX, screenWidthY))
display.set_caption('Pong')

# color palette
backgroundColor = (0, 190, 105) 
objectColor = (250, 250, 250)

# game objects
playerOne = player()
playerTwo = player()
ball = Ball()
game = Game()

# main game loop
while True:
    for event in event.get():
        if event.type == QUIT:
            quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                playerOne.speed += playerOne.speedChange
            if event.key == K_UP:
                playerOne.speed -= playerOne.speedChange
            if event.key == K_a:
                playerTwo.speed += playerTwo.speedChange
            if event.key == K_q:
                playeTwo.speed -= playerTwo.speedChange
        if event.type == KEYUP:
            if event.key == K_DOWN:
                playerOne.speed -= playerOne.speedChange
            if event.key == K_UP:
                playerOne.speed += playerOne.speedChange
            if event.key == K_a:
                playerTwo.speed -= playerTwo.speedChange
            if event.key == K_q:
                playerTwo.speed += playerTwo.speedChange

    # Background Stuff
	gameFrame.fill(backgroundColor)
	draw.line(gameFrame,)

    # Game Running
    game.run()

    # update game screen
    display.flip()
    frameRates.tick(60)