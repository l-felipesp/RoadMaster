# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1BG0': 1,
    'Level1BG1': 2,
    'Level1BG2': 3,
    'Level1BG3': 4,
    'Level1BG4': 5,
    'Level1BG5': 5,
    'Player': 2,
    'EnemyForward': 2,
    'EnemyReverse': -4,

}

# M
MENU_OPTION = ('NEW GAME - ARCADE', 'NEW GAME - ENDLESS', 'ENTER PASSWORD', 'QUIT')

#S
SPAWN_TIME = 6000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
