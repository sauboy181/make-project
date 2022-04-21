import pygame
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/deadpool.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-26)

        #Graphics setup
        self.import_player_assets()
        self.status = "down"
        self.frame_index = 0
        self.animation_speed = .15

        self.direction = pygame.math.Vector2()  # Vector that is going to have x and y
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

    def import_player_assets(self):
        character_path = "../graphics/test/player/" 
        self.animations = {
            "up": [],
            "down": [],
            "left": [],
            "right": [],
            "right_idle": [],
            "left_idle": [],
            "up_idle": [],
            "down_idle": [],
            "right_attack": [],
            "left_attack": [],
            "up_attack": [],
            "down_attack": [],
        } #All animation states

        for animation in self.animations.keys():
            # print(animation)
            full_path = character_path + animation #Create path
            self.animations[animation] = import_folder(full_path) #Import images

    def input(self):
        if not self.attacking: # no keyboard input when character attacks
            keys = pygame.key.get_pressed()

            # Movement Input
            if keys[pygame.K_UP]:
                self.direction.y = -1  # Going up
                self.status = "up"
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1  # Going down
                self.status = "down"
            else:
                self.direction.y = (
                    0  # IF neither up or down key being pressed player does not move
                )

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = "right"
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = "left"
            else:
                self.direction.x = 0

            # Attack input
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks
                print("attack")

            # Magic input
            if keys[pygame.K_1]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks
                print("magic")

    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:  # Check if direction is 0
            if not "idle" in self.status and not "attack" in self.status:  # check if status does not contain idle/ attacking
                self.status = (self.status + "_idle")  # Only add idle once and not multiple times

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not "attack" in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle","_attack") #Overwrite idle in place for attack
                else:
                    self.status = self.status + "_attack"
        else:
            if "attack" in self.status:
                self.status = self.status.replace("_attack","") #After attacking --> blank

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

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attacking >= self.attack_cooldown:
                self.attacking = False

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
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
