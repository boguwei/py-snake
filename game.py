# game
#
# author: boguwei@gmail.com
# date: 4/9/16

import pygame
import sys
import time
import copy
import itertools
import random
from collections import deque
from colors import colors
from Snake import Snake
from Segment import Segment
from KeyboardManager import KeyboardManager

def makeRectSegment(segment):
    return pygame.Rect(
            segment.x - segment.size / 2,
            segment.y + segment.size / 2,
            segment.size,
            segment.size)

# game options
width          = 600
height         = 400
gameDifficulty = 6 # the higher the difficulty, the faster the snake moves
random.seed()

# make snake alive
snakey = Snake(width/2, height/2, 0)
segmentRectQueue = deque()
segSize = snakey.theSnake[0].size

# configure pygame window 
pygame.init()
screenSize = width, height
screen = pygame.display.set_mode(screenSize, pygame.DOUBLEBUF)
screen.fill((255, 255, 255))
backgroundBlit = pygame.Surface((segSize, segSize))
backgroundBlit.fill((255, 255, 255))
pygame.display.set_caption('pySnake by bogu')


# make target alive
target = Segment(
        random.randrange(segSize, width - segSize, segSize),
        random.randrange(segSize, height - segSize, segSize),
        random.randrange(0, len(colors)))
targetRect = makeRectSegment(target)
targetSurface = pygame.Surface((targetRect.width, targetRect.height))
targetSurface.fill(colors[target.z])
screen.blit(targetSurface, targetRect)
pygame.display.update(targetRect)

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

    # wipe the screen
    oldSegmentRectQueue = copy.copy(segmentRectQueue)
    for segment in oldSegmentRectQueue:
        screen.blit(backgroundBlit, segment)

    # move, you slippery bastard, move
    snakey.moveSnake()
        
    # draw the screen
    segmentRectQueue.clear()
    for segment in snakey.theSnake:
        segmentRect = makeRectSegment(segment)
        segmentSurface = pygame.Surface((segmentRect.width, segmentRect.height))
        segmentSurface.fill(colors[segment.z])
        screen.blit(segmentSurface, segmentRect)
        segmentRectQueue.append(segmentRect)
    
    targetSurface.fill(colors[target.z])
    screen.blit(targetSurface, targetRect)
    
    pygame.display.update(oldSegmentRectQueue)
    pygame.display.update(segmentRectQueue)
    pygame.display.update(targetRect)

    # check collisions
    if len(segmentRectQueue) > 0:
        head =  segmentRectQueue[0]
        bodyList = deque(itertools.islice(segmentRectQueue,1,len(segmentRectQueue)))
        bodyInd = head.collidelist(bodyList)
        # hit a target
        if head.colliderect(targetRect) and snakey.theSnake[0].z == target.z:
            snakey.growSnake()
            #draw new target
            target.x = random.randrange(segSize, width - segSize, segSize)
            target.y = random.randrange(segSize, height - segSize, segSize)
            target.z = random.randrange(0, len(colors))
            targetRect = makeRectSegment(target)
            targetSurface.fill(colors[target.z])
            screen.blit(targetSurface, targetRect)
            pygame.display.update(targetRect)
        # hit yourself
        elif bodyInd >= 0:
            if snakey.theSnake[0].z == snakey.theSnake[bodyInd + 1].z:
                snakey.isAlive = False
        # hit the wall
        else:
            head = snakey.theSnake[0]
            if head.x < 0 or head.x > width or head.y < 0 or head.y > height:
                snakey.isAlive = False

    frameEnd = time.perf_counter()
    frame = (frameEnd - frameStart) 
    if frame < 1 / gameDifficulty:
        time.sleep(1 / gameDifficulty - frame)
