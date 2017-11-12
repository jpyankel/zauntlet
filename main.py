# Main game loop
import pygame, socket, math
from src.gamedata import GameData
from src.static import *
from src.render import redrawAll, SpriteGroups

def main():
    pygame.init()
    clock = pygame.time.Clock()
    data = GameData()
    screen = pygame.display.set_mode((data.window.width, data.window.height))
    Image.init()
    data.initPlayer()
    
    groups = SpriteGroups()
    groups.player.add(data.localPlayer)
    
    while data.running:
        time = clock.tick(60) #similar to timerDelay
        screen.fill((255,0,0))
        for event in pygame.event.get():
            handle(event,data)
        screen.fill((50,50,50))
        redrawAll(screen, data, groups)
        pygame.display.flip()
        #print(data.mostRecentDir)
    pygame.quit()
def handle(event,data):
#When you quit the window
    if event.type == pygame.QUIT:
        data.running = False
#when you press the keys
    if event.type == pygame.KEYDOWN:
        print(event.key)
        if event.key == pygame.K_UP:
            data.mostRecentDir = "up"
            data.keysPressed.add("up")
        if event.key == pygame.K_DOWN:
            data.mostRecentDir = "down"
            data.keysPressed.add("down")
        if event.key == pygame.K_LEFT:
            data.mostRecentDir = "left"
            data.keysPressed.add("left")
        if event.key == pygame.K_RIGHT:
            data.mostRecentDir = "right"
            data.keysPressed.add("right")
        if event.key == pygame.K_ESCAPE:#when you press the escape button
            data.running = False
#when you get off the keys
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            data.keysPressed.remove("up")
            if data.mostRecentDir == "up":
                data.mostRecentDir = None
        if event.key == pygame.K_DOWN:
            data.keysPressed.remove("down")
            if data.mostRecentDir == "down":
                data.mostRecentDir = None
        if event.key == pygame.K_LEFT:
            data.keysPressed.remove("left")
            if data.mostRecentDir == "left":
                data.mostRecentDir = None
        if event.key == pygame.K_RIGHT:
            data.keysPressed.remove("right")
            if data.mostRecentDir == "right":
                data.mostRecentDir = None

main()

