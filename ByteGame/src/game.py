import pygame
import sys
from const import *
from board import Board
from square import Square
from dragger import Dragger

class Game:
    
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.next_player = 'white'
        self.hovered_sqr = None
        self.P1_points = 0
        self.P2_points = 0
        self.winning_message = "Prazna tabla."
        self.game_over = False

    # Crtanje table
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # Crtanje polja
                color = (240,208,160) if (row + col) % 2 == 0 else (172,114,72)
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

                # Ispisivanje koordinata
                # Brojevi
                if col == 0:
                    color = (240, 208, 160) if row % 2 == 1 else (172,114,72)
                    lbl = pygame.font.SysFont('monospace', 15, bold=True).render(str(ROWS-row), 1, color)
                    lbl_pos = (5, 5 + row * SQSIZE)
                    surface.blit(lbl, lbl_pos)

                # Slova
                if row == 7:
                    color = (240, 208, 160) if col % 2 == 0 else (172,114,72)
                    lbl = pygame.font.SysFont('monospace', 15, bold=True).render(Square.get_alphacol(col), 1, color)
                    lbl_pos = (col * SQSIZE + SQSIZE - 20, HEIGHT - 20)
                    surface.blit(lbl, lbl_pos)

    # Crtanje figura
    def show_pieces(self, surface):
        
        def draw_singular_stack_piece(piece, value):
            img = pygame.image.load(piece.texture)
            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + (value * SQSIZE)
            piece.texture_rect = img.get_rect(center = img_center)
            surface.blit(img, piece.texture_rect)
        
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].is_valid_square():
                    stack = self.board.squares[row][col].pieces_on_square

                    for piece in stack:
                        # blit sve osim dragging piece
                        # Kada se figura pomera nestaje sa inicijalne pozicije
                        # if piece is not self.dragger.pieces[0]:
                            # Ne remeti velicinu na inicijalnoj poziciji
                            # piece.set_texture(size=50)
                            if piece == stack[0]:
                                draw_singular_stack_piece(piece, 0.75)
                            elif piece == stack[1]:
                                draw_singular_stack_piece(piece, 0.65)
                            elif piece == stack[2]:
                                draw_singular_stack_piece(piece, 0.55)
                            elif piece == stack[3]:
                                draw_singular_stack_piece(piece, 0.45)
                            elif piece == stack[4]:
                                draw_singular_stack_piece(piece, 0.35)
                            elif piece == stack[5]:
                                draw_singular_stack_piece(piece, 0.25)
                            elif piece == stack[6]:
                                draw_singular_stack_piece(piece, 0.15)
                            elif piece == stack[7]:
                                draw_singular_stack_piece(piece, 0.05)
           
    
    def display_end_message(self, surface):
        while True:
            surface.fill((240, 208, 160))

            lbl = pygame.font.SysFont('monospace', 25, bold=True).render("Game over. " + self.winning_message, True, (172,114,72))
            center_me = lbl.get_rect(center=(HEIGHT // 2, WIDTH // 2))
            surface.blit(lbl, center_me)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def validate_end_game(self):
        empty_board = True
        # Prazna tabla kao uslov za Game over
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].is_valid_square():
                    empty_board = False
        self.game_over = True if empty_board == True else False

        # P1 pobeda kao uslov za Game over
        if self.P1_points >= STACKS_TO_WIN_GAME:
            self.winning_message = "White wins."
            self.game_over = True
        # P2 pobeda kao uslov za Game over
        elif self.P2_points >= STACKS_TO_WIN_GAME:
            self.winning_message = "Black wins."
            self.game_over = True
    
    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.pieces[0]
            
            # Svi validni potezi
            for move in piece.valid_moves:
                # color
                # ideas: #C86464 #C84646
                color = '#93C572' if (move.final.row + move.final.col) % 2 == 0 else '#93C572'
                # rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
    
    def show_last_move(self, surface):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            
            for pos in [initial, final]:
                # color
                color = (244, 247, 116) if (pos.row + pos.col) % 2 == 0 else (172, 195, 15)
                # rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
    
    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (255, 255, 255)
            # rect
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # blit
            pygame.draw.rect(surface, color, rect, width=2)
                
    
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'
        
    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]
        
    def reset(self):
        self.__init__()
                
                