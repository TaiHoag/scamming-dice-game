import pygame
from Constants import *


def draw_text(surf, text, pos, color=WHITE, font_size=FONT_SIZE):
    """Draw text on the screen."""
    font = FONT
    text_surf = font.render(str(text), True, color)
    text_rect = text_surf.get_rect(center=pos)
    surf.blit(text_surf, text_rect)
