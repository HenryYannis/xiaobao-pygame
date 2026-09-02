import pygame

pygame.init()
窗口 = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Tic-Tac-Toe - Lesson 1")
时钟 = pygame.time.Clock()

棋盘数据 = [0] * 9                                     # 棋盘数据模型：长度为9的一维列表，0代表空格子
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    窗口.fill((255, 255, 255))                         # 纯白背景全屏填充

    for 序号 in range(1, 3):                           # 绘制九宫格四条黑色分割网格线
        pygame.draw.line(窗口, (0, 0, 0), (序号 * 100, 0), (序号 * 100, 300), 2)    # 纵向竖线
        pygame.draw.line(窗口, (0, 0, 0), (0, 序号 * 100), (300, 序号 * 100), 2)    # 横向水平线

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
