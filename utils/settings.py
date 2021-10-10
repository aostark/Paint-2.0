import pygame

pygame.init()
pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

fps = 120
width, height = 600, 700

rows = cols = 100
toolbar_height = height - width
pixel_size = width // cols
bg_color = white
draw_grid_lines = True


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
