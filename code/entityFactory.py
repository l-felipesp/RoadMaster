#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1BG{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1BG{i}', position=(WIN_WIDTH, 0)))
                return list_bg
