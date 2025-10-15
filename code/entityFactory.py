#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemyForward import EnemyForward
from code.enemyReverse import EnemyReverse
from code.player import Player


class EntityFactory:

    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1BG': #carregamento dos backgrounds e adição à lista na ordem de 0 a 5
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1BG{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1BG{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player': #carregamento do Player
                return Player('Player', position=(10, 170))

            case 'EnemyForward': #carrega os carros inimigos na mão de direção
                forward_lane_y = [245, 285] # define as faixas na mão de direção
                return EnemyForward(f'EnemyForward', position=(WIN_WIDTH + 10, random.choice(forward_lane_y))) #spawn random entre as faixas
            case 'EnemyReverse': #carrega os carros inimigos na contra-mão de direção
                reverse_lane_y = [205, 165] # define as faixas na contra-mão de direção
                return EnemyReverse(f'EnemyReverse', position=(586, random.choice(reverse_lane_y))) #spawn random entre as faixas
