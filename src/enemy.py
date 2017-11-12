from src.gameobject import GameObject
from src.static import *

class Spawner(GameObject): pass

class Monster(GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.dx = 2
        self.dy = 2
        self.image.blit(Image.MONSTER, (0,0))
    
    def update(self, data):
        # Moves the monster toward the player at the given speed.
        distance = ((self.y - data.player.y)**2 + (self.x - data.player.x)**2)**.5
        distanceX = data.player.x - self.x
        distanceY = data.player.y - self.y
        dx = (self.dx * distanceX)/distance
        dy = (self.dy * distanceY)/distance
        self.x += dx
        self.y += dy
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)