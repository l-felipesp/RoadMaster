#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu
from code.score import ScoreSystem


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
            score = ScoreSystem()
            score.window = self.window

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                player_score = [0]
                level = Level(self.window, 1, menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    score.save(self.window, menu_return, level_return)

            elif menu_return == MENU_OPTION[2]:
                score.show()

            else:
                pygame.quit()
                quit()

