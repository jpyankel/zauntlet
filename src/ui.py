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
        """
            Refreshes the hearts UI drawn on the screen.
        """
        data.groups.ui = pygame.sprite.Group() # Remove all old sprites.
        heartOrigin = Value.UI_HEART_SIZE * 2
        heartMargin = Value.UI_HEART_SIZE
        # Loop through the amount of hearts the player has and draw each:
        for heartIndex in range(data.player.HP):
            newHeart = Heart(heartOrigin + heartMargin*heartIndex, heartOrigin,
                             Value.UI_HEART_SIZE)
            data.groups.ui.add(newHeart) # Add new heart to be rendered

    def drawGameOver (self, data):
        """ Draws the game over screen """
        data.screenUI = Image.GAMEOVERSCREEN

    def drawWinScreen (self, data):
        """ Draws the win screen """
        data.screenUI = Image.WINSCREEN

class Heart (GameObject):
    """
        UI Heart sprite
    """
    def __init__ (self, x, y, size):
        super().__init__(x, y, size)
        self.image.blit(Image.HEART, (0,0))
