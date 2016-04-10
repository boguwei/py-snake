# game
#
# author: boguwei@gmail.com
# date: 4/9/16

import sys
import pygame
from Snake import Snake

pygame.init()

WHITE = 255, 255, 255
BLACK = 0, 0, 0
width = 800
height = 600
screenSize = width, height
screen = pygame.display.set_mode(screenSize)

snakey = Snake(width/2, height/2, 0)
segmentSize = 6

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(WHITE)

    for segment in snakey.theSnake:
        segmentRect = pygame.Rect(
                segment.x - segmentSize / 2,
                segment.y - segmentSize / 2,
                segmentSize * 2,
                segmentSize * 2)
        segmentSurface = pygame.Surface((segmentRect.width, segmentRect.height))
        
        segmentSurface.fill(BLACK)
        screen.blit(segmentSurface, segmentRect)

    pygame.display.flip()
