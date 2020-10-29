# Modules 
import pygame, sys, random
from pygame.math import Vector2 

# Global variables 
# The display is a grid with 10px cell size
cellWidth = 30
cellNumber = 15
displayWidth = cellNumber * cellWidth
displayHeight = cellNumber * cellWidth

# Color Palette
foodColor = (200, 63, 10)
snakeColor = (19, 53, 250)
backgroundColor = (84, 197, 74)

# Uploading assets
