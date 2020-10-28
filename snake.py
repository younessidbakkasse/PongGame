from globals import *

class Snake:
    def __init__(self):
        self.snakeBody = [Vector2(4, 10), Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
    
    def draw(self):
        for part in self.snakeBody:
            bodyRect = pygame.Rect(int(part.x * cellWidth), int(part.y * cellWidth), cellWidth, cellWidth)
            pygame.draw.rect(displaySurface, snakeColor, bodyRect) 

    def move(self):
        newSnakeBody = self.snakeBody[:-1]
        newSnakeBody.insert(0, self.snakeBody[0] + self.direction)
        self.snakeBody = newSnakeBody[:]

class Food:
    def __init__(self):
        self.x = random.randint(0, 29)
        self.y = random.randint(0, 19)
        self.pos = pygame.Vector2(self.x, self.y)
    
    def draw(self):
        foodRect = pygame.Rect(int(self.pos.x * cellWidth), int(self.pos.y * cellWidth), cellWidth, cellWidth)
        pygame.draw.rect(displaySurface, foodColor, foodRect)


# Creating game objects
food = Food()
snake = Snake()

# Initialising pygame modules
pygame.init()
frameRates = pygame.time.Clock()

# Creating the display object
displaySurface = pygame.display.set_mode((displayWidth, displayHeight))
displaySurface.fill(backgroundColor)
pygame.display.set_caption("Snake Game")

# Time event
timeEvent = pygame.USEREVENT
pygame.time.set_timer(timeEvent, 100)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == timeEvent:
            snake.move()
    
    food.pos.x += 0.1
    food.draw()
    snake.draw()
    pygame.display.update()
    frameRates.tick(60)
