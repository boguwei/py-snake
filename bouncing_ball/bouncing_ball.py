# bouncing ball
# 
# author: boguwei@gmail.com
# date:   3/26/16

import sys
import pygame

pygame.init()

width = 800
height = 600
size = width, height

speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
ball = pygame.image.load('ball.gif').convert()
ballRect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    ballRect = ballRect.move(speed)
    if ballRect.left < 0 or ballRect.right > width:
        speed[0] = -speed[0]
    if ballRect.top < 0 or ballRect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
#   screen.fill(white)
    screen.blit(ball, ballRect)
    pygame.display.flip()
