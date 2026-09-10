import pygame
import constants
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")


if __name__ == "__main__":
    main()
