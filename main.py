import pygame, sys, random

# Global variables 
# The display is a grid with 10px cell size
cellWidth = 20
cellNumber = 30
displayWidth = cellNumber * cellWidth
displayHeight = (cellNumber - 10) * cellWidth

# Color Palette
objectColor = (245, 245, 245)
backgroundColor = (0, 190, 105)
foodColor = (200, 30, 30)

# init all pygame modules 
pygame.init()
frameRates = pygame.time.Clock()
display = pygame.display.set_mode((displayWidth, displayHeight))

# Game font
mainFont = pygame.font.Font("./assets/MinecraftTen-VGORe.ttf", 21)
