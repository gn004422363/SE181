background_image_filename = 'background_chessboard.jpg'

# 指定图像文件名称

import pygame
# 导入pygame库
from pygame.locals import *
# 导入一些常用的函数和常量
from sys import exit

# 向sys模块借一个exit函数用来退出程序

pygame.init()
# 初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((640, 480), 0, 32)
rect = (113, 113, 525, 525)
startX = rect[0]
startY = rect[1]
# 创建了一个窗口
pygame.display.set_caption("Hello, World!")
# 设置窗口标题

background = pygame.image.load(background_image_filename).convert()
# 加载并转换图像

while True:
    # 游戏主循环

    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    screen.blit(background, (0, 0))
    # 将背景图画上去

    x, y = pygame.mouse.get_pos()

    pygame.display.update()