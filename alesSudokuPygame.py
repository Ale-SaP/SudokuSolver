import pygame
import pygame.freetype
import alesSudoku

pygame.init()
pygame.display.set_caption("Ale's Sudoku!")
sizeOfWindow = 1200
font = pygame.font.Font('freesansbold.ttf', 40)

sudoku = alesSudoku.sudoku
sudokuSolved = [alesSudoku.start(sudoku), alesSudoku.solved]

def grid(window, sizeOfWindow, rows):

    distance = 150
    pygame.draw.rect(window, (255, 255, 255),
                 [50, 50, 900, 900], 2)

    for number in range(9):
        pygame.draw.line(window, (255, 255, 255), (50, distance), (950, distance))
        pygame.draw.line(window, (255, 255, 255), (distance, 50), (distance, 950))
        distance += 100

def redraw(window):

    rows = 9
    window.fill((0,0,0))

    grid(window, (sizeOfWindow-200), rows)
    pygame.display.update()

def replace(window, board):
    y = 100
    for vert in range(9):
        x = 100
        for hor in range(9):
            if (board[vert][hor] != 0):
                text = font.render(f'{board[vert][hor]}', True, (0, 255, 0), (0,0,0))
                textRect = text.get_rect()
                textRect.center = (x, y)
                window.blit(text, textRect)
            x += 100
        y += 100

def main():
    window = pygame.display.set_mode((sizeOfWindow, sizeOfWindow))
    redraw(window)
    replace(window, sudokuSolved[1])
    while True:
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


main()