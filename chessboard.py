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
        screen.fill((225, 225, 225))
        for x in range(self.dimension):
            for y in range(self.dimension):
                block = pygame.Rect(x * self.block_size, y * self.block_size + 40, self.block_size, self.block_size)
                if (x+y) % 2 == 0:
                    pygame.draw.rect(surface, self.color_row, block)
                else:
                    pygame.draw.rect(surface, self.color_col, block)

    def main_menu(self):
        pass

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        new_chess.draw_board(screen)
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    width = 640
    height = 640

    screen = pygame.display.set_mode((height, 680))
    pygame.display.set_caption("Remote Chess Game")
    pygame.display.set_icon(pygame.image.load("icon.png"))

    light_color = pygame.Color("white")
    dark_color = pygame.Color("grey")
    new_chess = chessboard(width, height, light_color, dark_color)
    main()