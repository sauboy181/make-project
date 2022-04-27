import pygame
from settings import *
from support import import_folder

class Player2(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
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

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y < 0:  # Moving up
                        self.hitbox.top = sprite.hitbox.bottom

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
