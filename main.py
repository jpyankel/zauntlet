# Main game loop
import pygame, socket, math, argparse
from src.gamedata import GameData

def main ():
    pygame.init()
    clock = pygame.time.Clock()
    data = GameData()
    screen = pygame.display.set_mode((data.window.width, data.window.height))
    running = True
    while running:
        time = clock.tick(60) #similar to timerDelay
        screen.fill((255,0,0))
        for event in pygame.event.get():
            handle(event)
    pygame.quit()

def handle(event):
    if event.type == pygame.QUIT:
        running = False

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Run Zauntlet with parameters.")
    parser.add_argument("--hostIP", action="store", dest="hostIP",
                        help="The host IP to connect to")
    argsList = parser.parse_args() # Get list of arguments
    main()
