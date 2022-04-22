import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/tree.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10) # Changes size of rectangle --> - 10 shrink 5 pixel on each side



# class Tile(pygame.sprite.Sprite):
#     def __init__(self, pos, groups):
#     # def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
#         super().__init__(groups)
#         # self.sprite_type = sprite_type
#         # self.image = surface
#         # if sprite_type == "object": #Adjusting objects
#         #     self.rect = self.image.get_rect(pos[0], pos[1] - TILESIZE) #Offset
#         # else:
#         #     self.rect = self.image.get_rect(topleft=pos)
#         self.image = pygame.image.load("../graphics/test/rock.png").convert_alpha()
#         self.rect = self.image.get_rect(topleft = pos)
#         self.hitbox = self.rect.inflate(0, -10) # Changes size of rectangle --> - 10 shrink 5 pixel on each side

