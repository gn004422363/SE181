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

# this function is to draw the board in 8x8 dimension
# even coordinated blocks are light colored and odd blocks are dark colored
# For Example, the first block [1,1] is going to be light colored
# Because 1+1 = 2 which is an even coordinated block
def draw_board(surface):
    screen.fill((225,225,225))
    for x in range(dimension):
        for y in range(dimension):
            block = pygame.Rect(x * block_size, y * block_size + 40, block_size, block_size)
            if (x+y) % 2 == 0:
                pygame.draw.rect(surface, pygame.Color("white"), block)
            else:
                pygame.draw.rect(surface, pygame.Color("grey"), block)

def main_menu():
    pass

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        draw_board(screen)
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    width = 640
    height = 640
    dimension = 8
    block_size = 80
    screen = pygame.display.set_mode((height, 680))
    pygame.display.set_caption("Remote Chess Game")
    pygame.display.set_icon(pygame.image.load("icon.png"))
    main()