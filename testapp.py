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
from Grid import Grid
from Size import Size
from traits.velocity import Velocity
from traits.jump import Jump
from level import Level

DELTATIME = 1/60


class TestApp:

    def __init__(self, size):
        self._running = False
        self._level = None
        self._clock = pygame.time.Clock()
        self.size = size
        pygame.init()
        self._screen = pygame.display.set_mode(self.size, RESIZABLE)
        self._rendersize = (320, 240)
        self._renderBuffer = pygame.Surface(self._rendersize)
        self._layers = []
        self._mario = None
        self.camera = Camera(256, 224)
        self.camera.pos = Vec2d(48, 0)
        self._lastCameraPos = Vec2d(0,0)
        self.gravity = 2000
        self._map = None
        self._level = None

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
        self._map = loadTilemap("level_test.tmx", assetdir)

        self._level = Level()
        self._level.level_size = Size(self._map.map.map_size)
        self._level.comp.layers.append(self.backgroundRenderer)
        #layer = self._map.get_layer("Foreground")

        dx = int(self.camera.width / self._map.map.tile_size.width)
        dy = int(self.camera.height / self._map.map.tile_size.height)
        for layer in self._map.layers:
            gg = None
            if layer.name == "Foreground":
                self.loadSingleLevel(self._level.grid, layer, dx, dy)
                self._level.renderLayers.append(self._level.grid)
            else:
                gg = Grid()
                self._level.renderLayers.append(gg)
                self.loadSingleLevel(gg, layer, dx, dy)

    def loadSingleLevel(self, grid, layer, dx, dy):
        for y in range(dy):
            for x in range(dx):
                data = grid.get(x, y)
                if data == None:
                    data = { "layer": []}
                data["layer"].append(layer.data_at(x, y))
                grid.set(x, y, data)
       

    def backgroundRenderer(self, level, buffer, camera):
        # TODO: Is not taking into consideration camera 
        cx = math.floor(camera.pos.x / self._map.map.tile_size.width)
        #cy = math.floor(camera.pos.y / self._map.map.tile_size.height)
        for y in range(level.level_size.height):
            dy = y * level.tile_size.height
            for x in range(cx, level.level_size.width + cx):
                dx = x * level.tile_size.width
                for layer in level.renderLayers:
                    data = layer.get(x, y)
                    if data == None:
                        continue
                    for id in data["layer"]:
                        buffer.blit(self._map.image_at_id(id), (dx, dy))
    
               
    def loadEntities(self):
        path = sys.path[0]
        assetdir = os.path.join(path, 'assets')
        spritesheet = Spritesheet(os.path.join(
            assetdir, "smb_char_sprites.gif"))
        self._mario = Entity("mario")
        self._mario.pos = Vec2d(64, 64)
        self._mario.size = Size(14, 18)
        self._mario.sprite = spritesheet.image_at((276, 42, 14, 18))
        self._mario.addTrait(Jump())
        self._mario.addTrait(Velocity())
        self._level.entities.add(self._mario)

    def handleDir(self, keyCode, keyState):
        print(f"handling keyboard input {keyCode} : {keyState}")

    def handleSpace(self, keyCode, keyState):
        print(f"handling keyboard input {keyCode} : {keyState}")
        if keyState == 1:
            self._mario.getTrait("jump").start()
        else:
            self._mario.getTrait("jump").cancel()

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
        self._level.on_update(delta_time)
        

    def on_render(self, delta_time):
        #self._renderBuffer.fill((0, 0, 0))

        #if self.camera.pos != self._lastCameraPos:
        if True:
            # draw backgrounds
            self._level.comp.draw(self._renderBuffer, self.camera)
            self._lastCameraPos = self.camera.pos

        #for l in self._layers:
        #    l.on_render(delta_time, self._renderBuffer)
        for e in self._level.entities:
            e.on_render(delta_time, self._renderBuffer)

        # render to screen
        self._screen.blit(pygame.transform.scale(self._renderBuffer, self.size), (0, 0))  # scale to window size

        self._mario.vel.y += self.gravity * delta_time
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
