
import pygame
import random 
import sys
from sudoku_generator import * 
from Board import Board

def main():
        # Initializes game
        pygame.init()

        screen = pygame.display.set_mode((600, 700))
        pygame.display.set_caption("Sudoku")

        button_font = pygame.font.Font(None, 40)

        difficulty = "easy"
        board = Board(9, 9, screen, difficulty)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos

                        if y < 600:
                            clicked_cell = board.click(x, y)
                            if clicked_cell:
                                board.select(clicked_cell[0], clicked_cell[1])
                        else:
                            if 50 <= x <= 200 and 620 <= y <= 680:
                                board.reset_to_original()

                            elif 250 <= x <= 400 and 620 <= y <= 680:
                                board = Board(9, 9, screen, difficulty)

                            elif 450 <= x <= 600 and 620 <= y <= 680:
                                pygame.quit()
                                sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if board.selected_row is not None and board.selected_col is not None:
                            if event.key == pygame.K_1:
                                board.sketch(1)
                            if event.key == pygame.K_2:
                                board.sketch(2)
                            if event.key == pygame.K_3:
                                board.sketch(3)
                            if event.key == pygame.K_4:
                                board.sketch(4)
                            if event.key == pygame.K_5:
                                board.sketch(5)
                            if event.key == pygame.K_6:
                                board.sketch(6)
                            if event.key == pygame.K_7:
                                board.sketch(7)
                            if event.key == pygame.K_8:
                                board.sketch(8)
                            if event.key == pygame.K_9:
                                board.sketch(9)

                    if event.type == pygame.K_RETURN:
                        cell = board.cells[board.selected_row][board.selected_col]
                        if cell.sketched_value != 0:
                            board.place_number(cell.sketched_value)

                        if board.is_full():
                            print("You won!")
                        else:
                            print("Game over! Incorrect")


            screen.fill((255,255,255))
            board.draw()

            # Reset Button
            reset_btn = pygame.Rect(50, 620, 150, 60)
            pygame.draw.rect(screen, (150, 150, 150), reset_btn)
            reset_text = button_font.render("Reset", True, (0, 0, 0))
            screen.blit(reset_text, (reset_btn.x + 35, reset_btn.y + 15))

            # Restart Button
            restart_btn = pygame.Rect(250, 620, 150, 60)
            pygame.draw.rect(screen, (150, 150, 150), restart_btn)
            restart_text = button_font.render("Restart", True, (0, 0, 0))
            screen.blit(restart_text, (restart_btn.x + 25, restart_btn.y + 15))

            # Exit Button
            exit_btn = pygame.Rect(450, 620, 100, 60) # Smaller to fit
            pygame.draw.rect(screen, (150, 150, 150), exit_btn)
            exit_text = button_font.render("Exit", True, (0, 0, 0))
            screen.blit(exit_text, (exit_btn.x + 20, exit_btn.y + 15))

            pygame.display.flip()


        sudoku = SudokuGenerator(9, 50)
        sudoku.fill_values()
        board = sudoku.get_board()
        sudoku.remove_cells()
        board = sudoku.get_board()
        sudoku.print_board()


if __name__ == "__main__":
    main()
    
   