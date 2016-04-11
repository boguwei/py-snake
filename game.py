# game
#
# author: boguwei@gmail.com
# date: 4/9/16

import sys
import pygame
import time
import random
from collections import deque
from Snake import Snake
from Segment import Segment
from KeyboardManager import KeyboardManager

def makeRect(segment):
    return pygame.Rect(
            segment.x - segment.size / 2,
            segment.y + segment.size / 2,
            segment.size,
            segment.size)

pygame.init()
gameDifficulty = 2      # the higher the difficulty, the faster the snake moves

# configure pygame window parameters
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
width = 400
height = 300
screenSize = width, height
screen = pygame.display.set_mode(screenSize)

# make snake alive
snakey = Snake(width/2, height/2, 0)
segmentRectQueue = deque()

# make target alive
target = Segment(
        random.randrange(0, width, snakey.theSnake[0].size),
        random.randrange(0, height, snakey.theSnake[0].size),
        0)

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
    if snakey.isAlive:
        segmentRectQueue.clear()
        screen.fill(WHITE)
        targetRect = makeRect(target)
        targetSurface = pygame.Surface((targetRect.width, targetRect.height))
        targetSurface.fill(RED)
        screen.blit(targetSurface, targetRect)
        for segment in snakey.theSnake:
            segmentRect = makeRect(segment)
            segmentRectQueue.append(segmentRect)
            segmentSurface = pygame.Surface((segmentRect.width, segmentRect.height))
            segmentSurface.fill(BLACK)
            screen.blit(segmentSurface, segmentRect)
        pygame.display.flip()

    # don't hit anything except the target
    if len(segmentRectQueue) > 0:
        head =  segmentRectQueue.popleft()
        if head.colliderect(targetRect):
            target.x = random.randrange(0, width, snakey.theSnake[0].size)
            target.y = random.randrange(0, height, snakey.theSnake[0].size)
            snakey.growSnake()
        elif head.collidelist(segmentRectQueue) >= 0:
            snakey.isAlive = False
        else:
            head = snakey.theSnake[0]
            if head.x < 0 or head.x > width or head.y < 0 or head.y > height:
                snakey.isAlive = False

    frameEnd = time.perf_counter()
    frame = (frameEnd - frameStart) 
    if frame < 1 / gameDifficulty:
        time.sleep(1 / gameDifficulty - frame)
