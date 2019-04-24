import pygame
from pygame.rect import Rect

import const


def process_text(text: str, posx: int, posy: int, **kwargs) -> (pygame.Surface, Rect):
    color = kwargs.get('color', const.Color.BLACK)
    size = kwargs.get('size', 25)
    font_name = kwargs.get('font', 'arial')
    font = pygame.font.SysFont(font_name, size)
    res = font.render(text, True, color)
    res_rect = res.get_rect()
    res_rect.centerx = posx
    res_rect.centery = posy
    return res, res_rect
