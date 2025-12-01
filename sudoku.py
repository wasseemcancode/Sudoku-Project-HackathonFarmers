
import pygame
import random 
from sudoku_generator import SudokuGenerator




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

            pass
    

   


        




def main():
    try:
        pygame.init()

        sudoku = SudokuGenerator(9, 50)
        sudoku.fill_values()
        board = sudoku.get_board()
        sudoku.remove_cells()
        board = sudoku.get_board()
        sudoku.print_board()


        ### NOTE: this was taken from M13 in class activities and is helpful for seeing where the user clicked. 

        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("sudoku.jpg")
        screen = pygame.display.set_mode((480, 360))
        clock = pygame.time.Clock()
        mx, my = 0, 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = (event.pos)
                    if mx <= x < mx + (640/20) and my <= y < my + (640/20):
                        mx = random.randrange(0, 20) * (640/20)
                        my = random.randrange(0, 16) * (640/20)
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for x, y in zip([(640/20)*i for i in range(1, 20)], [(640/20)*i for i in range(1, 16)] + [-1]*4):
                pygame.draw.line(screen, 'black', (x, 0), (x, 512))
                pygame.draw.line(screen, 'black', (0, y), (640, y))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mx, my)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":


    main()
    
   