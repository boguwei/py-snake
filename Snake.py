# Segment
#
# author:   boguwei@gmail.com
# date:     4/2/16

import Segment

class Snake:

    def __init__(self, x, y, z):
        self.moveX = 0
        self.moveY = 0
        self.moveZ = 0
        self.theSnake = [Segment(x, y, z)]
