# Constants for various data files
import pygame
class Image(object):
    @staticmethod
    def init():
        Image.LINK = pygame.image.load("src/images/link.png").convert_alpha()
        Image.PROJECTILE = pygame.image.load("src/images/projectile.png").convert_alpha()
        Image.WALL = pygame.image.load("src/images/wall.png").convert_alpha()
        Image.TILE = pygame.image.load("src/images/tile.png").convert_alpha()
        Image.MONSTER = pygame.image.load("src/images/monster.png").convert_alpha()
        Image.SPAWNER = pygame.image.load("src/images/spawner.png").convert_alpha()

class StaticPath ():
    DUNGEON_LAYOUT_DIR = "src/dungeonlayout/"

class StaticDungeonLayout ():
    DUNGEON_ROOM_WIDTH = 20
    DUNGEON_ROOM_HEIGHT = 15
    DUNGEON_WIDTH = 5
    DUNGEON_HEIGHT = 5
    WALL_CHAR = "#"
    TILE_CHAR = "-"
    PLAYER_CHAR = "P"
    MONSTER_CHAR = "M"
    SPAWNER_CHAR = "S"

class Value(object):
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    PLAYER_SIZE = 32
    PROJECTILE_SIZE = 16
    TERRAIN_SIZE = 32
    MONSTER_SIZE = 32
    SPAWNER_SIZE = 32
