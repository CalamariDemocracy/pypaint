import math

import pygame


DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
DEFAULT_SIZE = (DEFAULT_WIDTH, DEFAULT_HEIGHT)

FPS = 60


class Pen:
    """contains current drawing data"""
    def __init__(self, color=(0, 0, 0), pos=(0, 0), width=1):
        self.pos = pygame.Vector2(pos)
        self.color = pygame.Color(color)
        self.width = width
        self.down = False


def draw_line(surface, start_pos, end_pos, color, width=1):
    """draws circles pixel by pixel between two points to create a line"""
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    distance = max(abs(dx), abs(dy))
    for pixel in range(distance):
        x = start_pos[0] + pixel/distance*dx
        y = start_pos[1] + pixel/distance*dy
        pygame.draw.circle(surface, color, (x, y), math.ceil(width / 2))


def draw_points(surface, points, color, width=1):
    """draws lines between all given points
    
    Single point defaults to circle.
    """
    for j, point in enumerate(points):
        if j < 1:
            pygame.draw.circle(surface, color, point, math.ceil(width / 2))
            continue
        draw_line(surface, points[j - 1], point, color, width)


def get_delta_time(ms_last_frame):
    """calculate delta time based on milliseconds past"""
    return round(ms_last_frame / 1000 * 60)


def main():
    """initializes display and other resources, then handles game loop"""
    screen = pygame.display.set_mode(DEFAULT_SIZE)
    clock = pygame.time.Clock()
    pen = Pen()
    range_width = (1, 25)
    lines = []

    while True:
        ms = clock.tick(FPS)
        dt = get_delta_time(ms)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if pygame.key.get_mods() and pygame.KMOD_CTRL:
                        lines.clear()
                    elif lines:
                        lines.pop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button != 2:
                    lines.append({'color': pen.color, 'width': pen.width, 'points': []})
                    pen.down = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button != 2:
                    pen.down = False
            if event.type == pygame.MOUSEWHEEL:
                pen.width += -1 if event.y > 0 else 1
                if pen.width > max(range_width):
                    pen.width = max(range_width)
                if pen.width < min(range_width):
                    pen.width = min(range_width)
        if pen.down:
            point = pygame.mouse.get_pos()
            if point not in lines[-1]['points']:
                lines[-1]['points'].append(point)
        screen.fill('white')
        for i, line in enumerate(lines):
            draw_points(screen, line['points'], line['color'], line['width'])
        pygame.display.update()


if __name__ == '__main__':
    main()

pygame.quit()