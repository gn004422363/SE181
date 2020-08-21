"""
    Project For SE 181
    Group 22
    Ailin Weng
    Jonah Musto
    Man Tik Li
    Yi Yan
"""

"""
    This is a game interface that contains a main menu
    and a chessboard.
    Players will get to choose from "Match Game" to play chess, 
    "About" to see game version, and "Credit" to see our developers
"""

import pygame
import sys
sys.path.insert(0, "./SE181_pieces")
import SE181_samplemain
from network import Network

class chessboard:
    dimension = 8
    block_size = 80

    # constructor for building up the board in x/y position with light/dark color
    def __init__(self, x, y, light, dark):
        self.row = x
        self.col = y
        self.color_row = light
        self.color_col = dark
        self.run = True

    # this function is to draw the board in 8x8 dimension
    # even coordinated blocks are light colored and odd blocks are dark colored
    # For Example, the first block [1,1] is going to be light colored
    # Because 1+1 = 2 which is an even coordinated block
    def draw_board(self, surface):
        for x in range(self.dimension):
            for y in range(self.dimension):
                block = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
                if (x + y) % 2 == 0:
                    pygame.draw.rect(surface, self.color_row, block)
                else:
                    pygame.draw.rect(surface, self.color_col, block)

    # render pieces pic on block
    def draw_piece(self):
        for x in range(self.dimension):
            for y in range(self.dimension):
                piece = SE181_samplemain.board[x][y]
                print(piece)
                piece_rect = pygame.Rect(y * self.block_size, x * self.block_size, self.block_size, self.block_size)
                if piece != None:
                    if piece.color == "Black":
                        piece_img = pygame.transform.scale(pygame.image.load("images/b" + type(piece).__name__ + ".png"), (self.block_size, self.block_size))
                        screen.blit(piece_img, piece_rect)
                    else:
                        piece_img = pygame.transform.scale(pygame.image.load("images/w" + type(piece).__name__ + ".png"), (self.block_size, self.block_size))
                        screen.blit(piece_img, piece_rect)

    # chess game loop
    def chess_run(self, surface):
        self.draw_board(surface)
        self.draw_piece()
        while self.run:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
            pygame.display.update()

# class for creating buttons with text, may add different event when buttons is clicked
class buttons:
    button_size = (220, 80)
    white = (255, 255, 255)
    light_blue = (134, 197, 218)
    dark_blue = (30, 144, 255)

    # constructor for buttons. Buttons will have a fix x position and fix button width and height
    # pass in y position and the text/function of the button to create the buttons
    def __init__(self, y, text):
        self.x = 210
        self.y = y
        self.w = self.button_size[0]
        self.h = self.button_size[1]
        self.text = text
        self.button = pygame.Rect(self.x, self.y, self.w, self.h)

    # draw button on main menu
    def draw_button(self, surface):
        mouse = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if (self.x < mouse[0] < (self.x + self.w)) and (self.y < mouse[1] < (self.y + self.h)):
            pygame.draw.rect(surface, self.dark_blue, self.button)
            self.button_text()
            if mouse_click[0] == 1:
                self.button_function()
        else:
            pygame.draw.rect(surface, self.light_blue, self.button)
            self.button_text()

    # render text on buttons
    def button_text(self):
        text_x = self.x + self.w // 2
        text_y = self.y + self.h // 2
        text_font = pygame.font.SysFont("arial", 26, True)
        title_surface = text_font.render(self.text, True, self.white)
        title = title_surface.get_rect(center=(text_x, text_y))
        screen.blit(title_surface, title)

    # different button functionalities
    def button_function(self):
        if self.text == "Start":
            # need to connect to go to waiting page for player if only one connection
            # start the game where there are two players
            my_chess.chess_run(screen)
        elif self.text == "About":
            about = True
            while about:
                screen.fill((169, 169, 169))
                about_font = pygame.font.SysFont("arial", 16, True)
                about_text = about_font.render("Online Chess Game Version 1.0", True, self.white)
                about_rect = about_text.get_rect(center=(width//2, height//2))
                screen.blit(about_text, about_rect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        about = False
                        main()
                    elif event.type == pygame.QUIT:
                        exit()
        elif self.text == "Credit":
            credit = True
            while credit:
                screen.fill((169, 169, 169))
                credit_font = pygame.font.SysFont("arial", 16, True)
                credit_text = credit_font.render("Dev: Ailin Weng, Jonah Musto, Man Tik Li, Yi Yan", True, self.white)
                credit_rect = credit_text.get_rect(center=(width // 2, height // 2))
                screen.blit(credit_text, credit_rect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        credit = False
                        main()
                    elif event.type == pygame.QUIT:
                        exit()

# function for main menu that includes start matching, about, and credit
def main_menu():
    # main menu background
    background = pygame.transform.scale(pygame.image.load("images/background_chessboard.jpg").convert(), (width, height))
    screen.blit(background, (0, 0))

    start = buttons(180, "Start")
    about = buttons(300, "About")
    credit = buttons(420, "Credit")

    start.draw_button(screen)
    about.draw_button(screen)
    credit.draw_button(screen)

def main():
    while True:
        pygame.event.pump()
        main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    width = 640
    height = 640

    # run = True
    # n = Network()
    # p = n.getPos()
    # clock = pygame.time.Clock()
    #
    # for e in pygame.event.get():
    #     if e.type == pygame.QUIT:
    #         run = False
    #         pygame.quit()


    # set up the windows, caption, and icon for chess game
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Remote Chess Game")
    pygame.display.set_icon(pygame.image.load("images/icon.png"))

    light_color = pygame.Color("white")
    dark_color = pygame.Color("grey")
    my_chess = chessboard(width, height, light_color, dark_color)
    main()
