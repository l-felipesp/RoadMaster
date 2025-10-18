#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import choice

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import entityFactory, enemyForward, player
from code.EntityMediator import EntityMediator
from code.const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, TIMEOUT_LEVEL, COLOR_YELLOW
from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window: Surface, number: int, game_mode: str, player_score: int):
        self.window = window
        self.number = number
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        player = EntityFactory.get_entity('Player')
        if not hasattr(player, 'score'):
            player.score = 0
        self.player = player
        self.start_time = pygame.time.get_ticks()
        self.score_rate = 10.0
        self.entity_list.append(self.player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        if number == 0 and isinstance(player_score, (list, tuple)) and len(player_score) > 0:
            self.player.score = player_score[0]

    def run(self, player_score: list[int]):
        pygame.mixer.music.load(f'./asset/Level{self.number}.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            dt_ms = clock.tick(60)
            dt = dt_ms / 1000.0

            # Atualiza score do player por tempo decorrido
            if hasattr(self, 'player') and getattr(self.player, 'alive', True):
                self.player.score = getattr(self.player, 'score', 0) + self.score_rate * dt

            # Desenhar + atualizar entidades
            for ent in list(self.entity_list):
                if ent is None:
                    continue
                self.window.blit(source=ent.surf, dest=ent.rect)
                try:
                    ent.move(dt)
                except TypeError:
                    ent.move()
                # desenha status do player quando encontrar a entidade Player
                if getattr(ent, 'name', None) == 'Player':
                    self.level_text(14, f'Player - Health: {ent.health} | SCORE: {int(ent.score)}', COLOR_YELLOW,
                                    (5, 5))

            # eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('EnemyForward'))
                    self.entity_list.append(EntityFactory.get_entity('EnemyReverse'))

            # Informações extras - FPS e quantidade de entidades - apenas debug
            # self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            # self.level_text(14, f'entities: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # verificações de colisão e health
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            player_dead = False
            if getattr(self, 'player', None) is not None:
                if getattr(self.player, 'health', 1) <= 0:
                    player_dead = True
                if self.player not in self.entity_list:
                    player_dead = True

            if player_dead:
                final_score = int(getattr(self.player, 'score', 0))
                self.entity_list = [e for e in self.entity_list if getattr(e, 'name', None) != 'Player']
                return [final_score]

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, text_rect=None):
        text_font: Font = pygame.font.SysFont("Arial Black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
