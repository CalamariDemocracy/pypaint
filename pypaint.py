import pygame


DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
DEFAULT_SIZE = (DEFAULT_WIDTH, DEFAULT_HEIGHT)

FPS = 60


def main():
    screen = pygame.display.set_mode(DEFAULT_SIZE)
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == '__main__':
    main()

pygame.quit()