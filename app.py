import pygame
import time
import sys
import random
import os
from pygame.locals import *
from time import gmtime, strftime


class AssetTypes:
    FONTS = "fonts"
    IMAGES = "images"


class App:
    def __init__(self, width=640, height=480):
        self.deltatime = 0.0
        self._running = True
        self._display_surface = None
        self.size = self.width, self.height = width, height
        self.init_after()

    def init_after(self):
        self._assets = {}
        self._assets[AssetTypes.FONTS] = {}
        self._assets[AssetTypes.IMAGES] = {}

    def asset_add(self, type, key, asset):
        ag = self._assets.get(type)
        existing = ag.get(key)
        if existing == None:
            ag[key] = asset
        else:
            raise ValueError(key)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        pass

    def on_loop(self):
        pass

    def on_render(self):
        #self._display_surface.blit(self._image_surf, (0, 0))
        self.taskbar()
        pygame.display.flip()

    def taskbar(self):
        basicfont = pygame.font.SysFont(None, 24)
        text = basicfont.render(
            strftime("%Y-%m-%d", gmtime()), True, (0, 0, 0))
        text2 = basicfont.render(
            strftime("%H:%M:%S", gmtime()), True, (0, 0, 0))
        self._display_surface.fill((55, 155, 255))
        self._display_surface.blit(text, (self.width - 100, self.height - 37))
        self._display_surface.blit(text2, (self.width - 100, self.height - 17))

    def on_cleanup(self):
        pygame.quit()

    # game loop
    def run(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        while self._running:
            self.deltatime =
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
