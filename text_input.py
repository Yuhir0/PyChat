import sys

import pygame
from pygame.rect import Rect
import pygame.locals as pg_locals

from function import process_text


class TextInput:
    def __init__(self):
        self.__characters = list()
        self.__error_time = int()
        self.__text = str()
        self.__error = "Incorrect character"

    def read(self):
        for event in pygame.event.get():
            if event.type == pg_locals.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                print('event.type == pygame.KEYDOWN')
                if event.key == pygame.K_BACKSPACE and len(self.__characters) > 0:
                    self.__characters = self.__characters[0:-1]
                    print('event.key == pygame.K_BACKSPACE')
                else:
                    print('else')
                    try:
                        self.__characters += str(event.unicode)
                    except:
                        self.__error_time = 90

        self.write()
        print(self.__text)

    def write(self):
        self.__text = str()
        for i in self.__characters:
            self.__text += i

    def clear_input(self):
        self.__text = str()

    def get_text(self, posx: int, posy: int, **kwargs) -> (pygame.Surface, Rect):
        return process_text(self.__text, posx, posy, **kwargs)

    def show_errors(self, SCREEN, posx: int, posy: int, **kwargs):
        if self.__error_time > 0:
            error, error_rect = process_text(self.__error, posx, posy, **kwargs)
            SCREEN.blit(error, error_rect)
            self.error_tim -= 1
