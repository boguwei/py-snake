# Segment
#
# author:   boguwei@gmail.com
# date:     4/2/16

from Segment import Segment

class Snake:

    def __init__(self, x, y, z):
        self.moveX = 0
        self.moveY = 0
        self.moveZ = 0
        self.theSnake = [Segment(x, y, z)]

    def moveSnake(self):
        for i in reversed(range(1, len(self.theSnake))):
            self.theSnake[i].copySegment(self.theSnake[i-1])
        self.theSnake[0].moveSegment(self.moveX, self.moveY, self.moveZ)

    def growSnake(self):
        lenSnake = len(self.theSnake)
        lastSegment = Segment(
                self.theSnake[lenSnake - 1].x,
                self.theSnake[lenSnake - 1].y,
                self.theSnake[lenSnake - 1].z)
        lastSegment.moveSegment(
                self.moveX * -1,
                self.moveY * -1,
                self.moveZ * -1)
        self.theSnake.append(lastSegment)

    def printSnake(self):
        for i, seg in enumerate(self.theSnake):
            print(i, ' ', end='')
            seg.printSegment()

