import pygame
import random 
from sudoku_generator import * 




class Cell:

    def __init__(self, value, row, col, screen):

        self.value = value

        self.row = row

        self.col = col

        self.screen = screen


    def set_cell_value(self, value):

        if not self.filled:

            self.value = value


    def set_sketched_value(self, value):

        self.sketched_value = value 


    def draw(self, surface):

        rect = pygame.Rect(self.value, self.row, self.col)

        pygame.draw.rect(surface, (255, 255, 255), rect)

        border_color = (255,0,0)

        pygame.draw.rect(surface, border_color, rect, 2)


        if self.value != 0:

            font = pygame.font.Font(None, self.size - 10)

            text = font.render(str(self.value), True, (0,0,0))

            text_rect = text.get_rect(center = rect.center)

            surface.blit((text, text_rect))


