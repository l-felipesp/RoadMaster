#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame
from typing import List, Dict
import os

from code.background import Background
from code.const import WIN_WIDTH
from code.enemyForward import EnemyForward
from code.enemyReverse import EnemyReverse
from code.player import Player

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = os.path.join(BASE_DIR, "asset")

_SKIN_CACHE: Dict[str, List[pygame.Surface]] = {}


def _discover_and_load_skins(entity_key: str) -> List[pygame.Surface]:
    if entity_key in _SKIN_CACHE:
        return _SKIN_CACHE[entity_key]

    surfaces: List[pygame.Surface] = []
    exts = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp")

    key = entity_key.lower()
    for fname in os.listdir(ASSET_DIR):
        lower = fname.lower()
        if any(lower.endswith(ext) for ext in exts) and (key in lower or lower.startswith(key + "_")):
            path = os.path.join(ASSET_DIR, fname)
            surf = pygame.image.load(path).convert_alpha()
            surfaces.append(surf)

    _SKIN_CACHE[entity_key] = surfaces


class EntityFactory:

    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1BG':  # carregamento dos backgrounds e adição à lista na ordem de 0 a 5
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1BG{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1BG{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player':  # carregamento do Player
                return Player('Player', position=(10, 170))

            case 'EnemyForward':
                forward_lane_y = [245, 285]  # faixas para mão de direção
                enemy = EnemyForward(f'EnemyForward', position=(WIN_WIDTH + 10, random.choice(forward_lane_y)))
                skins = _discover_and_load_skins('EnemyForward')
                if skins:
                    chosen_surf = random.choice(skins)
                    left, top = position if position != (0, 0) else (enemy.rect.left, enemy.rect.top)
                    enemy.surf = chosen_surf
                    enemy.rect = enemy.surf.get_rect(left=left, top=top)
                return enemy

            case 'EnemyReverse':
                reverse_lane_y = [205, 165]  # faixas para contra-mão
                enemy = EnemyReverse(f'EnemyReverse', position=(WIN_WIDTH - 10, random.choice(reverse_lane_y)))
                skins = _discover_and_load_skins('EnemyReverse')
                if skins:
                    chosen_surf = random.choice(skins)
                    left, top = position if position != (0, 0) else (enemy.rect.left, enemy.rect.top)
                    enemy.surf = chosen_surf
                    enemy.rect = enemy.surf.get_rect(left=left, top=top)
                return enemy
