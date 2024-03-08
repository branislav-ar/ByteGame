import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move

class Main:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("ByteGame")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game = Game()

        # self.game_state = None

    def mainloop(self):

        screen = self.screen
        game = self.game
        dragger = self.game.dragger
        board = self.game.board

        while True:
            
            # show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_hover(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)
            
            game.validate_end_game()
            if game.game_over:
                game.display_end_message(screen)

            for event in pygame.event.get():
                
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE                    
                    
                    # Regulacija selekcije elemenata u okviru jednog steka
                    if (board.squares[clicked_row][clicked_col].is_valid_square()):
                        
                        initial_stack = board.squares[clicked_row][clicked_col].pieces_on_square
                        
                        # initial_stack ima 1 el. - ne moramo da brinemo o granicama na kvadratu!
                        if(len(initial_stack) == 1):
                            print("Pomera se <stack[0]> figura!")
                            piece = board.squares[clicked_row][clicked_col].pieces_on_square[0]
                        
                        # initial_stack ima 2 el.
                        elif(len(initial_stack) == 2):
                            # stack_to_move pocinje od el. 0
                            if(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 4))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 11))):
                                    print("Pomera se <stack[0]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[0]
                            # stack_to_move pocinje od el. 1
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 11))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 19))):
                                    print("Pomera se <stack[1]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[1]
                        
                        # initial_stack ima 3 el.
                        elif(len(initial_stack) == 3):
                            # stack_to_move pocinje od el. 0
                            if(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 4))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 11))):
                                    print("Pomera se <stack[0]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[0]
                            # stack_to_move pocinje od el. 1
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 11))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 19))):
                                    print("Pomera se <stack[1]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[1]
                            # stack_to_move pocinje od el. 2
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 19))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 27))):
                                    print("Pomera se <stack[2]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[2]
                        
                        # initial_stack ima 4 el.
                        elif(len(initial_stack) == 4):
                            # stack_to_move pocinje od el. 0
                            if(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 4))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 11))):
                                    print("Pomera se <stack[0]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[0]
                            # stack_to_move pocinje od el. 1
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 11))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 19))):
                                    print("Pomera se <stack[1]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[1]
                            # stack_to_move pocinje od el. 2
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 19))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 27))):
                                    print("Pomera se <stack[2]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[2]
                            # stack_to_move pocinje od el. 3
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 27))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 34))):
                                    print("Pomera se <stack[3]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[3]
                        
                        # initial_stack ima 5 el.
                        elif(len(initial_stack) == 5):
                            # stack_to_move pocinje od el. 0
                            if(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 4))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 11))):
                                    print("Pomera se <stack[0]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[0]
                            # stack_to_move pocinje od el. 1
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 11))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 19))):
                                    print("Pomera se <stack[1]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[1]
                            # stack_to_move pocinje od el. 2
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 19))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 27))):
                                    print("Pomera se <stack[2]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[2]
                            # stack_to_move pocinje od el. 3
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 27))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 34))):
                                    print("Pomera se <stack[3]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[3]
                            # stack_to_move pocinje od el. 4
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 34))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 42))):
                                    print("Pomera se <stack[4]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[4]

                        # initial_stack ima 6 el.
                        elif(len(initial_stack) == 6):
                            # stack_to_move pocinje od el. 0
                            if(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 4))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 11))):
                                    print("Pomera se <stack[0]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[0]
                            # stack_to_move pocinje od el. 1
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 11))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 19))):
                                    print("Pomera se <stack[1]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[1]
                            # stack_to_move pocinje od el. 2
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 19))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 27))):
                                    print("Pomera se <stack[2]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[2]
                            # stack_to_move pocinje od el. 3
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 27))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 34))):
                                    print("Pomera se <stack[3]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[3]
                            # stack_to_move pocinje od el. 4
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 34))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 42))):
                                    print("Pomera se <stack[4]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[4]
                            # stack_to_move pocinje od el. 5
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 42))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 50))):
                                    print("Pomera se <stack[5]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[5]
                            
                        # initial_stack ima 7 el.
                        elif(len(initial_stack) == 7):
                            # stack_to_move pocinje od el. 0
                            if(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 4))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 11))):
                                    print("Pomera se <stack[0]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[0]
                            # stack_to_move pocinje od el. 1
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 11))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 19))):
                                    print("Pomera se <stack[1]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[1]
                            # stack_to_move pocinje od el. 2
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 19))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 27))):
                                    print("Pomera se <stack[2]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[2]
                            # stack_to_move pocinje od el. 3
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 27))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 34))):
                                    print("Pomera se <stack[3]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[3]
                            # stack_to_move pocinje od el. 4
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 34))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 42))):
                                    print("Pomera se <stack[4]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[4]
                            # stack_to_move pocinje od el. 5
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 42))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 50))):
                                    print("Pomera se <stack[5]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[5]
                            # stack_to_move pocinje od el. 6
                            elif(dragger.mouseX > (clicked_col * SQSIZE + SQSIZE // 5) 
                                and dragger.mouseX < (clicked_col * SQSIZE + 4*(SQSIZE // 5))
                                and dragger.mouseY < (clicked_row * SQSIZE + (SQSIZE - 50))
                                and dragger.mouseY > (clicked_row * SQSIZE + (SQSIZE - 58))):
                                    print("Pomera se <stack[6]> figura!")
                                    piece = board.squares[clicked_row][clicked_col].pieces_on_square[6]
                                    
                        # Provera "Ko je na potezu?"
                        # BY DEFAULT: WHITE GOES FIRST
                        if piece.color == game.next_player:
                        
                            # Odredjivanje pieces_to_be_moved
                            current_piece_index = -1
                            
                            for single_piece in initial_stack:
                                current_piece_index = current_piece_index + 1
                                if single_piece is piece:
                                    pieces_to_be_moved = board.squares[clicked_row][clicked_col].pieces_on_square[current_piece_index:]
                            
                            board.calc_moves(piece, clicked_row, clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(pieces_to_be_moved)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                
                # mouse movement
                elif event.type == pygame.MOUSEMOTION:
                    
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE
                    
                    game.set_hover(motion_row, motion_col)
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_hover(screen)
                        game.show_pieces(screen)
                        
                        dragger.update_blit(screen)
                
                # click realease
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        
                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE
                        
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)
                        
                        # Da li je potez validan? DA - pomeranje u memoriji!
                        if board.valid_move(dragger.pieces[0], move):
                              
                            board.move(dragger.pieces[0], move)
                            
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            
                            # next turn
                            game.next_turn()
                    
                    dragger.undrag_piece()
                    
                    color_returned = board.check_for_points()
                    
                    if color_returned == "white":
                        self.game.P1_points = self.game.P1_points + 1
                    elif color_returned == "black":
                        self.game.P2_points = self.game.P2_points + 1
                    else:
                        print("No new points.")
                    
                    print(" - - - - start - - - - ")
                    for row in range(ROWS):
                        print(" - - - - ROW", row+1, "- - - - ")
                        for col in range(COLS):
                            stack = self.game.board.squares[row][col].pieces_on_square
                            i = 0
                            for piece in stack:
                                print(row, col, piece.color, i)
                                i = i + 1
                    print(" - - - - stop - - - - ")
                    
                    
                    print("P1 (white): ", self.game.P1_points, " P2 (black): ", self.game.P2_points)
                    print("TURN PLAYER: ", self.game.next_player)
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        dragger = self.game.dragger
                        board = self.game.board
                
                # quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()    

main = Main()
main.mainloop()