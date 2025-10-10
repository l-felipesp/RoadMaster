#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemyForward import EnemyForward
from code.player import Player


class EntityFactory:

    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1BG{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1BG{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', position=(10, 170))

            case 'EnemyForward':
                ForwardLaneY = [245, 285]
                return EnemyForward(f'EnemyForward', position=(WIN_WIDTH+10, random.choice(ForwardLaneY)))

