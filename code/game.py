#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Road Master")
        self.menu = Menu(self.window)

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, '1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[1]:
                level = Level(self.window, '2', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[2]:
                level = Level(self.window, '3', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()
            else:
                pass


