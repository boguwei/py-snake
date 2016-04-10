# game
#
# author: boguwei@gmail.com
# date: 4/9/16

import sys
import pygame
import time
from Snake import Snake
from KeyboardManager import KeyboardManager

pygame.init()
gameDifficulty = 1      # the higher the difficulty, the faster the snake moves

# configure pygame window parameters
WHITE = 255, 255, 255
BLACK = 0, 0, 0
width = 800
height = 600
screenSize = width, height
screen = pygame.display.set_mode(screenSize)

# make snake alive
snakey = Snake(width/2, height/2, 0)

# make snake recognize human overlord
eventManager = KeyboardManager(snakey)

# enter game loop
while snakey.isAlive:
    frameStart = time.perf_counter()

    # check for overlord orders
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            eventManager.eventSwitcher(event)

    # move, you slippery bastard, move
    snakey.moveSnake()
        
    # render to screen
    screen.fill(WHITE)
    for segment in snakey.theSnake:
        segmentRect = pygame.Rect(
                segment.x - segment.size / 2,
                segment.y + segment.size / 2,
                segment.size,
                segment.size)
        segmentSurface = pygame.Surface((segmentRect.width, segmentRect.height))
        segmentSurface.fill(BLACK)
        screen.blit(segmentSurface, segmentRect)
    pygame.display.flip()

    # don't hit anything
    head = snakey.theSnake[0]
    if head.x < 0 or head.x > width or head.y < 0 or head.y > height:
        snakey.isAlive = False

    frameEnd = time.perf_counter()
    frame = (frameEnd - frameStart) 
    if frame < 1 / gameDifficulty:
        time.sleep(1 / gameDifficulty - frame)
