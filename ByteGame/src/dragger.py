import pygame

from const import *

class Dragger:
    
    def __init__(self):
        self.pieces = []
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = None
        self.initial_col = None
    
    def update_blit(self, surface):
        
        def draw_singular_stack_piece(piece, value):
            # texture
            piece.set_texture(size=50)
            texture = piece.texture
            # img
            img = pygame.image.load(texture)
            # rect
            img_center = (self.mouseX, self.mouseY - (value * SQSIZE))
            piece.texture_rect = img.get_rect(center = img_center)
            # blit
            surface.blit(img, piece.texture_rect)
            
            # img = pygame.image.load(piece.texture)
            # img_center = self.initial_col * SQSIZE + SQSIZE // 2, self.initial_row * SQSIZE + (value * SQSIZE)
            # piece.texture_rect = img.get_rect(center = img_center)
            # surface.blit(img, piece.texture_rect)
        
        for piece in self.pieces:
            if piece == self.pieces[0]:
                draw_singular_stack_piece(piece, 0.01)
            elif piece == self.pieces[1]:
                draw_singular_stack_piece(piece, 0.11)
            elif piece == self.pieces[2]:
                draw_singular_stack_piece(piece, 0.21)
            elif piece == self.pieces[3]:
                draw_singular_stack_piece(piece, 0.31)
            elif piece == self.pieces[4]:
                draw_singular_stack_piece(piece, 0.41)
            elif piece == self.pieces[5]:
                draw_singular_stack_piece(piece, 0.51)
            elif piece == self.pieces[6]:
                draw_singular_stack_piece(piece, 0.61)
            elif piece == self.pieces[7]:
                draw_singular_stack_piece(piece, 0.71)
            
            
            
            # texture
            #  piece.set_texture(size=50)
            #  texture = piece.texture
            # img
            #  img = pygame.image.load(texture)
            # rect
            #  img_center = (self.mouseX, self.mouseY)
            #  piece.texture_rect = img.get_rect(center = img_center)
            # blit
            #  surface.blit(img, piece.texture_rect)
        
    
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos
        
    def save_initial(self, pos):
        self.initial_col = pos[0] // SQSIZE
        self.initial_row = pos[1] // SQSIZE
    
    def drag_piece(self, pieces):
        self.pieces = pieces
        self.dragging = True
        
    def undrag_piece(self):
        self.pieces = None
        self.dragging = False
        