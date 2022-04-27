import pygame
from settings import *
from tile import Tile
from player3 import Player3
from debug import debug


class Level3:  # Contain all the sprites + interactions
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()  # Will be drawin in screen (Player/Map/Obstacle)
        self.obstacle_sprites = pygame.sprite.Group()  # Can collide with player

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(GAME_MAP):  # Each row, know the index
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE  # X position
                y = row_index * TILESIZE  # Y position
                if col == "x":  # Set up a certain kind of sprite
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "p":
                    self.player3 = Player3(
                        (x, y), [self.visible_sprites], self.obstacle_sprites
                    )
           
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player3)  # Display visible sprites
        self.visible_sprites.update()
        # debug(self.player.direction) #Displays the [x,y] of the player
        # debug(self.player.status) #Displays the status of the player



class YSortCameraGroup(pygame.sprite.Group):
    # Sort the sprite by Y-coordinate
    # Make a camera
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface() # Display the surface
        self.half_width = (
            self.display_surface.get_size()[0] // 2
        )  # Player in the middle --> Distance from the left
        self.half_height = (
            self.display_surface.get_size()[1] // 2
        )  # Player in the middle --> Distance from the top
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player3):

        # getting the offset of the player
        self.offset.x = player3.rect.centerx - self.half_width  #
        self.offset.y = player3.rect.centery - self.half_height  #

        for sprite in sorted(self.sprites(), key = lambda sprite:sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

