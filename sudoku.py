import pygame
import sys
from sudoku_generator import * 
from Board import Board

def main():
        
        pygame.init()

        screen = pygame.display.set_mode((600, 700))
        pygame.display.set_caption("Hackathon Farmer Sudoku")

        buttonFont = pygame.font.Font(None, 40)

        difficulty = None
        board = None
        gameState = 'menu'
        statusMessage = ''
        gameRunning = True

        while gameRunning:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameRunning = False
                    sys.exit()

                if gameState == 'menu':
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        x, y = event.pos
                        easyButton = pygame.Rect(200, 220, 200, 60)
                        mediumButton = pygame.Rect(200, 300, 200, 60)
                        hardButton = pygame.Rect(200, 380, 200, 60)

                        if easyButton.collidepoint(x, y):
                            difficulty = 'easy'
                            board = Board(9, 9, screen, difficulty)
                            statusMessage = ''
                            gameState = 'gaming'

                        elif mediumButton.collidepoint(x, y):
                            difficulty = 'medium'
                            board = Board(9, 9, screen, difficulty)
                            statusMessage = ''
                            gameState = 'gaming'

                        elif hardButton.collidepoint(x, y):
                            difficulty = 'hard'
                            board = Board(9, 9, screen, difficulty)
                            statusMessage = ''
                            gameState = 'gaming'

                elif gameState == 'gaming':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        resetButton = pygame.Rect(20, 620, 120, 60)
                        restartButton = pygame.Rect(160, 620, 120, 60)
                        checkButton = pygame.Rect(300, 620, 120, 60)
                        exitButton = pygame.Rect(440, 620, 120, 60)

                        if resetButton.collidepoint(x, y):

                            board.reset_to_original()

                        elif restartButton.collidepoint(x, y):
                            gameState = 'menu'
                            statusMessage = ''

                        elif checkButton.collidepoint(x, y):
                            try:
                                if board.is_full():
                                    if board.check_board():
                                        gameState = 'won'
                                    else:
                                        gameState = 'lost'
                                else:
                                    statusMessage = 'Board not complete!'
                            except Exception:
                                statusMessage = 'Error try again'

                        elif exitButton.collidepoint(x, y):
                            pygame.quit()
                            sys.exit()
                        else:
                            if y < 600:
                                clicked_cell = board.click(x, y)
                                if clicked_cell:
                                    board.select(clicked_cell[0], clicked_cell[1])
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
                        if event.key == pygame.K_RETURN:
                            cell = board.cells[board.selected_row][board.selected_col]
                            if cell.sketched_value != 0:
                                board.place_number(cell.sketched_value)

                elif gameState == 'won':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        exitButton = pygame.Rect(240, 400, 120, 60)
                        if exitButton.collidepoint(x, y):
                            pygame.quit()
                            sys.exit()

                elif gameState == 'lost':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        restartButton = pygame.Rect(240, 400, 120, 60)
                        if restartButton.collidepoint(x, y):
                            gameState = 'menu'
                            statusMessage = ''

            screen.fill((255,255,255))

            if gameState == 'menu':

                title = buttonFont.render('Sudoku', True, (0,0,0))
                screen.blit(title, (250, 120))
                easyButton = pygame.Rect(200, 220, 200, 60)
                pygame.draw.rect(screen, (200,200,200), easyButton)
                easy_text = buttonFont.render('Easy', True, (0,0,0))
                screen.blit(easy_text, (easyButton.x + 70, easyButton.y + 12))
                mediumButton = pygame.Rect(200, 300, 200, 60)
                pygame.draw.rect(screen, (200,200,200), mediumButton)
                medium_text = buttonFont.render('Medium', True, (0,0,0))
                screen.blit(medium_text, (mediumButton.x + 55, mediumButton.y + 12))
                hardButton = pygame.Rect(200, 380, 200, 60)
                pygame.draw.rect(screen, (200,200,200), hardButton)
                hard_text = buttonFont.render('Hard', True, (0,0,0))
                screen.blit(hard_text, (hardButton.x + 75, hardButton.y + 12))

            elif gameState == 'gaming':

                board.draw()
                resetButton = pygame.Rect(20, 620, 120, 60)
                pygame.draw.rect(screen, (150,150,150), resetButton)
                reset_text = buttonFont.render('Reset', True, (0,0,0))
                screen.blit(reset_text, (resetButton.x + 25, resetButton.y + 15))
                restartButton = pygame.Rect(160, 620, 120, 60)
                pygame.draw.rect(screen, (150,150,150), restartButton)
                restart_text = buttonFont.render('Restart', True, (0,0,0))
                screen.blit(restart_text, (restartButton.x + 15, restartButton.y + 15))
                checkButton = pygame.Rect(300, 620, 120, 60)
                pygame.draw.rect(screen, (150,150,150), checkButton)
                check_text = buttonFont.render('Check', True, (0,0,0))
                screen.blit(check_text, (checkButton.x + 25, checkButton.y + 15))
                exitButton = pygame.Rect(440, 620, 120, 60)
                pygame.draw.rect(screen, (150,150,150), exitButton)
                exit_text = buttonFont.render('Exit', True, (0,0,0))
                screen.blit(exit_text, (exitButton.x + 35, exitButton.y + 15))

                if statusMessage:
                    msg = buttonFont.render(statusMessage, True, (0,150,0) if 'Victory' in statusMessage else (150,0,0))
                    screen.blit(msg, (220, 500))

            elif gameState == 'won':
                title = buttonFont.render('Game Won!', True, (0, 150, 0))
                screen.blit(title, (230, 300))
                exitButton = pygame.Rect(240, 400, 120, 60)
                pygame.draw.rect(screen, (150,150,150), exitButton)
                exit_text = buttonFont.render('Exit', True, (0,0,0))
                screen.blit(exit_text, (exitButton.x + 35, exitButton.y + 15))

            elif gameState == 'lost':
                title = buttonFont.render('Game Over :(', True, (150, 0, 0))
                screen.blit(title, (220, 300))
                restartButton = pygame.Rect(240, 400, 120, 60)
                pygame.draw.rect(screen, (150,150,150), restartButton)
                restart_text = buttonFont.render('Restart', True, (0,0,0))
                screen.blit(restart_text, (restartButton.x + 15, restartButton.y + 15))

            pygame.display.flip()


if __name__ == "__main__":
    main()
