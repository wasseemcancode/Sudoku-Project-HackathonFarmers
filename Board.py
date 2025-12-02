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


        def draw():
            pygame.init()
            size = 600
            height = 700
            screen = pygame.display.set_mode((size, height))
            pygame.display.set_caption("Sudoku UI")

            grid_size = 9
            cell_size = size // grid_size

            button_font = pygame.font.SysFont(None, 36)

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