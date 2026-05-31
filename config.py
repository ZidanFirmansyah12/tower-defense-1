import pygame
from enum import Enum

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREEN = (0, 255, 100)
RED = (255, 60, 60)
BLUE = (0, 150, 255)
YELLOW = (255, 255, 0)
PURPLE = (180, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
LIME = (50, 205, 50)
DARK_ORANGE = (255, 140, 0)
MAGENTA = (255, 0, 255)
LIGHT_CYAN = (100, 200, 255)
PINK = (255, 192, 203)

font = pygame.font.SysFont("arial", 28)
small_font = pygame.font.SysFont("arial", 18)
tiny_font = pygame.font.SysFont("arial", 14)


class GameState(Enum):
    MENU = 0
    DIFFICULTY_SELECT = 1
    PLAYING = 2
    PAUSED = 3
    WAVE_GAP = 4
    GAME_OVER = 5


class WaveState(Enum):
    IDLE = 1
    SPAWNING = 2
    IN_PROGRESS = 3
    COMPLETED = 4


class Difficulty(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3


class TargetMode(Enum):
    FIRST = 1
    LAST = 2
    STRONGEST = 3
    CLOSEST = 4


class DifficultyConfig:
    @staticmethod
    def get_config(difficulty):
        configs = {
            Difficulty.EASY: {
                'enemy_health_multiplier': 0.7,
                'enemy_speed_multiplier': 0.8,
                'spawn_rate': 40,
                'starting_money': 200,
                'base_health': 20,
                'difficulty_name': 'EASY'
            },
            Difficulty.NORMAL: {
                'enemy_health_multiplier': 1.0,
                'enemy_speed_multiplier': 1.0,
                'spawn_rate': 30,
                'starting_money': 100,
                'base_health': 10,
                'difficulty_name': 'NORMAL'
            },
            Difficulty.HARD: {
                'enemy_health_multiplier': 1.5,
                'enemy_speed_multiplier': 1.2,
                'spawn_rate': 25,
                'starting_money': 50,
                'base_health': 5,
                'difficulty_name': 'HARD'
            }
        }
        return configs.get(difficulty, configs[Difficulty.NORMAL])
