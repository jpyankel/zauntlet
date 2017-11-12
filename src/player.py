from src.gameobject import GameObject
from src.static import *
class Player (GameObject):
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
        elif "space" in data.keysPressed:
            self.fireProjectile(data)
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)
    def fireProjectile(self, data):
        data.groups.projectiles.add(Projectile(self.x, self.y,\
                                    data.mostRecentDir, Value.PROJECTILE_SIZE))

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