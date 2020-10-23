class Player:
    width = 0
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        
    def getPosition(self):
        print("the position of the snake is : " + "x = " + str(self.posX) + " and " + "y = " + str(self.posY))

    
snakeOne = Player(14, 209)
snakeTwo = Player(109, 10)

snakeOne.getPosition()
snakeTwo.getPosition()
