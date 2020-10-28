# Modules 
import pygame, sys, random

def ball_animation():
	global ball_speed_x, ball_speed_y
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
	if ball.left <= 0 or ball.right >= screen_width:
		ball_speed_x *= -1


pygame.init()
clock = pygame.time.Clock()

screen_width = 680
screen_height = 460
screen = pygame.display.set_mode((screen_width,screen_height))

ball = pygame.Rect(100, 100, 20, 20)

# Game Variables
ball_speed_x = 7
ball_speed_y = 7

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	# Game logic
	ball_animation()

	pygame.draw.ellipse(screen, pygame.Color("white"), ball)

	pygame.display.flip()
	clock.tick(60)        
