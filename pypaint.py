import math

import pygame


DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
DEFAULT_SIZE = (DEFAULT_WIDTH, DEFAULT_HEIGHT)

FPS = 60


def draw_line(surface, start_pos, end_pos, color, width=1):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    distance = max(abs(dx), abs(dy))
    for pixel in range(distance):
        x = start_pos[0] + pixel/distance*dx
        y = start_pos[1] + pixel/distance*dy
        pygame.draw.circle(surface, color, (x, y), math.ceil(width / 2))


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