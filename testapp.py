import pygame
import time
import sys
import random
import os
from pygame.locals import *
from time import gmtime, strftime

class TestApp:

    def __init__(self, size):
        self._running = False
        self._layers = []
        self._clock = pygame.time.Clock()
        self.size = size
        self._rendersize= (320, 240)
        pygame.init()
        self._screen = pygame.display.set_mode(self.size, RESIZABLE)


    def add_layer(self, layer):
        layer.canvassize = self._rendersize
        self._layers.append(layer)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == VIDEORESIZE:
            self.size = event.dict['size']
            self._screen = pygame.display.set_mode(self.size, RESIZABLE)

    def on_loop(self):
        pass

    def on_render(self):
        buffer = pygame.Surface(self._rendersize)
        buffer.fill((92, 148, 252))
        for l in self._layers:
            l.on_render(self._clock.get_time(), buffer)
        self._screen.blit(pygame.transform.scale(buffer, self.size), (0, 0)) # scale to window size
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def run(self):
        self._running = True

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        