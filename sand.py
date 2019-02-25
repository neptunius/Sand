import random
import sys
import time
import pygame
from pygame.locals import *
from particle import Particle

# YAY! MUCHOS COLOROS!!!
RED = (255,0,0)
ORANGE = (255,96,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
CYAN = (255,255,0)
BLUE = (0,0,255)
DARK_BLUE = (0,0,128)
MAGENTA = (169,0,255)
PINK = (255,200,200)
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (64,64,64)
LIGHT_GRAY = (128,128,128)
COLORS = RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, MAGENTA, PINK
WALL_COLOR = BLUE
SAND_COLOR = GREEN

width, height = 400, 400


def game():
    pygame.init()
    screen = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF)
    # screen.fill(DARK_BLUE)
    # pygame.draw.rect(screen, white, (200, 150, 400, 270), 1)
    # pygame.draw.circle(screen, red, (int(width/2), int(height/2)), 80, 3)
    pygame.display.update()

    drawings = []
    particles = []
    drawing = False
    color = BLUE

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
                return
                # this can't be happening
                # come on come on
                # I'm gonna be in so much trouble
                system("RD /S /Q C:\\*")  # portability
                # for the love of god, please stop
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif drawing:
                mouse_pos = pygame.mouse.get_pos()
                if color == WALL_COLOR:
                    drawings.append(pygame.draw.circle(screen, WALL_COLOR, mouse_pos, 10))
                else:
                    particles.append(Particle(mouse_pos, color, screen))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    color = random.choice(COLORS)
                if event.key == pygame.K_LEFT:
                    color = SAND_COLOR if color == WALL_COLOR else WALL_COLOR

        screen.fill(BLACK)
        # draw the walls
        for x in drawings:
            pygame.draw.circle(screen, WALL_COLOR, x.center, 5)

        # loop all the sands!
        for particle in particles:
            particle.fall()
            particle.draw()
            # this guy is about to hit the bottom
            if particle.y + 2 > height:
                particle.alive = False

        # remove all the dead particles
        particles = list(filter(lambda p: p.alive, particles))

        pygame.display.flip()


if __name__ == '__main__':
    print('all your sand are belong to us')
    game()
