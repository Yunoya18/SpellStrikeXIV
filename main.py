from typing import Any
import pygame, sys

#from pygame.sprite import _Group
from level101 import *
from level import Level

#normal projectile ---not skill---
class magic_missle(pygame.sprite.Sprite):
    def __init__(self, player_pos_x, player_pos_y, speed) :
        super().__init__()
        self.image = pygame.surface((20,10))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect(center = (player_pos_x,player_pos_y))
        self.speed = speed

def create_magic_missle(x, y):
    return magic_missle(x +1, y)

def main():
    pygame.init()

    win = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()
    level = Level(level_map,win)
    pygame.display.set_caption("RSXIV")
    run = True

    # object
    width = 20

    # current cord
    x = 250
    y = 250
    vel = 5

    magic_missiles = pygame.sprite.Group()

    #SPEED
    speed = 10
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > width:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 500 - width:
            x += vel
        if keys[pygame.K_UP] and y > width:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - width:
            y += vel

        win.fill(('black'))
        level.run()
        pygame.draw.circle(win, (255, 0, 0), [x, y], width, 0)

        pygame.display.update()
        magic_missle.update(x)
        clock.tick(60)
    pygame.quit()

main()
