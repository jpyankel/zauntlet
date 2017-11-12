# Main game loop
import pygame, socket, math, argparse
from src.gamedata import GameData
from src.static import *
from src.render import *

def main ():
    pygame.init()
    clock = pygame.time.Clock()
    data = GameData()
    # Initialize Screen:
    screen = pygame.display.set_mode((data.window.width, data.window.height))
    Image.init()
    data.initGroups()
    data.dungeonMap.loadCurrentRoom(data)

    while data.running:
        time = clock.tick(60) #similar to timerDelay
        screen.fill((50, 50, 50)) # background
        for event in pygame.event.get():
            handle(event,data)
        updateAll(data)
        checkCollision(data)
        redrawAll(screen, data)
        pygame.display.flip()
        #print(data.mostRecentDir)
    pygame.quit()

def handle(event,data):
    #When you quit the window
    if event.type == pygame.QUIT:
        data.running = False
#when you press the keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            data.mostRecentDir = "up"
            data.keysPressed.append("up")
        if event.key == pygame.K_DOWN:
            data.mostRecentDir = "down"
            data.keysPressed.append("down")
        if event.key == pygame.K_LEFT:
            data.mostRecentDir = "left"
            data.keysPressed.append("left")
        if event.key == pygame.K_RIGHT:
            data.mostRecentDir = "right"
            data.keysPressed.append("right")
        if event.key == pygame.K_ESCAPE:#when you press the escape button
            data.running = False
        if event.key == pygame.K_SPACE:
            data.player.fireProjectile(data)
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
        if data.mostRecentDir == None and len(data.keysPressed)> 0:
            data.mostRecentDir = data.keysPressed[-1]

if __name__ == "__main__":
    main()
