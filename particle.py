import random
import pygame


class Particle:
    def __init__(self, pos, color, surface):
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.alive = True
        self.drift = True
        self.surface = surface

    def fall(self):
        # fall
        if (self.y + 1 < self.surface.get_height() and  # in bounds
            self.surface.get_at((self.x, self.y + 1)) == (0,0,0,255)):  # alpha
            self.y += 1

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
