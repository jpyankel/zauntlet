<<<<<<< HEAD
import pygame

class Creature(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(x - size/2, y - size/2, size, size)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.image = self.image.convert_alpha()
    def update(self, date):
=======
class Creature(object):
    def __init__(self):
        pass
    def move(self,dir):
        pass
    def draw(self):
>>>>>>> 6686f046cc82e5c0e872f9e6360ae356f34a0f6d
        pass
