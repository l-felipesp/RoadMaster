#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from datetime import datetime

import pygame
from pygame import Surface, K_BACKSPACE, KEYDOWN, K_RETURN, K_ESCAPE, Rect
from pygame.font import Font

from code.DB_Proxy import DBProxy
from code.const import COLOR_ORANGE, COLOR_WHITE, WIN_WIDTH, SCORE_POS


class ScoreSystem:
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.score = 0
        self.window: Surface | None = None
        self.surf = None
        self.rect = None

    def save(self, window: Surface, game_mode: str, player_score):
        if isinstance(player_score, (list, tuple)):
            score_value = int(player_score[0]) if player_score else 0
        else:
            score_value = int(player_score or 0)
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pygame.mixer.music.load('./asset/Score.mp3')
        pygame.mixer.music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            # desenha background
            if self.surf:
                self.window.blit(source=self.surf, dest=self.rect)
            else:
                self.window.fill((0, 0, 0))

            # cabeçalho
            self.score_text(52, 'GAME OVER', COLOR_ORANGE, SCORE_POS['Title'])
            self.score_text(20, 'Enter your name (4 chars):', COLOR_WHITE, SCORE_POS['EnterName'])

            # exibe o score numérico
            self.score_text(20, f'Score: {score_value}', COLOR_WHITE, SCORE_POS['ScoreValue'])

            # eventos de input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    db_proxy.close()
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        safe_name = ''.join([c for c in name if c.isprintable() and c != '|'])[:20].upper()
                        db_proxy.save({'name': safe_name, 'score': score_value, 'date': get_formatted_date()})
                        db_proxy.close()
                        # depois de salvar, mostra a tabela
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4 and getattr(event, 'unicode', None):
                            # garantir apenas caracteres imprimíveis
                            ch = event.unicode
                            if ch.isprintable() and ch != '|':
                                name += ch.upper()

            self.score_text(28, name.ljust(4, '_'), COLOR_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer.music.load('./asset/Score.mp3')
        pygame.mixer.music.play(-1)
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.window.blit(self.surf, self.rect)
        self.score_text(48, 'TOP SCORES', COLOR_WHITE, SCORE_POS['Title'])
        self.score_text(12, 'Press ESC to return to MENU', COLOR_ORANGE, SCORE_POS['Tips'])
        self.score_text(20, 'NAME        SCORE             DATE', COLOR_WHITE, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        lines_pos = SCORE_POS.get('Lines', None)
        y_start = SCORE_POS.get('LinesStartY', 140)
        x_center = SCORE_POS.get('Title', (WIN_WIDTH // 2, 60))[0]

        for idx, record in enumerate(list_score[:10]):
            if len(record) >= 4:
                _, name, score, date = record
            else:
                name = record[0]
                score = record[1]
                date = record[2] if len(record) > 2 else ''
            if lines_pos and idx < len(lines_pos):
                pos = lines_pos[idx]
            else:
                pos = (x_center, y_start + idx * 26)

            self.score_text(15, f'         {name:8s}             {int(score):05d}              {date}', COLOR_WHITE, pos)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial Black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
