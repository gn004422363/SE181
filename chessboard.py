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


# function for main menu that includes start matching, about, and credit
def main_menu():
    # main menu background
    background = pygame.transform.scale(pygame.image.load("background_chessboard.jpg").convert(), (width, win_height))
    screen.blit(background, (0, 0))

    buttons("Start", 180)
    buttons("About", 300)
    buttons("Credit", 420)

# function for creating buttons with text, may add different event when buttons is clicked
def buttons(text, location):
    button_size = (220, 80)
    light_blue = (134, 197, 218)
    dark_blue = (30, 144, 255)
    x = 210
    mouse = pygame.mouse.get_pos()

    #create button with color, if mouse point to button, darker the color
    if (x < mouse[0] < (x + button_size[0])) and (location < mouse[1] < (location + button_size[1])):
        pygame.draw.rect(screen, dark_blue, pygame.Rect((x, location), button_size))
    else:
        pygame.draw.rect(screen, light_blue, pygame.Rect((x, location), button_size))

    #Font
    white = (255, 255, 255)
    font_x = 220//2 + 210
    font_y = 80//2 + location
    my_font = pygame.font.SysFont("arial", 26, True)
    title_surface = my_font.render(text, True, white)
    title = title_surface.get_rect(center=(font_x, font_y))
    screen.blit(title_surface, title)

def main():
    while True:
        pygame.event.pump()
        main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

        # my_chess.draw_board(screen) #comment out the board, this need to put in the start game event
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    width = 640
    height = 640
    win_height = height + 40
    # screen_center = (width//2, win_height//2)

    screen = pygame.display.set_mode((width, win_height))
    pygame.display.set_caption("Remote Chess Game")
    pygame.display.set_icon(pygame.image.load("icon.png"))

    light_color = pygame.Color("white")
    dark_color = pygame.Color("grey")
    my_chess = chessboard(width, height, light_color, dark_color)
    main()
