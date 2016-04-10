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
        self.len = 1
        self.theSnake = [Segment(x, y, z)]
        self.isAlive = True

    def moveSnake(self):
        for i in reversed(range(1, self.len)):
            self.theSnake[i].copySegment(self.theSnake[i-1])
        self.theSnake[0].moveSegment(self.moveX, self.moveY, self.moveZ)

    def growSnake(self):
        lastSegment = Segment(
                self.theSnake[self.len- 1].x,
                self.theSnake[self.len- 1].y,
                self.theSnake[self.len- 1].z)
        lastSegment.moveSegment(
                self.moveX * -1,
                self.moveY * -1,
                self.moveZ * -1)
        self.theSnake.append(lastSegment)
        self.len += 1

    def printSnake(self):
        for i, seg in enumerate(self.theSnake):
            print(i, ' ', end='')
            seg.printSegment()

