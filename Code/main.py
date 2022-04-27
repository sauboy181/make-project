from turtle import bgcolor
import pygame, sys
from button import Button

import pygame, sys 
from settings import * # import everything from settings
from level import Level
from level2 import Level2
from level3 import Level3
from debug import debug

pygame.init()

SCREEN = pygame.display.set_mode((1440,850))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

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
                        if CHOOSE_MAGE_IMAGE.checkForInput(PLAY_MOUSE_POS):
                            class Game:
                                def __init__(self):

                                    # general setup
                                    pygame.init() #Initiate pygame
                                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initiate surface
                                    pygame.display.set_caption("Maze Runner")
                                    self.clock = pygame.time.Clock() #clock
                                    
                                    self.level = Level2()

                                def run(self):
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                        self.screen.fill('light green') # light green background
                                        self.level.run()
                                        pygame.display.update() # updating screen
                                        self.clock.tick(FPS) # FPS


                            if __name__ == "__main__":  
                                game = Game()
                                game.run()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CHOOSE_MAGE.checkForInput(PLAY_MOUSE_POS):
                            
                            class Game:
                                def __init__(self):

                                    # general setup
                                    pygame.init() #Initiate pygame
                                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initiate surface
                                    pygame.display.set_caption("Maze Runner")
                                    self.clock = pygame.time.Clock() #clock
                                    
                                    self.level = Level2()

                                def run(self):
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                        self.screen.fill('light green') # light green background
                                        self.level.run()
                                        pygame.display.update() # updating screen
                                        self.clock.tick(FPS) # FPS


                            if __name__ == "__main__":  
                                game = Game()
                                game.run()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CHOOSE_KNIGHT_IMAGE.checkForInput(PLAY_MOUSE_POS):
                            
                            class Game:
                                def __init__(self):

                                    # general setup
                                    pygame.init() #Initiate pygame
                                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initiate surface
                                    pygame.display.set_caption("Maze Runner")
                                    self.clock = pygame.time.Clock() #clock
                                    
                                    self.level = Level()

                                def run(self):
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                        self.screen.fill('light green') # light green background
                                        self.level.run()
                                        pygame.display.update() # updating screen
                                        self.clock.tick(FPS) # FPS


                            if __name__ == "__main__":  
                                game = Game()
                                game.run()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CHOOSE_KNIGHT.checkForInput(PLAY_MOUSE_POS):
                            
                            class Game:
                                def __init__(self):

                                    # general setup
                                    pygame.init() #Initiate pygame
                                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initiate surface
                                    pygame.display.set_caption("Maze Runner")
                                    self.clock = pygame.time.Clock() #clock
                                    
                                    self.level = Level()

                                def run(self):
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                        self.screen.fill('light green') # light green background
                                        self.level.run()
                                        pygame.display.update() # updating screen
                                        self.clock.tick(FPS) # FPS


                            if __name__ == "__main__":  
                                game = Game()
                                game.run()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CHOOSE_ROGUE_IMAGE.checkForInput(PLAY_MOUSE_POS):
                            
                            class Game:
                                def __init__(self):

                                    # general setup
                                    pygame.init() #Initiate pygame
                                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initiate surface
                                    pygame.display.set_caption("Maze Runner")
                                    self.clock = pygame.time.Clock() #clock
                                    
                                    self.level = Level3()

                                def run(self):
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                        self.screen.fill('light green') # light green background
                                        self.level.run()
                                        pygame.display.update() # updating screen
                                        self.clock.tick(FPS) # FPS


                            if __name__ == "__main__":  
                                game = Game()
                                game.run()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CHOOSE_ROGUE.checkForInput(PLAY_MOUSE_POS):
                            
                            class Game:
                                def __init__(self):

                                    # general setup
                                    pygame.init() #Initiate pygame
                                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initiate surface
                                    pygame.display.set_caption("Maze Runner")
                                    self.clock = pygame.time.Clock() #clock
                                    
                                    self.level = Level3()

                                def run(self):
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                        self.screen.fill('light green') # light green background
                                        self.level.run()
                                        pygame.display.update() # updating screen
                                        self.clock.tick(FPS) # FPS


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

main_menu()
