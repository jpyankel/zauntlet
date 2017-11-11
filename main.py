# Main game loop
import pygame, socket, math
from src.gamedata import GameData

def main():
    pygame.init()
    clock = pygame.time.Clock()
    data = GameData()
    screen = pygame.display.set_mode((data.window.width, data.window.height))

    running = True
    while running:
        time = clock.tick(60) #similar to timerDelay
        screen.fill((255,0,0))
        for event in pygame.event.get():
<<<<<<< HEAD
            handle(event,data)
    
    pygame.quit()
    
def handle(event,data):
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            data.keysPressed.add("up")
        if event.key == pygame.K_DOWN:
            data.keysPressed.add("down")
        if event.key == pygame.K_LEFT:
            data.keysPressed.add("left")
        if event.key == pygame.K_RIGHT:
            data.keysPressed.add("right")
def handleMovement(event,data):
    if "up" in data.keysPressed:
        dir = (0,1)
    if "down" in data.keysPressed:
        dir = (0,-1)
    if "left" in data.keysPressed:
        dir = (-1,0)
    if "right" in data.keysPressed:
        dir = (1,0)
    
main()
=======
            handle(event)

    pygame.quit()

def handle(event):
    if event.type == pygame.QUIT:
        running = False

main()
>>>>>>> 1c2f90342533fb7547428c64fc08e07d12c32771
