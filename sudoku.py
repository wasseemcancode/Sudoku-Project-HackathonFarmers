
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

        self.value = value


    def set_sketched_value(self, value):

        self.value = value 


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
