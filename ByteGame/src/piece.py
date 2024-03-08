import os

class Piece:

    def __init__(self, color, texture=None, texture_rect=None):
        self.color = color
        self.valid_moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=50):
        self.texture = os.path.join(
            f'assets/images/{self.color}-{size}px.png'
        )
    
    def add_move(self, move):
        self.valid_moves.append(move)
        
    def clear_moves(self):
        self.valid_moves = []