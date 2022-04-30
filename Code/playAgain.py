from turtle import bgcolor
import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1440,850))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

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
                    play_again()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

play_again()
