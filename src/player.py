from src.creature import Creature
from src.static import *
class Player (Creature):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.dx = 2
        self.dy = 2
        self.image.blit(Image.LINK, (0,0))
    def update(self, data):
        
        if data.mostRecentDir == "up":
            self.y -= self.dy
        elif data.mostRecentDir == "down":
            self.y += self.dy
        elif data.mostRecentDir == "left":
            self.x -= self.dx
        elif data.mostRecentDir == "right":
            self.x += self.dx
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)