#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code import entityFactory
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, number, menu_option):
        self.window = window
        self.number = number
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
