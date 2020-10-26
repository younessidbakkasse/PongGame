from pygame import *
from sys import exit


class gameObject():
    def __init__(self, posX, posY, widthX, widthY):
        Rect(posX, posY, widthX, widthY)

class Player(gameObject):
    def __init__(self, posX, posY, widthX, widthY, speed)
        super().__init__(posX, posY, widthX, widthY)

    def screenConstraints():
        if self.top <= 0: 
            player.top = 0
        if self.bottom >= screenWidthY:
            self.bottom = screenWidthY
        
    def mouvement():
        self.posY += self.speed
        screenConstraints()

class Ball(gameObject):
    def __init__(self, posX, posY, widthX, widthY, speedX, speedY)
        super().__init__(posX, posY, widthX, widthY)

    def reset(self):
        self.speedX, self.speedY = 0, 0
        self.center = (screenWidthX/2, screenWidthY/2)

    def constraints(self):
        if self.top <= 0 or self.bottom >= screenWidthY:
            self.speedY *= -1

        if ball.left <= 0:
            playerScore += 1
            resetBall()

        if ball.right >= screenWidthX:
            opponentScore += 1
            resetBall()

    

# global variables
screenWidthX = 700
screenWidthY = 400

# generals
screen = display.set_mode((screenWidthX, screenWidthY))

# color palette
backgroundColor = (0, 190, 105) 
objectColor = (250, 250, 250)