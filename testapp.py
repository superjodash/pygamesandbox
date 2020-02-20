import pygame
import time
import sys
import random
import os
from keyboard import *
from pygame.locals import *
from time import gmtime, strftime
from pytiled_pygame import *
from camera import Camera
from layers import BackgroundLayer, ForegroundLayer
from entity import Entity
from Vec2d import Vec2d
from Size import Size
from traits.velocity import Velocity
from traits.jump import Jump

DELTATIME = 1/60


class TestApp:

    def __init__(self, size):
        self._running = False
        self._level = None
        self._clock = pygame.time.Clock()
        self.size = size
        self._rendersize = (256, 224)
        pygame.init()
        self._screen = pygame.display.set_mode(self.size, RESIZABLE)
        self._renderBuffer = pygame.Surface(self._rendersize)
        self._layers = []
        self._entities = []
        self._mario = None
        self.camera = Camera(256, 224)
        self.gravity = 2000

    def bootstrap(self):
        self.loadKeyboardHandling()
        self.loadLevel()
        self.loadEntities()

    def loadKeyboardHandling(self):
        self._keyboardState = KeyboardState()
        self._keyboardState.addMapping(pygame.K_w, self.handleDir)
        self._keyboardState.addMapping(pygame.K_a, self.handleDir)
        self._keyboardState.addMapping(pygame.K_s, self.handleDir)
        self._keyboardState.addMapping(pygame.K_d, self.handleDir)
        self._keyboardState.addMapping(pygame.K_SPACE, self.handleSpace)

    def loadLevel(self):
        #self._level = Level()
        path = sys.path[0]
        assetdir = os.path.join(path, 'assets')
        map = loadTilemap("level_test.tmx", assetdir)
        # for layer in map.layers:
        for ix, layer in enumerate(map.layers):
            if layer.name == "Sky" or layer.name == "Background":
                self.add_layer(BackgroundLayer(self.camera, ix, map))
            elif layer.name == "Foreground":
                self.add_layer(ForegroundLayer(self.camera, ix, map))

    def loadEntities(self):
        path = sys.path[0]
        assetdir = os.path.join(path, 'assets')
        spritesheet = Spritesheet(os.path.join(
            assetdir, "smb_char_sprites.gif"))
        self._mario = Entity()
        self._mario.pos = Vec2d(64, 64)
        self._mario.size = Size(14, 18)
        self._mario.sprite = spritesheet.image_at((276, 42, 14, 18))
        self._mario.addTrait(Jump())
        self._mario.addTrait(Velocity())
        self._entities.append(self._mario)

    def handleDir(self, keyCode, keyState):
        print(f"handling keyboard input {keyCode} : {keyState}")

    def handleSpace(self, keyCode, keyState):
        print(f"handling keyboard input {keyCode} : {keyState}")
        if keyState == 1:
            self._mario.getTrait("jump").start()
        else:
            self._mario.getTrait("jump").cancel()

    def add_layer(self, layer):
        layer.canvassize = self._rendersize
        self._layers.append(layer)

    def run(self):
        self.bootstrap()
        self._running = True
        #accumulatedTime = 0
        #lastTime = 0
        while self._running:
            time = self._clock.tick()
            #accumulatedTime += (time - lastTime) / 1000
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop(DELTATIME)
            # while(accumulatedTime > DELTATIME):
            self.on_render(DELTATIME)
            #accumulatedTime -= DELTATIME
            #lastTime = time
            self._clock.tick(30)

        self.on_cleanup()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self._keyboardState.handleEvent(event)
        elif event.type == VIDEORESIZE:
            self.size = event.dict['size']
            self._screen = pygame.display.set_mode(self.size, RESIZABLE)

    def on_loop(self, delta_time):
        # physics
        for e in self._entities:
            e.update(delta_time)

    def on_render(self, delta_time):
        self._renderBuffer.fill((0, 0, 0))

        for l in self._layers:
            l.on_render(delta_time, self._renderBuffer)
        for e in self._entities:
            e.on_render(delta_time, self._renderBuffer)
        self._screen.blit(pygame.transform.scale(
            self._renderBuffer, self.size), (0, 0))  # scale to window size
        self._mario.vel.y += self.gravity * delta_time
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
