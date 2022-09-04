import pygame
from checkers.constants import RED, SQUARE_SIZE, WHITE, WIDTH, HEIGHT
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
  x, y = pos
  row = y // SQUARE_SIZE
  col = x // SQUARE_SIZE
  return row, col

def main():
  run = True
  clock = pygame.time.Clock()
  game = Game(WIN)

  while run:
    clock.tick(FPS)

    # if game.turn == WHITE:
    #   value, new_board = minimax(game.get_board(), 4, WHITE, game)
    #   game.ai_move(new_board)
    # elif game.turn == RED:
    #   value, new_board = minimax(game.get_board(), 3, False, game)
    #   game.ai_move(new_board)
    
    #pygame.time.delay(50)

    if game.winner() != None:
      game.update()
      print(game.winner())
      pygame.time.delay(2000)
      run = False
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        row, col = get_row_col_from_mouse(pos)
        game.select(row, col)

    game.update()

  pygame.quit()

main()