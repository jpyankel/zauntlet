# Drawing functions like redrawAll()
import pygame
def redrawAll(screen, data, groups):
    groups.player.update(data)
    groups.player.draw(screen)
    
class SpriteGroups(object):
    def __init__(self):
        self.player = pygame.sprite.Group()