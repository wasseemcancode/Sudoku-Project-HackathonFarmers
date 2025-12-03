import pygame
from sudoku_generator import * 




class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.color = (0, 0, 0)


    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value 
    

    def draw(self, surface):
        # Making size of cells match with the size of the window
        x_offset = 30
        y_offset = 30
        cell_size = 60
        x = (self.col * cell_size) + x_offset
        y = (self.row * cell_size) + y_offset

        # Creating cell
        rect = pygame.Rect(x, y, cell_size, cell_size)

        # Draw the main number in solid black
        if self.value != 0:
            font = pygame.font.Font(None, 40)
            text = font.render(str(self.value), True, self.color)
            text_rect = text.get_rect(center = rect.center)
            surface.blit(text, text_rect)

        # IF main value is zero, draw the sketched value in gray
        elif self.sketched_value != 0:
            font = pygame.font.Font(None, 40)
            text = font.render(str(self.sketched_value), True, (128,128,128))
            text_rect = text.get_rect(center = rect.center)
            surface.blit(text, text_rect)

        # Draw red if selected
        if self.selected:
            pygame.draw.rect(surface, (250,0,0), rect, 3)


