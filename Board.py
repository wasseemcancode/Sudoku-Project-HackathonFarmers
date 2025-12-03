import pygame
import sys
import random 
from sudoku_generator import * 
from Cell import * 



class Board:

    def __init__(self, width, height, screen, difficulty):

        self.width = width
        self.height = height 
        self.screen = screen
        self.difficulty = difficulty 

        self.board_size = 540
        self.cell_size = 60

        removed_squares = 0 
        if difficulty == "easy":
            removed_squares = 30
        elif difficulty == "medium":
            removed_squares = 40
        else:
            removed_squares = 50

        self.sudoku = SudokuGenerator(self.width, removed_squares)
        self.sudoku.fill_values()
        self.solution = [row[:] for row in self.sudoku.get_board()]

        self.sudoku.print_board()

        self.sudoku.remove_cells()

        self.my_Board = self.sudoku.get_board()

        self.original_board = [row[:] for row in self.my_Board]

        self.cells = [
            [Cell(self.my_Board[row][col], row, col, screen) 
             for col in range(self.width)]
            for row in range(self.height)
        ]

        self.selected_row = None
        self.selected_col = None

    def draw(self):
        x_offset = 30
        y_offset = 30
        for row in range(self.height):
            for col in range(self.width):
                self.cells[row][col].draw(self.screen)


        for i in range(self.width + 1):
            thickness = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0,0,0), (i * self.cell_size + x_offset, 0 + y_offset), (i * self.cell_size + x_offset, self.board_size + y_offset), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0 + x_offset, i * self.cell_size + y_offset), (self.board_size + x_offset, i * self.cell_size + y_offset), thickness)

    def select(self, row, col):
        for i in range(self.height):
            for j in range(self.width):
                self.cells[i][j].selected = False

        self.cells[row][col].selected = True
        self.selected_row = row
        self.selected_col = col

    def click(self, x, y):
        x_offset = 30
        y_offset = 30
        if x_offset < x < (self.board_size + x_offset) and y_offset < y < (self.board_size + y_offset):
            col = (x - x_offset) // self.cell_size
            row = (y - y_offset) // self.cell_size
            return (row, col)
        return None            

    def clear(self):
        if self.selected_row is not None and self.selected_col is not None:
            self.cells[self.selected_row][self.selected_col].set_cell_value(0)
            self.cells[self.selected_row][self.selected_col].set_sketched_value(0)
            self.my_Board[self.selected_row][self.selected_col] = 0

    def sketch(self, value):
        if self.selected_row is not None and self.selected_col is not None:
            if self.original_board[self.selected_row][self.selected_col] == 0:
                self.cells[self.selected_row][self.selected_col].set_sketched_value(value)

    def place_number(self, value):
        if self.selected_row is not None and self.selected_col is not None:
            if self.original_board[self.selected_row][self.selected_col] == 0:
                self.cells[self.selected_row][self.selected_col].set_cell_value(value)
                self.my_Board[self.selected_row][self.selected_col] = value

                if value == self.solution[self.selected_row][self.selected_col]:
                    self.cells[self.selected_row][self.selected_col].color = (0, 155, 0)
                else:
                    self.cells[self.selected_row][self.selected_col].color = (200, 0, 0)

    def reset_to_original(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.original_board[row][col] == 0:
                    self.cells[row][col].set_cell_value(0)
                    self.cells[row][col].set_sketched_value(0)
                    self.cells[row][col].color = (0,0,0)
                    self.my_Board[row][col] = 0
        
    def is_full(self):
        for row in range(self.height):
            for col in range(self.width):
                cell = self.cells[row][col]
                if cell.value == 0 and cell.sketched_value == 0:
                    return False
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
        for i in range(self.height):
            for j in range(self.width):
                cell = self.cells[i][j]
                cell_value = cell.value if cell.value != 0 else cell.sketched_value
                if cell_value != self.solution[i][j]:
                    return False
        return True