import random
import pygame


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
MAGENTA = (169,0,255)
CYAN = (255,255,0)
SAND_COLORS = RED, GREEN, BLUE, MAGENTA
FALL_DIR = {RED: (0, -1), BLUE: (0, 1), GREEN: (1, 0), MAGENTA: (-1, 0), CYAN: (1, -1)}


class Particle:
    def __init__(self, pos, color, surface):
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.alive = True
        self.drift = True
        self.surface = surface

    def fall(self):
        # fall based on gravity direction of this particle's color
        dx, dy = FALL_DIR[self.color]
        x = self.x + dx
        y = self.y + dy
        if (0 < x < self.surface.get_width() and  # in bounds
            0 < y < self.surface.get_height() and  # in bounds
            self.surface.get_at((x, y)) == (0,0,0,255)):  # alpha
            self.x = x
            self.y = y

        # jiggle?
        if self.drift:
            # TODO: direction based on color
            # ...
            dx = random.choice((-2,-1,0,1,2))
            # would be outside of bounds
            if self.x + dx < 0 or self.x + dx >= self.surface.get_width():
                dx = -dx
            # do the jiggle
            if self.surface.get_at((self.x + dx, self.y)) == (0,0,0,255):
                self.x += dx

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), 1)
