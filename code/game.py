#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Road Master")
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.window)

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()



