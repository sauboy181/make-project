import sys
from turtle import bgcolor

import pygame

from button import Button
from debug import debug
from settings import *
from support import import_folder
from tile import *

SCREEN = pygame.display.set_mode((1440,850))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


class Level:  # Contain all the sprites + interactions
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()  # Will be drawin in screen (Player/Map/Obstacle)
        self.obstacle_sprites = pygame.sprite.Group()  # Can collide with player
        self.player = pygame.sprite.Group()
        self.win_sprites = pygame.sprite.Group()  # Can collide with player

        # sprite setup
        self.create_map()

    
    def create_map(self):
        for row_index, row in enumerate(GAME_MAP):  # Each row, know the index
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE  # X position
                y = row_index * TILESIZE  # Y position
                if col == "x":  # Set up a certain kind of sprite
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "y":
                    Tile1((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "a":
                    Tile2((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "b":
                    Tile3((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "c":
                    Tile4((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "d":
                    Tile5((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "p":
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.win_sprites)
                if col == "z":
                    self.win_sprites = Key((x, y), [self.visible_sprites, self.win_sprites])
                    
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)  # Display visible sprites
        self.visible_sprites.update()
        # debug(self.player.direction) #Displays the [x,y] of the player
        # debug(self.player.status) #Displays the status of the player

class Level2:  # Contain all the sprites + interactions
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()  # Will be drawin in screen (Player/Map/Obstacle)
        self.obstacle_sprites = pygame.sprite.Group()  # Can collide with player
        self.win_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(GAME_MAP):  # Each row, know the index
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE  # X position
                y = row_index * TILESIZE  # Y position
                if col == "x":  # Set up a certain kind of sprite
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "y":
                    Tile1((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "a":
                    Tile2((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "b":
                    Tile3((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "c":
                    Tile4((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "d":
                    Tile5((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "p":
                    self.player2 = Player2(
                        (x, y), [self.visible_sprites], self.obstacle_sprites, self.win_sprites
                    )
                if col == "z":
                    self.win_sprites = Key((x, y), [self.visible_sprites, self.win_sprites])
                    
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player2)  # Display visible sprites
        self.visible_sprites.update()
        # debug(self.player.direction) #Displays the [x,y] of the player
        # debug(self.player.status) #Displays the status of the player

class Level3:  # Contain all the sprites + interactions
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()  # Will be drawin in screen (Player/Map/Obstacle)
        self.obstacle_sprites = pygame.sprite.Group()  # Can collide with player
        self.win_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(GAME_MAP):  # Each row, know the index
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE  # X position
                y = row_index * TILESIZE  # Y position
                if col == "x":  # Set up a certain kind of sprite
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "y":
                    Tile1((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "a":
                    Tile2((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "b":
                    Tile3((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "c":
                    Tile4((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "d":
                    Tile5((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "p":
                    self.player3 = Player3(
                        (x, y), [self.visible_sprites], self.obstacle_sprites, self.win_sprites
                    )
                if col == "z":
                    self.win_sprites = Key((x, y), [self.visible_sprites, self.win_sprites])
           
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player3)  # Display visible sprites
        self.visible_sprites.update()
        # debug(self.player.direction) #Displays the [x,y] of the player
        # debug(self.player.status) #Displays the status of the player

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos, groups, obstacle_sprites, win_sprites):
    # def __init__(self, pos, groups, obstacle_sprites):

        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/knight1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-20)

        #Graphics setup
        self.import_player_assets()
        self.status = "down"
        self.frame_index = 0
        self.animation_speed = .15

        self.direction = pygame.math.Vector2()  # Vector that is going to have x and y
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
        self.win_sprites = win_sprites

    def import_player_assets(self):
        character_path = "../graphics/test/knight/" 
        self.animations = {
            "up": [],
            "down": [],
            "left": [],
            "right": [],
            "right_idle": [],
            "left_idle": [],
            "up_idle": [],
            "down_idle": [],
        } #All animation states

        for animation in self.animations.keys():
            # print(animation)
            full_path = character_path + animation #Create path
            self.animations[animation] = import_folder(full_path) #Import images

    def input(self):
        keys = pygame.key.get_pressed()

        # Movement Input
        if keys[pygame.K_UP]:
            self.direction.y = -1  # Going up
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1  # Going down
            self.status = "down"
        else:
            self.direction.y = 0 # IF neither up or down key being pressed player does not move

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:  # Check if direction is 0
            if not "idle" in self.status:  # check if status does not contain idle/ attacking
                self.status = (self.status + "_idle")  # Only add idle once and not multiple times

    def move(self, speed):  # Update + draw the game
        if self.direction.magnitude() != 0:  # Vector of 0 can not be normalized
            self.direction = self.direction.normalize()  # Vector length = 1

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")  # Horizontal Collisions
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")  # Vertical Collisions
        self.rect.center = self.hitbox.center

    def collision(self, direction):  # Check for collisions
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # Moving right
                        self.hitbox.right = sprite.hitbox.left
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x < 0:  # Moving left
                        self.hitbox.left = sprite.hitbox.right
            for sprite in self.win_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x >= 0 or self.direction.x <= 0:  # Moving right
                        play_again()
        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y < 0:  # Moving up
                        self.hitbox.top = sprite.hitbox.bottom        
            for sprite in self.win_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y >= 0 or self.direction.y <= 0:  # Moving down
                        play_again()
                
    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed # Continuously larger number
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Set the image
        self.image = animation[int(self.frame_index)] #Convert frame index to integer
        self.rect = self.image.get_rect(center = self.hitbox.center)
 
    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)

class Player2(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, win_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/mage1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-20)

        #Graphics setup
        self.import_player_assets()
        self.status = "down"
        self.frame_index = 0
        self.animation_speed = .15

        self.direction = pygame.math.Vector2()  # Vector that is going to have x and y
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
        self.win_sprites = win_sprites

    def import_player_assets(self):
        character_path = "../graphics/test/mage/" 
        self.animations = {
            "up": [],
            "down": [],
            "left": [],
            "right": [],
            "right_idle": [],
            "left_idle": [],
            "up_idle": [],
            "down_idle": [],
        } #All animation states

        for animation in self.animations.keys():
            # print(animation)
            full_path = character_path + animation #Create path
            self.animations[animation] = import_folder(full_path) #Import images

    def input(self):
        keys = pygame.key.get_pressed()

        # Movement Input
        if keys[pygame.K_UP]:
            self.direction.y = -1  # Going up
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1  # Going down
            self.status = "down"
        else:
            self.direction.y = (0) # IF neither up or down key being pressed player does not move

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:  # Check if direction is 0
            if not "idle" in self.status:  # check if status does not contain idle/ attacking
                self.status = (self.status + "_idle")  # Only add idle once and not multiple times

    def move(self, speed):  # Update + draw the game
        if self.direction.magnitude() != 0:  # Vector of 0 can not be normalized
            self.direction = self.direction.normalize()  # Vector length = 1

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")  # Horizontal Collisions
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")  # Vertical Collisions
        self.rect.center = self.hitbox.center

    def collision(self, direction):  # Check for collisions
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # Moving right
                        self.hitbox.right = sprite.hitbox.left
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x < 0:  # Moving left
                        self.hitbox.left = sprite.hitbox.right
            for sprite in self.win_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x >= 0 or self.direction.x <= 0:  # Moving right
                        play_again()
        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y < 0:  # Moving up
                        self.hitbox.top = sprite.hitbox.bottom        
            for sprite in self.win_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y >= 0 or self.direction.y <= 0:  # Moving down
                        play_again()

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed # Continuously larger number
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Set the image
        self.image = animation[int(self.frame_index)] #Convert frame index to integer
        self.rect = self.image.get_rect(center = self.hitbox.center)
 
    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)

class Player3(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, win_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/rogue1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-20)

        #Graphics setup
        self.import_player_assets()
        self.status = "down"
        self.frame_index = 0
        self.animation_speed = .15

        self.direction = pygame.math.Vector2()  # Vector that is going to have x and y
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
        self.win_sprites = win_sprites

    def import_player_assets(self):
        character_path = "../graphics/test/rogue/" 
        self.animations = {
            "up": [],
            "down": [],
            "left": [],
            "right": [],
            "right_idle": [],
            "left_idle": [],
            "up_idle": [],
            "down_idle": [],
        } #All animation states

        for animation in self.animations.keys():
            # print(animation)
            full_path = character_path + animation #Create path
            self.animations[animation] = import_folder(full_path) #Import images

    def input(self):
        keys = pygame.key.get_pressed()

        # Movement Input
        if keys[pygame.K_UP]:
            self.direction.y = -1  # Going up
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1  # Going down
            self.status = "down"
        else:
            self.direction.y = 0 # IF neither up or down key being pressed player does not move

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:  # Check if direction is 0
            if not "idle" in self.status:  # check if status does not contain idle/ attacking
                self.status = (self.status + "_idle")  # Only add idle once and not multiple times

    def move(self, speed):  # Update + draw the game
        if self.direction.magnitude() != 0:  # Vector of 0 can not be normalized
            self.direction = self.direction.normalize()  # Vector length = 1

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")  # Horizontal Collisions
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")  # Vertical Collisions
        self.rect.center = self.hitbox.center

    def collision(self, direction):  # Check for collisions
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # Moving right
                        self.hitbox.right = sprite.hitbox.left
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x < 0:  # Moving left
                        self.hitbox.left = sprite.hitbox.right
            for sprite in self.win_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x >= 0 or self.direction.x <= 0:  # Moving right
                        play_again()
        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y < 0:  # Moving up
                        self.hitbox.top = sprite.hitbox.bottom        
            for sprite in self.win_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y >= 0 or self.direction.y <= 0:  # Moving down
                        play_again()

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed # Continuously larger number
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Set the image
        self.image = animation[int(self.frame_index)] #Convert frame index to integer
        self.rect = self.image.get_rect(center = self.hitbox.center)
 
    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)

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

    def custom_draw(self, player):

        # getting the offset of the player
        self.offset.x = player.rect.centerx - self.half_width  
        self.offset.y = player.rect.centery - self.half_height  

        for sprite in sorted(self.sprites(), key = lambda sprite:sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
              
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black") 

        PLAY_TEXT = get_font(45).render("Choose a character", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(730,180))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
        # character selection page button setup
        CHOOSE_MAGE_IMAGE = Button(image=pygame.image.load("assets/mage.png"), pos=(400, 350), 
            text_input="", font=get_font(30), base_color="White", hovering_color="light green")
        CHOOSE_MAGE = Button(image=None, pos=(360, 550), 
            text_input="MAGE", font=get_font(35), base_color="White", hovering_color="light green")
        CHOOSE_KNIGHT_IMAGE = Button(image=pygame.image.load("assets/knight.png"), pos=(780, 350), 
            text_input="", font=get_font(30), base_color="White", hovering_color="light green")
        CHOOSE_KNIGHT = Button(image=None, pos=(740, 550), 
            text_input="KNIGHT", font=get_font(35), base_color="White", hovering_color="light green")
        CHOOSE_ROGUE_IMAGE = Button(image=pygame.image.load("assets/rogue.png"), pos=(1160, 350), 
            text_input="", font=get_font(30), base_color="White", hovering_color="light green")
        CHOOSE_ROGUE = Button(image=None, pos=(1120, 550), 
            text_input="ROGUE", font=get_font(35), base_color="White", hovering_color="light green")
        PLAY_BACK = Button(image=None, pos=(740, 750), 
            text_input="BACK", font=get_font(35), base_color="White", hovering_color="light green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        CHOOSE_MAGE_IMAGE.changeColor(PLAY_MOUSE_POS)
        CHOOSE_MAGE_IMAGE.update(SCREEN)
        CHOOSE_MAGE.changeColor(PLAY_MOUSE_POS)
        CHOOSE_MAGE.update(SCREEN)
        CHOOSE_KNIGHT_IMAGE.changeColor(PLAY_MOUSE_POS)
        CHOOSE_KNIGHT_IMAGE.update(SCREEN)
        CHOOSE_KNIGHT.changeColor(PLAY_MOUSE_POS)
        CHOOSE_KNIGHT.update(SCREEN)
        CHOOSE_ROGUE_IMAGE.changeColor(PLAY_MOUSE_POS)
        CHOOSE_ROGUE_IMAGE.update(SCREEN)
        CHOOSE_ROGUE.changeColor(PLAY_MOUSE_POS)
        CHOOSE_ROGUE.update(SCREEN)

        # assigning instructions for button selection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOOSE_MAGE_IMAGE.checkForInput(PLAY_MOUSE_POS) or CHOOSE_MAGE.checkForInput(PLAY_MOUSE_POS):
                    class Game:
                        def __init__(self):

                            # general setup
                            pygame.init() #Initiate pygame
                            self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initiate surface
                            pygame.display.set_caption("Maze Runner")
                            self.clock = pygame.time.Clock() #clock       

                            self.level = Level2()

                            self.time = pygame.time.get_ticks()

                        def run(self):
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()

                                self.screen.fill('light green') # light green background
                                self.level.run()
                                self.clock.tick(FPS) # FPS
                                
                                self.passed_time = pygame.time.get_ticks() - self.time
                                self.timer_text = get_font(20).render(str(self.passed_time/1000), True, "#000000")
                                self.timer_rect = self.timer_text.get_rect(center=(100,25))
                                SCREEN.blit(self.timer_text,self.timer_rect)
                                pygame.display.update() # updating screen
                                
                    if __name__ == "__main__":  
                        game = Game()
                        game.run()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOOSE_KNIGHT_IMAGE.checkForInput(PLAY_MOUSE_POS) or CHOOSE_KNIGHT.checkForInput(PLAY_MOUSE_POS):
                    class Game:
                        def __init__(self):

                            # general setup
                            pygame.init() #Initiate pygame
                            self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initiate surface
                            pygame.display.set_caption("Maze Runner")
                            self.clock = pygame.time.Clock() #clock
                            self.level = Level()

                            self.time = pygame.time.get_ticks()

                        def run(self):
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()

                                self.screen.fill('light green') # light green background
                                self.level.run()
                                self.clock.tick(FPS) # FPS
                                
                                self.passed_time = pygame.time.get_ticks() - self.time
                                self.timer_text = get_font(20).render(str(self.passed_time/1000), True, "#000000")
                                self.timer_rect = self.timer_text.get_rect(center=(100,25))
                                SCREEN.blit(self.timer_text,self.timer_rect)
                                pygame.display.update() # updating screen

                    if __name__ == "__main__":  
                        game = Game()
                        game.run()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOOSE_ROGUE_IMAGE.checkForInput(PLAY_MOUSE_POS) or CHOOSE_ROGUE.checkForInput(PLAY_MOUSE_POS):
                    class Game:
                        def __init__(self):

                            # general setup
                            pygame.init() #Initiate pygame
                            self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initiate surface
                            pygame.display.set_caption("Maze Runner")
                            self.clock = pygame.time.Clock() #clock
                            
                            self.level = Level3()
                            self.time = pygame.time.get_ticks()

                        def run(self):
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()

                                self.screen.fill('light green') # light green background
                                self.level.run()
                                self.clock.tick(FPS) # FPS
                                
                                self.passed_time = pygame.time.get_ticks() - self.time
                                self.timer_text = get_font(20).render(str(self.passed_time/1000), True, "#000000")
                                self.timer_rect = self.timer_text.get_rect(center=(100,25))
                                SCREEN.blit(self.timer_text,self.timer_rect)
                                pygame.display.update() # updating screen

                    if __name__ == "__main__":  
                        game = Game()
                        game.run()

        pygame.display.update()
def main_menu():

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(720, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(270, 260), 
            text_input="PLAY", font=get_font(75), base_color="#000000", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1200, 260), 
            text_input="QUIT", font=get_font(75), base_color="#000000", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play_again():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black") 

        PLAY_TEXT = get_font(45).render("Play again?", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(730,180))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_AGAIN = Button(image=None, pos=(500, 450), 
                            text_input="Yes", font=get_font(70), base_color="White", hovering_color="green")
        QUIT = Button(image=None, pos=(950, 450), 
                            text_input="No", font=get_font(70), base_color="White", hovering_color="red")

        PLAY_AGAIN.changeColor(PLAY_MOUSE_POS)
        PLAY_AGAIN.update(SCREEN)
        QUIT.changeColor(PLAY_MOUSE_POS)
        QUIT.update(SCREEN)


        # assigning instructions for button selection
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_AGAIN.checkForInput(PLAY_MOUSE_POS):
                            main_menu()
                        if QUIT.checkForInput(PLAY_MOUSE_POS):
                            pygame.quit()
                            sys.exit()
                    
        pygame.display.update() 

main_menu()
