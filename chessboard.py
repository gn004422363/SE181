"""
    Project For SE 181
    Group 22
    Ailin Weng
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


class chessboard:
    dimension = 8
    block_size = 80

    # constructor for building up the board in x/y position with light/dark color
    def __init__(self, x, y, light, dark):
        self.row = x
        self.col = y
        self.color_row = light
        self.color_col = dark

    # this function is to draw the board in 8x8 dimension
    # even coordinated blocks are light colored and odd blocks are dark colored
    # For Example, the first block [1,1] is going to be light colored
    # Because 1+1 = 2 which is an even coordinated block
    def draw_board(self, surface):
        for x in range(self.dimension):
            for y in range(self.dimension):
                block = pygame.Rect(x * self.block_size, y * self.block_size + 40, self.block_size, self.block_size)
                if (x + y) % 2 == 0:
                    pygame.draw.rect(surface, self.color_row, block)
                else:
                    pygame.draw.rect(surface, self.color_col, block)


# function for creating buttons with text, may add different event when buttons is clicked
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

    def button_text(self):
        text_x = self.x + self.w // 2
        text_y = self.y + self.h // 2
        text_font = pygame.font.SysFont("arial", 26, True)
        title_surface = text_font.render(self.text, True, self.white)
        title = title_surface.get_rect(center=(text_x, text_y))
        screen.blit(title_surface, title)

    def button_function(self):
        if self.text == "Start":
            # need to connect to go to waiting page for player if only one connection
            # start the game where there are two players
            chess_loop()
        elif self.text == "About":
            pass
        elif self.text == "Credit":
            pass


# function for main menu that includes start matching, about, and credit
def main_menu():
    # my_chess = chessboard(width, height, light_color, dark_color)
    # main menu background
    background = pygame.transform.scale(pygame.image.load("background_chessboard.jpg").convert(), (width, win_height))
    screen.blit(background, (0, 0))

    start = buttons(180, "Start")
    about = buttons(300, "About")
    credit = buttons(420, "Credit")

    start.draw_button(screen)
    about.draw_button(screen)
    credit.draw_button(screen)


def main_menu_loop():
    while True:
        pygame.event.pump()
        main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()


def chess_loop():
    while True:
        pygame.event.pump()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        my_chess.draw_board(screen)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    width = 640
    height = 640
    win_height = height + 40

    # set up the windows, caption, and icon for chess game
    screen = pygame.display.set_mode((width, win_height))
    pygame.display.set_caption("Remote Chess Game")
    pygame.display.set_icon(pygame.image.load("icon.png"))

    light_color = pygame.Color("white")
    dark_color = pygame.Color("grey")
    my_chess = chessboard(width, height, light_color, dark_color)
    main_menu_loop()