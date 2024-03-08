from const import *
from square import Square
from move import Move
from piece import *

class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.last_move = None
        self._create()
        # TEST: Prazna tabla.
        self._add_initial_stacks()
        
    def move(self, piece, move):
        initial = move.initial
        final = move.final
        
        # Uklanjanje figura iz initial stack prema indeksu u steku koji ima prosledjeni piece
        # Uklanja se piece[current_piece_index] i sve figure iznad nje
        current_piece_index = -1
        initial_stack = self.squares[initial.row][initial.col].pieces_on_square
        for single_piece in initial_stack:
            current_piece_index = current_piece_index + 1
            if single_piece is piece:
                # self.squares[initial.row][initial.col].pieces_on_square.pop(current_piece_index)
                pieces_to_be_moved = self.squares[initial.row][initial.col].pieces_on_square[current_piece_index:]
                self.squares[initial.row][initial.col].pieces_on_square = self.squares[initial.row][initial.col].pieces_on_square[:current_piece_index]
        
        # Dodavanje pieces_to_be_moved na final stack na vrh
        self.squares[final.row][final.col].pieces_on_square = self.squares[final.row][final.col].pieces_on_square + pieces_to_be_moved
        
        piece.moved = True
        piece.clear_moves()
        self.last_move = move
    
    def valid_move(self, piece, move):
        return move in piece.valid_moves
        
    def calc_moves(self, piece, row, col):
        ''' 
            Calculates all possible moves of a piece
        '''
        # 4 moves
        possible_moves = [
            (row-1, col-1), #GL
            (row-1, col+1), #GD
            (row+1, col-1), #DL
            (row+1, col+1)  #DD
        ]
        
        def calc_standard_moves():          
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    
                    # square za poteze
                    initial = Square(row, col)
                    final = Square(possible_move_row, possible_move_col)
                    # novi potez
                    move = Move(initial, final)
                    
                    
                    # Priprema za ostvarivanje USLOVA 2
                    pieces_on_final_square = self.squares[final.row][final.col].pieces_on_square
                    pieces_on_initial_square = self.squares[initial.row][initial.col].pieces_on_square
                    
                    current_piece_index = -1
                    pieces_on_initial_square = self.squares[initial.row][initial.col].pieces_on_square
                    for single_piece in pieces_on_initial_square:
                        current_piece_index = current_piece_index + 1
                        if single_piece is piece:
                            pieces_to_be_moved_LEN = len(self.squares[initial.row][initial.col].pieces_on_square[current_piece_index:])
                            
                    if( 
                        # fixes random missclicks
                        pieces_to_be_moved_LEN
                        
                        
                        # USLOV 1
                        # Ako ima figura na susednom steku polje je valid_move
                        and pieces_on_final_square
                        
                        
                        # USLOV 2
                        # Pomeranje na susedni stek moze da se obavi
                        # samo ako novodobijeni stek nakon pomeranja ima vise figura nego inicijalni stek                        
                        and (len(pieces_on_final_square)+pieces_to_be_moved_LEN) > len(pieces_on_initial_square)
                        
                        
                        # USLOV 3
                        # Pomeranje na susedni stek moze da se obavi samo ako
                        # novodobijeni stek ima osam ili manje figura
                        and (len(pieces_on_final_square)+pieces_to_be_moved_LEN) <= 8
                       ):
                        print("Possible move: ", move.final.row, move.final.col)
                        piece.add_move(move) 
        
        def calc_additional_moves():
            # Potez u slucaju da su sva susedna polja prazna
            print("Nema figura na susednim poljima!")
            # ...
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    
                    # square za poteze
                    initial = Square(row, col)
                    final = Square(possible_move_row, possible_move_col)
                    # novi potez
                    move = Move(initial, final)
                    
                    
                    # Priprema za ostvarivanje USLOVA 2
                    pieces_on_final_square = self.squares[final.row][final.col].pieces_on_square
                    pieces_on_initial_square = self.squares[initial.row][initial.col].pieces_on_square
                    
                    current_piece_index = -1
                    pieces_on_initial_square = self.squares[initial.row][initial.col].pieces_on_square
                    for single_piece in pieces_on_initial_square:
                        current_piece_index = current_piece_index + 1
                        if single_piece is piece:
                            pieces_to_be_moved_LEN = len(self.squares[initial.row][initial.col].pieces_on_square[current_piece_index:])

                    if( 
                        # fixes random missclicks
                        pieces_to_be_moved_LEN
                        
                        
                        # USLOV 1
                        # Ako ima figura na susednom steku polje je valid_move
                        and not pieces_on_final_square
                       ):
                        print("Possible move: ", move.final.row, move.final.col)
                        piece.add_move(move)
                      
        
        calc_standard_moves()
        
        if piece.valid_moves == []:
            calc_additional_moves() 

    def _create(self):        
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_initial_stacks(self):
        for row in range(ROWS):
            for col in range(COLS):
                if (row % 2 == 1) and (col % 2 == 1) and (row < ROWS - 1) and (row > 0):
                    self.squares[row][col].add_piece(Piece('black'))
                else:
                    if (row % 2 == 0) and (col % 2 == 0) and (row < ROWS - 1) and (row > 0):
                        self.squares[row][col].add_piece(Piece('white'))
    
    def check_for_points(self):
        print("checking for points...")
        for row in range(ROWS):
            for col in range(COLS):
                if (len(self.squares[row][col].pieces_on_square) >= 8):
                    stack = self.squares[row][col].pieces_on_square
                    for piece in stack:
                        color_of_top_piece = piece.color

                    self.squares[row][col].pieces_on_square = []
                    return color_of_top_piece
                    
