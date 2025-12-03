import pygame
import sys
import random 
from sudoku_generator import * 
from Cell import * 



class Board:

    def __init__(self, width, height, screen, difficulty):

        # Classic instance variables
        self.width = width
        self.height = height 
        self.screen = screen
        self.difficulty = difficulty 

        # Define size of board (placeholder values)
        self.board_size = 600
        self.cell_size = self.board_size // 9




        # Determining how many cells to move
        removed_squares = 0 
        if difficulty == "easy":
            removed_squares = 30
        elif difficulty == "medium":
            removed_squares = 40
        else:
            removed_squares = 50

        # Backend Board
        self.sudoku = SudokuGenerator(self.width, removed_squares)
        self.sudoku.fill_values()
        self.sudoku.remove_cells()

        # Initializing the board that will be shown
        my_Board = sudoku.get_board()

        # Creating the cell objects
        for row in range(self.width):
            for col in range(self.height):
                cell_value = my_Board[row][col] 
                self.cells[row][col] = Cell(cell_value, row, col, screen)

        self.selected_row = None
        self.selected_col = None

    def draw(self):
        # Drawing cells
        for row in range(self.height):
            for col in range(self.width):
                self.cells[row][col].draw(self.screen)

        # Drawing grid lines
        for i in range(self.width + 1):
            pygame.draw_line(self.screen, (0, 0, 0), (i * self.cell_size, 0), (i* self.cell_size, self.board_size))
            pygame.draw_line(self.screen, (0, 0, 0), (0, i * self.cell_size), (self.board_size, i * self.cell_size))


        """pygame.init()
        size = 600
        height = 700
        screen = pygame.display.set_mode((size, height))
        pygame.display.set_caption("Sudoku UI")

        grid_size = 9
        cell_size = size // grid_size

        button_font = pygame.font.SysFont(None, 36)"""

    def draw_button(text, x, y, w, h):
            rect = pygame.Rect(x, y, w, h)
            pygame.draw.rect(screen, (200, 200, 200), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)
            label = button_font.render(text, True, (0, 0, 0))
            label_rect = label.get_rect(center=rect.center)
            screen.blit(label, label_rect)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                screen.fill((255, 255, 255))

                for i in range(grid_size + 1):
                    thickness = 1
                    if i % 3 == 0:
                        thickness = 4
                    pygame.draw.line(screen, (0, 0, 0), (0, i * cell_size), (size, i * cell_size), thickness)
                    pygame.draw.line(screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, size), thickness)

                btn_y = size + 40
                btn_w = 150
                btn_h = 50

    draw_button("Reset", 25, btn_y, btn_w, btn_h)
    draw_button("Restart", 225, btn_y, btn_w, btn_h)
    draw_button("Exit", 425, btn_y, btn_w, btn_h)

    pygame.display.flip()

    pygame.quit()
    sys.exit()

    def select(self, row, col):
        # Deselect all
        for i in range(self.height):
            for j in range(self.width):
                self.cells[r][c].selected = False

        # Select a new spot
        self.cells[row][col].selected = True
        self.select_row = row
        self.select_col = col

    def click(self, x, y):
        if x < self.board_size and y < self.board_size:
            col = x
            row = y
            return (row, col)
        return None            

    def clear(self):
        if self.selected_row is not None and self.selected_col is not None:
            self.cells[self.selected_row][self.selected_col].set_cell_value(0)
            self.cells[self.selected_row][self.selected_col].set_sketched_value(0)
            self.my_Board[self.selected_row][self.selected_col] = 0

    def sketch(self, value):
        if self.selected_row is not None and self.selected_col is not None:
            self.cells[self.selected_row][self.selected_col].set_sketched_value(value)

    def place_number(self, value):
        if self.selected_row is not None and self.selected_col is not None:
            self.cells[self.selected_row][selected_col].set_cell_value(value)
            self.my_Board[self.selected_row][self.selected_col] = value

    def reset_to_original(self):

        pass

    def is_full(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.my_Board[row][col] == 0:
                    return False
                else:
                    return True 

    def update_board(self):

        pass

    def find_empty(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.my_Board[row][col] == 0:
                    return (row, col)
                else:
                    return None

    def check_board(self):
        return self.is_full