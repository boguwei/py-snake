# KeyboardManager
#
# author: boguwei@gmail.com
# date: 4/9/2016

class KeyboardManager:

    def __init__(self, snake):
        self.snake = snake
        self.segmentSize = snake.theSnake[0].size
        
    def eventSwitcher(self, keyEvent):
        methodName = 'keyDown' + str(keyEvent.key)
        methodToCall = getattr(self, methodName, lambda: "nothing")

        return methodToCall()

    def keyDown27(self):
        print('\nESC key pressed.')
        self.snake.isAlive = False

    def keyDown97(self):
        print('\na key pressed.')
        self.snake.moveX = -1 * self.segmentSize
        self.snake.moveY = 0

    def keyDown100(self):
        print('\nd key pressed.')
        self.snake.moveX = 1 * self.segmentSize
        self.snake.moveY = 0

    def keyDown103(self):
        print('\ng key pressed.')
        self.snake.growSnake()

    def keyDown106(self):
        print('\nj key pressed.')
        if self.snake.moveZ == 0:
            self.snake.moveZ = -1

    def keyDown107(self):
        print('\nk key pressed.')
        if self.snake.moveZ == 0:
            self.snake.moveZ = 1

    def keyDown115(self):
        print('\ns key pressed.')
        self.snake.moveX = 0
        self.snake.moveY = 1 * self.segmentSize

    def keyDown119(self):
        print('\nw key pressed.')
        self.snake.moveX = 0
        self.snake.moveY = -1 * self.segmentSize
