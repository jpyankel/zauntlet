from src.gameobject import GameObject
from src.static import *
class Player (GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.dx = 2
        self.dy = 2
        self.image.blit(Image.LINK, (0,0))
    def update(self, data):
        if "up" in data.keysPressed:
            self.y -= self.dy
        if "down" in data.keysPressed:
            self.y += self.dy
        if "left" in data.keysPressed:
            self.x -= self.dx
        if "right" in data.keysPressed:
            self.x += self.dx
        if "space" in data.keysPressed:
            self.fireProjectile(data)
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)
    def fireProjectile(self, data):
        data.groups.projectiles.add(Projectile(self.x, self.y, "up",\
                                               Value.PROJECTILE_SIZE)

class Projectile(GameObject):
    def __init__(self, x, y, direction, size):
        if direction == "up": self.dx, self.dy = 0, -10
        elif direction == "down": self.dx, self.dy = 0, 10
        elif direction == "left": self.dx, self.dy = -10, 0
        elif direction == "right": self.dx, self.dy = 10, 0
        self.image.blit(Image.PROJECTILE, (0,0))
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)