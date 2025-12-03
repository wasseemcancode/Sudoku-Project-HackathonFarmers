import pygame
from sudoku_generator import * 




class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.filled = False


    def set_cell_value(self, value):
        if not self.filled:
            self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value 
    

    def draw(self, surface):
        # Making size of cells match with the size of the window
        cell_size = 600 // 9
        x = self.col * cell_size
        y = self.row * cell_size

        # Creating cell
        rect = pygame.Rect(x, y, self.row, self.col)

        # Draw the main number in solid black
        if self.value != 0:
            font = pygame.font.Font(None, self.size - 10)
            text = font.render(str(self.value), True, (0,0,0))
            text_rect = text.get_rect(center = rect.center)
            surface.blit((text, text_rect))

        # IF main value is zero, draw the sketched value in gray
        elif self.sketched_value != 0:
            font = pygame.font.Font(None, 30)
            text = font.render(str(self.sketched_value), True, (128,128,128))
            surface.blit(text, (x+5, y+5))

        # Draw red if selected
        if self.selected:
            pygame.draw.rect(surface, (250,0,0), rect, 3)


