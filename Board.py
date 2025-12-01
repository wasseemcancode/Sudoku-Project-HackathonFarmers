import pygame
import random 
from sudoku_generator import * 
from Cell import * 



class Board:

    def __init__(self, width, height, screen, difficulty):

        self.width = width

        self.height = height 

        self.screen = screen

        self.difficulty = difficulty 

        self.cells = []

        self.selected_row = None

        self.selected_col = None

        removed_squares = 0 

        if difficulty == "easy":

            removed_squares = 10

        elif difficulty == "medium":

            removed_squares = 20

        else:
            
            removed_squares = 30 

        sudoku = SudokuGenerator(self.width, removed_squares)

        sudoku.fill_values()


   


        sudoku.remove_cells()

        my_Board = sudoku.get_board()


        for row in range(self.width):

            for col in range(self.height):

                cell_value = my_Board[row][col] 

                self.cells[row][col] = Cell(cell_value, row, col, screen)


        def draw(self):

            pass


        def select(self, row, col):
            
            self.select_row = row

            self.select_col = col



            

        def click(self, x, y):

            pass

        def clear(self):

            pass

        def sketch(self, value):

            pass


        def place_number(self, value):

            if self.selected_row is not None and self.selected_col is not None:

                my_Board[self.selected_row][self.selected_col] = value



        def reset_to_original(self):

            pass

        def is_full(self):

            for row in range(self.width):

                for col in range(self.height):

                    if my_Board[col][row] == "0":

                        return False
                    
            else:

                return True 

        def update_board(self):

            pass

        def find_empty(self):

            for row in range(self.width):

                for col in range(self.height):

                    if my_Board[col][row] == "0":

                        return (col, row)

        def check_board(self):

            if is_full == True:

                return True
            
            else:

                return False