import os, sys
from testapp import TestApp
from layers import *
import pygame
from pytiled_pygame import *
import pytiled_parser

"""
Mario
Screen: 320x240 (20x15 tiles)
Screen Render: 256, 224 (16, 14)
Sprites: 8x8 and 8x16
"""


def runApp():
    #a = TestApp((320, 240))
    a = TestApp((640, 480))
    a.run()


if __name__ == "__main__":
    runApp()
