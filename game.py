# game
#
# author: boguwei@gmail.com
# date: 4/9/16

import sys
import pygame
import time
import random
from collections import deque
from colors import colors
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
gameDifficulty = 3   # the higher the difficulty, the faster the snake moves
random.seed()

# configure pygame window parameters
width   = 600
height  = 400
screenSize = width, height
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('pySnake by bogu')

# make snake alive
snakey = Snake(width/2, height/2, 0)
segmentRectQueue = deque()
segmentSize = snakey.theSnake[0].size

# make target alive
target = Segment(
        random.randrange(segmentSize, width - segmentSize, segmentSize),
        random.randrange(segmentSize, height - segmentSize, segmentSize),
        random.randrange(0, len(colors)))

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
        screen.fill((255, 255, 255))
        
        targetRect = makeRect(target)
        targetSurface = pygame.Surface((targetRect.width, targetRect.height))
        targetSurface.fill(colors[target.z])
        screen.blit(targetSurface, targetRect)

        for segment in snakey.theSnake:
            segmentRect = makeRect(segment)
            segmentRectQueue.append(segmentRect)
            segmentSurface = pygame.Surface((segmentRect.width, segmentRect.height))
            segmentSurface.fill(colors[segment.z])
            screen.blit(segmentSurface, segmentRect)

        pygame.display.flip()

    # don't hit anything except the target
    if len(segmentRectQueue) > 0:
        head =  segmentRectQueue.popleft()
        bodyInd = head.collidelist(segmentRectQueue)
        if head.colliderect(targetRect) and snakey.theSnake[0].z == target.z:
            target.x = random.randrange(segmentSize, width - segmentSize, segmentSize)
            target.y = random.randrange(segmentSize, height - segmentSize, segmentSize)
            target.z = random.randrange(0, len(colors))
            snakey.growSnake()
        elif bodyInd >= 0:
            if snakey.theSnake[0].z == snakey.theSnake[bodyInd + 1].z:
                snakey.isAlive = False
        else:
            head = snakey.theSnake[0]
            if head.x < 0 or head.x > width or head.y < 0 or head.y > height:
                snakey.isAlive = False

    frameEnd = time.perf_counter()
    frame = (frameEnd - frameStart) 
    if frame < 1 / gameDifficulty:
        time.sleep(1 / gameDifficulty - frame)
