import pygame
from src.gameobject import GameObject
from src.static import *

class UI ():
    """
        User interface class
    """

    def __init__ (self, data):
        self.updateHearts(data)

    def updateHearts(self, data):
        data.groups.ui = pygame.sprite.Group()
        heartOrigin = Value.UI_HEART_SIZE * 2
        heartMargin = Value.UI_HEART_SIZE
        for heartIndex in range(data.player.HP):
            newHeart = Heart(heartOrigin + heartMargin*heartIndex, heartOrigin,
                             Value.UI_HEART_SIZE)
            data.groups.ui.add(newHeart)

class Heart (GameObject):
    """
        UI Heart sprite
    """
    def __init__ (self, x, y, size):
        super().__init__(x, y, size)
        self.image.blit(Image.HEART, (0,0))
