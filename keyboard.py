import pygame

PRESSED = 1
RELEASED = 0

class KeyboardState(object):

    def __init__(self):
        self.keyStates = {}
        self.keyMap= {}
        pass

    def addMapping(self, keyCode, callback):
        self.keyMap[keyCode] = callback

    def handleEvent(self, event):
        if self.keyMap.get(event.key) == None:
            return False
        
        keyState = RELEASED
        if event.type == pygame.KEYDOWN:
            keyState = PRESSED

        keyCode = event.key

        if self.keyStates.get(keyCode) == keyState:
            return

        self.keyStates[keyCode] = keyState
        self.keyMap[keyCode](keyCode, keyState)

    