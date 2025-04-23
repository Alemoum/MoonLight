import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_control = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=000,rect=None,special_flags=0)
        pygame.display.flip()
        time_control.tick(60)
        dt = time_control.tick(60) / 1000
    # print("Starting Asteroids!")
    # print("Screen width: 1280")
    # print("Screen height: 720")
    
if __name__ == "__main__":
    main()