# Our main gamedata class.
from src.windowdata import WindowData
from src.player import Player
import pygame

class GameData(object):
    def __init__ (self):
        self.running = True
        self.window = WindowData()
        self.keysPressed = set()
        self.mostRecentDir = None 
    def initGroups(self):
        self.localPlayer = Player(self.window.width/2, self.window.height/2, 32)
        self.groups = SpriteGroups()
        self.groups.player.add(self.localPlayer)

class SpriteGroups(object):
    def __init__(self):
        self.walls = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

