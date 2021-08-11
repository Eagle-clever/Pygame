#!/usr/bin/env python
# encoding: utf-8
"""
@author: Eagle
@contact: 2170257193qq.com
@software: PyCharm
@file: pygame_基本流程.py
@time: 2021/8/11 下午9:26
@desc: 游戏设计基本流程
"""

import pygame
import sys
# 引入所需库

pygame.init()               # Pygame初始化

screen = pygame.display.set_mode((500,500))              # 游戏创建窗口

while True:
    pygame.display.update()                              # 不断刷新游戏画面
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                    # 检测事件__如果按下了"QUIT"键，就执行退出
            # QUIT为一个常量,数值为256。表示事件类型为退出Pygame
            pygame.quit()
            sys.exit()
            # 如果系统在pygame.quit()前终止，IDLE会挂起，所以一般会在最后调用sys.exit()

