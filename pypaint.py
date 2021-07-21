import math

import pygame


DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
DEFAULT_SIZE = (DEFAULT_WIDTH, DEFAULT_HEIGHT)

FPS = 60


class Pen:
    def __init__(self, color=(0, 0, 0), pos=(0, 0), width=1):
        self.pos = pygame.Vector2(pos)
        self.color = pygame.Color(color)
        self.width = width
        self.down = False


def draw_line(surface, start_pos, end_pos, color, width=1):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    distance = max(abs(dx), abs(dy))
    for pixel in range(distance):
        x = start_pos[0] + pixel/distance*dx
        y = start_pos[1] + pixel/distance*dy
        pygame.draw.circle(surface, color, (x, y), math.ceil(width / 2))


def draw_points(surface, points, color, width=1):
    for j, point in enumerate(points):
        if j < 1:
            pygame.draw.circle(surface, color, point, math.ceil(width / 2))
            continue
        draw_line(surface, points[j - 1], point, color)


def get_delta_time(ms_last_frame):
    return round(ms_last_frame / 1000 * 60)


def main():
    screen = pygame.display.set_mode(DEFAULT_SIZE)
    clock = pygame.time.Clock()
    pen = Pen()
    lines = []
    lines_info = []

    while True:
        ms = clock.tick(FPS)
        dt = get_delta_time(ms)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button != 2:
                    lines.append([])
                    lines_info.append({'color': pen.color})
                    pen.down = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button != 2:
                    pen.down = False
        if pen.down:
            point = pygame.mouse.get_pos()
            if point not in lines[-1]:
                lines[-1].append(point)
        screen.fill('white')
        for i, line in enumerate(lines):
            draw_points(screen, line, lines_info[i]['color'])
        pygame.display.update()


if __name__ == '__main__':
    main()

pygame.quit()