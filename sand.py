import random
import sys
import time
import pygame
from pygame.locals import *
from point import Point
from particle import Particle

# YAY! MUCHOS COLOROS!!!
RED = (255,0,0)
ORANGE = (255,96,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
CYAN = (255,255,0)
TURQUIOSE = (0,0x60,0x80)
BLUE = (0,0,255)
DARK_BLUE = (0,0,128)
MAGENTA = (169,0,255)
PINK = (255,200,200)
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (64,64,64)
LIGHT_GRAY = (128,128,128)
COLORS = RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, MAGENTA, PINK
SAND_COLORS = RED, GREEN, BLUE, MAGENTA, CYAN
SAND_COLOR = GREEN
WALL_COLOR = TURQUIOSE
BG_COLOR = BLACK

width, height = 400, 400


def game():
    pygame.init()
    screen = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF)
    # screen.fill(DARK_BLUE)
    # pygame.draw.rect(screen, white, (200, 150, 400, 270), 1)
    # pygame.draw.circle(screen, red, (int(width/2), int(height/2)), 80, 3)
    pygame.display.update()

    sands = []  # list of Particle objects
    walls = [[]]  # 2D array, each element is a list of (x, y) wall coordinates
    wall_num = 0
    wall_pos = Point(0, 200)  # middle of left edge
    velocity = Point(5, 0)  # to the right
    drawing = False
    color = BLUE

    for iteration in range(1000000):
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif drawing:
                mouse_pos = pygame.mouse.get_pos()
                # if color == WALL_COLOR:
                #     wall = pygame.draw.circle(screen, WALL_COLOR, mouse_pos, 10)
                #     walls.append(wall)
                # else:
                sands.append(Particle(mouse_pos, color, screen))
            # keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    color = random.choice(SAND_COLORS)
                if event.key == pygame.K_LEFT:
                    color = SAND_COLOR if color == WALL_COLOR else WALL_COLOR

        # generate some walls
        max_dy = 2
        # wall_num, remainder = divmod(iteration, 2)
        # wall_num = int(iteration / (width * max_dy * 2))
        if iteration % 1 == 0 and wall_num < 40:  # 10 walls
            x, y = wall_pos
            if x >= width:  # hit the right screen boundary
                # print(walls[wall_num])
                print("NEW WALL")
                # new wall!
                walls.append([])
                wall_num += 1
                x = x % width  # reset to left boundary (similar to x = 0)
                y = random.randint(100, height)  # skip top 100 of left edge
                wall_pos = Point(x, y)
                velocity = Point(5, 0)  # to the right

            delta = Point(0, random.randint(-max_dy, max_dy))
            velocity = ((velocity + delta) / velocity.norm()) * 5
            wall_pos = wall_pos + velocity.intify()
            # print(velocity)
            wall_rect = pygame.draw.circle(screen, WALL_COLOR, wall_pos.coords, 10)
            # points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height),
            #           (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
            # pygame.draw.lines(screen, color, False, points, lineThickness)
            walls[wall_num].append(wall_pos)

        # randomly generate sand
        for _ in range(10):
            random_x = random.randint(0, width)  # - int(width/2)
            random_y = random.randint(0, height)  # - int(height/2)
            sands.append(Particle((random_x, random_y), color, screen))

        # background
        screen.fill(BG_COLOR)
        # draw the walls
        for wall in walls:  # each wall is a list of (x, y) wall coordinates
            # pygame.draw.circle(screen, WALL_COLOR, wall.center, 5)
            if len(wall) > 1:
                # pygame.draw.lines(screen, color, closed, pointlist, thickness)
                wall_coords = [point.coords for point in wall]
                pygame.draw.lines(screen, WALL_COLOR, False, wall_coords, 4)

        # loop all the sands!
        for sand in sands:
            sand.fall()
            sand.draw()
            # he's about to kick the sand bucket
            if sand.y + 2 > height:
                sand.alive = False

        # remove all the dead sands
        sands = list(filter(lambda p: p.alive, sands))

        # make it show! –Captain Kirk
        pygame.display.flip()


if __name__ == '__main__':
    print('all your sand are belong to us')
    game()
