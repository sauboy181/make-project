import pygame, sys 
from settings import * # import everything from settings
from level import Level
from debug import debug


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
