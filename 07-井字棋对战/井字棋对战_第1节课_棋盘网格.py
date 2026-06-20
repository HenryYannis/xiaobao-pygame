# 井字棋对战_第1节课_棋盘网格.py
# 学习目标：掌握如何使用 Pygame 绘制网格线，并建立 1D 列表作为棋盘的数据模型

import pygame  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((300, 300))  # 创建300x300窗口，每格100像素
pygame.display.set_caption("Tic-Tac-Toe - Lesson 1")
shizhong = pygame.time.Clock()

# 变量定义：棋盘数据列表。0代表空，1代表X，2代表O
# 这是一个长度为 9 的列表，对应 3x3 的格子
qipan_shuju = [0] * 9  # 棋盘数据（是什么），存储每个格子的状态（为什么），初始化为9个空位（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False

    chuangkou.fill((255, 255, 255))  # 刷白背景
    
    # 绘制棋盘网格线
    for i in range(1, 3):
        # 绘制两条垂直线
        pygame.draw.line(chuangkou, (0, 0, 0), (i*100, 0), (i*100, 300), 2)  # 竖线（是什么），划分列（为什么），起点终点(x,y)（怎么用）
        # 绘制两条水平线
        pygame.draw.line(chuangkou, (0, 0, 0), (0, i*100), (300, i*100), 2)  # 横线（是什么），划分行（为什么），起点终点(x,y)（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
