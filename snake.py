from globals import *

class Snake:
    def __init__(self):
        self.snakeBody = [Vector2(5, 10), Vector2(4,10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.newBodyPart = False

        # Head images
        self.head = None
        self.headUp = pygame.image.load("./assets/headUp.png")
        self.headDown = pygame.image.load("./assets/headDown.png")
        self.headRight = pygame.image.load("./assets/headRight.png")
        self.headLeft = pygame.image.load("./assets/headLeft.png")

        # Tail images
        self.tail = None
        self.tailUp = pygame.image.load("./assets/tailUp.png")
        self.tailDown = pygame.image.load("./assets/tailDown.png")
        self.tailRight = pygame.image.load("./assets/tailRight.png")
        self.tailLeft = pygame.image.load("./assets/tailLeft.png")

        # Turning body images
        self.upRight = pygame.image.load("./assets/upRight.png")
        self.upLeft = pygame.image.load("./assets/upLeft.png")
        self.downRight = pygame.image.load("./assets/downRight.png")
        self.downLeft = pygame.image.load("./assets/downLeft.png")

        # Body
        self.bodyHorizontal = pygame.image.load("./assets/bodyHorizontal.png")
        self.bodyVertical = pygame.image.load("./assets/bodyVertical.png")
    
    def draw(self):
        self.updateHead()
        self.updateTail()
        for index, part in enumerate(self.snakeBody):
            bodyRect = pygame.Rect(int(part.x * cellWidth), int(part.y * cellWidth), cellWidth, cellWidth)

            if index == 0:
                displaySurface.blit(self.head, bodyRect)
            elif index == (len(self.snakeBody) - 1):
                displaySurface.blit(self.tail, bodyRect)
            else:
                previousPart = self.snakeBody[index + 1] - part
                nextPart = self.snakeBody[index - 1] - part
                if previousPart.x == nextPart.x:
                    displaySurface.blit(self.bodyVertical, bodyRect)
                elif previousPart.y == nextPart.y:
                    displaySurface.blit(self.bodyHorizontal, bodyRect)
                else:
                    if previousPart.x == -1 and nextPart.y == -1 or previousPart.y == -1 and nextPart.x == -1:
                        displaySurface.blit(self.downLeft, bodyRect)
                    elif previousPart.x == 1 and nextPart.y == 1 or previousPart.y == 1 and nextPart.x == 1:
                        displaySurface.blit(self.upRight, bodyRect)
                    elif previousPart.x == 1 and nextPart.y == -1 or previousPart.y == -1 and nextPart.x == 1:
                        displaySurface.blit(self.downRight, bodyRect)
                    elif previousPart.x == -1 and nextPart.y == 1 or previousPart.y == 1 and nextPart.x == -1:
                        displaySurface.blit(self.upLeft, bodyRect)

    def updateHead(self):
        headToBody = self.snakeBody[1] - self.snakeBody[0] 
        if headToBody == Vector2(1, 0):
            self.head = self.headLeft
        elif headToBody == Vector2(-1, 0):
            self.head = self.headRight
        elif headToBody == Vector2(0, 1):
            self.head = self.headUp
        elif headToBody == Vector2(0, -1):
            self.head = self.headDown

    def updateTail(self):
        tailToBody = self.snakeBody[len(self.snakeBody) - 2] - self.snakeBody[len(self.snakeBody) - 1]
        if tailToBody == Vector2(1, 0):
            self.tail = self.tailLeft
        elif tailToBody == Vector2(-1, 0):
            self.tail = self.tailRight
        elif tailToBody == Vector2(0, 1):
            self.tail = self.tailUp
        elif tailToBody == Vector2(0, -1):
            self.tail = self.tailDown

    def move(self):
        if self.newBodyPart == True:
            newSnakeBody = self.snakeBody[:]
            newSnakeBody.insert(0, self.snakeBody[0] + self.direction)
            self.snakeBody = newSnakeBody[:]
            self.newBodyPart = False
        else:
            newSnakeBody = self.snakeBody[:-1]
            newSnakeBody.insert(0, self.snakeBody[0] + self.direction)
            self.snakeBody = newSnakeBody[:]

    def isGrowing(self):
        self.newBodyPart = True

class Food:
    def __init__(self):
        self.randomize()
        self.apple = pygame.image.load("./assets/apple.png")

    def draw(self):
        foodRect = pygame.Rect(int(self.pos.x * cellWidth), int(self.pos.y * cellWidth), cellWidth, cellWidth)
        displaySurface.blit(self.apple, foodRect)

    def randomize(self):
        self.x = random.randint(0, cellNumber - 1)
        self.y = random.randint(0, cellNumber - 1)
        self.pos = pygame.Vector2(self.x, self.y)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
    
    def isCollide(self):
        if self.food.pos == self.snake.snakeBody[0]:
            self.food.randomize()
            self.snake.isGrowing()

    def update(self):
        self.snake.move()
        self.isCollide()
        self.isOutside()
        self.isEatenSelf()

    def draw(self):
        self.drawBackgroundPattern()
        self.food.draw()
        self.snake.draw()

    def isOutside(self):
        if not 0 <= self.snake.snakeBody[0].x < cellNumber or not 0 <= self.snake.snakeBody[0].y < cellNumber: 
            self.gameOver()
    
    def isEatenSelf(self):
        for part in self.snake.snakeBody[1:]:
            if part == self.snake.snakeBody[0]:
                self.gameOver()

    def gameOver(self):
        pygame.quit()
        sys.exit()

    def drawBackgroundPattern(self):
        displaySurface.fill(darkBackgroundColor)
        for row in range(cellNumber):
            if row % 2 == 0:
                for col in range(cellNumber):
                    if col % 2 == 0:
                        lightGrassBlock = pygame.Rect(col * cellWidth, row * cellWidth, cellWidth, cellWidth)
                        pygame.draw.rect(displaySurface, lightBackgroundColor, lightGrassBlock)
            if row % 2 != 0:
                for col in range(cellNumber):
                    if col % 2 != 0:
                        lightGrassBlock = pygame.Rect(col * cellWidth, row * cellWidth, cellWidth, cellWidth)
                        pygame.draw.rect(displaySurface, lightBackgroundColor, lightGrassBlock)



# Initialising pygame modules
pygame.init()
frameRates = pygame.time.Clock()
game = Game()



# Creating the display object
displaySurface = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Snake Game")

# Time event
timeEvent = pygame.USEREVENT
pygame.time.set_timer(timeEvent, 100)

# Main game loop
while True:
    # Game control and user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == timeEvent:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)  
    
    # Display updating the game
    game.draw()
    pygame.display.flip()
    frameRates.tick(60)
