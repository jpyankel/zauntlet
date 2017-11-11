from src.creature import Creature
from src.static import *
class Player (Creature):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.dx = 1
        self.dy = 1
        self.image.blit(Image.LINK, self.rect)
    def update(self, data):
        if "up" in data.keysPressed:
            self.y -= self.dy
        if "down" in data.keysPressed:
            self.y += self.dy
        if "left" in data.keysPressed:
            self.x -= self.dx
        if "right" in data.keysPressed:
            self.x += self.dx
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)