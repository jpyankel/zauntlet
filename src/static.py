# Constants for various data files
import pygame
class Image(object):
    @staticmethod
    def init():
        Image.LINK = pygame.image.load("src/images/link.png").convert_alpha()
        Image.LINK = pygame.transform.scale(Image.LINK, (Value.PLAYER_SIZE, Value.PLAYER_SIZE))
        Image.PROJECTILE = pygame.image.load("src/images/projectile.png").convert_alpha()
        Image.PROJECTILE = pygame.transform.scale(Image.PROJECTILE, (Value.PROJECTILE_SIZE, Value.PROJECTILE_SIZE))
        Image.WALL = pygame.image.load("src/images/wall.png").convert_alpha()
        Image.TILE = pygame.image.load("src/images/tile.png").convert_alpha()
        Image.MONSTER = pygame.image.load("src/images/monster.png").convert_alpha()
        Image.MONSTER = pygame.transform.scale(Image.MONSTER, (Value.MONSTER_SIZE, Value.MONSTER_SIZE))
        Image.SPAWNER = pygame.image.load("src/images/spawner.png").convert_alpha()
        Image.SPAWNER = pygame.transform.scale(Image.SPAWNER, (Value.SPAWNER_SIZE, Value.SPAWNER_SIZE))

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
    FRAME_RATE = 60
    CELL_SIZE = 32
    PLAYER_SIZE = 48
    PROJECTILE_SIZE = 24
    TERRAIN_SIZE = 32
    MONSTER_SIZE = 48
    SPAWNER_SIZE = 32
