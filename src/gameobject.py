import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(x - size/2, y - size/2, size, size)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.image = self.image.convert_alpha()
    def update(self, date):
        pass
