from src.gameobject import GameObject
from src.static import *
class Player (GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.dx = 2
        self.dy = 2
        self.facing = "down"
        self.image.blit(Image.LINK, (0,0))
    def update(self, data):
        if data.mostRecentDir == "up":
            self.y -= self.dy
            self.facing = data.mostRecentDir
        elif data.mostRecentDir == "down":
            self.y += self.dy
            self.facing = data.mostRecentDir
        elif data.mostRecentDir == "left":
            self.x -= self.dx
            self.facing = data.mostRecentDir
        elif data.mostRecentDir == "right":
            self.x += self.dx
            self.facing = data.mostRecentDir
        self.checkBounds(data)
        self.rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2,
                                self.size, self.size)

    def fireProjectile(self, data):
        print("space presses, facing:", self.facing)
        data.groups.projectiles.add(Projectile(self.x, self.y,\
                                    self.facing, Value.PROJECTILE_SIZE))

    def checkBounds (self, data):
        """
            Ensures that a scene transition takes place if the player moves off
             the screen.
        """
        sceneTransitionDir = None
        if self.x + Value.PLAYER_SIZE/2 >= Value.WINDOW_WIDTH + Value.PLAYER_SIZE:
            sceneTransitionDir = "right"
            self.x = Value.WINDOW_WIDTH - Value.PLAYER_SIZE # Undo move in advance
        elif self.x - Value.PLAYER_SIZE/2 <= -Value.PLAYER_SIZE:
            sceneTransitionDir = "left"
            self.x = Value.PLAYER_SIZE
        elif self.y + Value.PLAYER_SIZE/2 >= Value.WINDOW_HEIGHT + Value.PLAYER_SIZE:
            sceneTransitionDir = "down"
            self.y = Value.WINDOW_HEIGHT - Value.PLAYER_SIZE
        elif self.y - Value.PLAYER_SIZE/2 <= -Value.PLAYER_SIZE:
            sceneTransitionDir = "up"
            self.y = Value.PLAYER_SIZE
        if sceneTransitionDir != None:
            # Attempt a screen transition:
            data.tryTransition(sceneTransitionDir)

class Projectile(GameObject):
    def __init__(self, x, y, direction, size):
        super().__init__(x, y, size)
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
