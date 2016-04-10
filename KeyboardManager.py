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

    def keyDown115(self):
        print('\nS key pressed.')

    def keyDown119(self):
        print('\nW key pressed.')

    def keyDown273(self):
        print('\nUP key pressed.')
        self.snake.moveX = 0
        self.snake.moveY = -1 * self.segmentSize
        
    def keyDown274(self):
        print('\nDOWN key pressed.')
        self.snake.moveX = 0
        self.snake.moveY = 1 * self.segmentSize

    def keyDown275(self):
        print('\nRIGHT key pressed.')
        self.snake.moveX = 1 * self.segmentSize
        self.snake.moveY = 0

    def keyDown276(self):
        print('\nLEFT key pressed.')
        self.snake.moveX = -1 * self.segmentSize
        self.snake.moveY = 0
