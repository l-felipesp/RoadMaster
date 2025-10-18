# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_DAMAGE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level1BG5': 0,
    'Player': 0,
    'EnemyForward': 50,
    'EnemyReverse': 50,
}
ENTITY_SCORE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level1BG5': 0,
    'Player': 0,
    'EnemyForward': 0,
    'EnemyReverse': 0,
}

ENTITY_SPEED = {
    'Level1BG0': 1,
    'Level1BG1': 2,
    'Level1BG2': 3,
    'Level1BG3': 4,
    'Level1BG4': 5,
    'Level1BG5': 5,
    'Player': 2,
    'EnemyForward': 2,
    'EnemyReverse': -16,
}
ENTITY_HEALTH = {
    'Level1BG0': 1,
    'Level1BG1': 2,
    'Level1BG2': 3,
    'Level1BG3': 4,
    'Level1BG4': 5,
    'Level1BG5': 5,
    'Player': 300,
    'EnemyForward': 999,
    'EnemyReverse': 999,
}

ENTITY_COLLISION = {
    'Player': 100,
}

# M
MENU_OPTION = ('NEW GAME - ARCADE', 'NEW GAME - TIME ATTACK', 'HIGH SCORES', 'QUIT')

# S
WIN_WIDTH = 576
WIN_HEIGHT = 324
SCORE_POS = {
    'Title': (WIN_WIDTH // 2, 50),
    'EnterName': (WIN_WIDTH // 2, 85),
    'ScoreValue': (WIN_WIDTH // 2, 110),
    'Name': (WIN_WIDTH // 2, 150),
    'Label': (WIN_WIDTH // 2, 190),
    # lista de posições para as linhas do TOP 10 (x,y)
    'Lines': [
        (WIN_WIDTH // 2, 220 + i * 26) for i in range(10)
    ],
    # fallback start y
    'LinesStartY': 220
}

SPAWN_TIME = 1900

# T
TIMEOUT_LEVEL = 20000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

