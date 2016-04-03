# Segment
# 
# author:   boguwei@gmail.com
# date:     3/31/16

class Segment:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def copyState(self, otherSegment):
        self.x = otherSegment.x
        self.y = otherSegment.y
        self.z = otherSegment.z

    def printSegment(self):
        print('[ ',str(self.x),' ',str(self.y),' ',str(self.z),' ]')
