from const import *
from piece import *

class Square:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.pieces_on_square = []
        
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    def add_piece(self, piece):
        self.pieces_on_square.append(piece)

    def is_valid_square(self): # def has_piece()
        return True if self.pieces_on_square else False
    
    @staticmethod
    def get_alphacol(col):
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p' }
        return ALPHACOLS[col]
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
                