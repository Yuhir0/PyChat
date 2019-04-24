import sys

import pygame
import pygame.locals as pg_locals


def event_listener(event_list: list):
    for event in pygame.event.get():
        if event.type == pg_locals.QUIT:
            sys.exit(0)
