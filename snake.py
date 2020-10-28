import pygame, sys, random
from pygame.math import Vector2

# General variables who need a seperate file 
# Colors 
foodColor = (200, 63, 10)
snakeColor = (19, 53, 250)
backgroundColor = (84, 197, 74)

class Snake:
    def __init__(self):
        self.body = [Vector2(4, 10), Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
    
    def draw(self):
        for part in self.body:
            bodyRect = pygame.Rect(int(part.x * cellWidth), int(part.y * cellWidth), cellWidth, cellWidth)
            pygame.draw.rect(displaySurface, snakeColor, bodyRect) 

class Food:
    def __init__(self):
        self.x = random.randint(0, 29)
        self.y = random.randint(0, 19)
        self.pos = pygame.Vector2(self.x, self.y)
    
    def draw(self):
        foodRect = pygame.Rect(int(self.pos.x * cellWidth), int(self.pos.y * cellWidth), cellWidth, cellWidth)
        pygame.draw.rect(displaySurface, foodColor, foodRect)

food = Food()
snake = Snake()

# Initialising pygame modules
pygame.init()
frameRates = pygame.time.Clock()

# Global variables 
# The display is a grid with 10px cell size
cellWidth = 20
displayWidth = 30 * cellWidth
displayHeight = 20 * cellWidth

# Creating the display object
displaySurface = pygame.display.set_mode((displayWidth, displayHeight))
displaySurface.fill(backgroundColor)
pygame.display.set_caption("Snake Game")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    food.draw()
    snake.draw()
    pygame.display.update()
    frameRates.tick(60)
