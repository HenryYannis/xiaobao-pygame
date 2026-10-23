import pygame

pygame.init()
窗口 = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Tic-Tac-Toe - Lesson 2")
时钟 = pygame.time.Clock()

棋盘数据 = [0] * 9                                     # 棋盘数据模型：长度为9的一维列表，0代表空，1代表玩家1，2代表玩家2
当前玩家 = 1                                           # 新增变量：执子标志位，1代表玩家1，2代表玩家2(交替落子)
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.MOUSEBUTTONDOWN and 事件.button == 1:  # 新增代码：响应鼠标左键落子(button 1是左键，滚轮和右键不算)
            鼠标x, 鼠标y = 事件.pos                   # 新增代码：取事件自带的点击坐标
            格点索引 = (鼠标y // 100) * 3 + (鼠标x // 100)  # 新增代码：换算列表索引(0-8)
            if 0 <= 格点索引 < 9 and 棋盘数据[格点索引] == 0:  # 新增代码：仅在空格位允许落子
                棋盘数据[格点索引] = 当前玩家         # 新增代码：写入当前玩家棋子
                当前玩家 = 2 if 当前玩家 == 1 else 1   # 新增代码：切换执子方(1与2交替)

    窗口.fill((255, 255, 255))                         # 纯白背景全屏填充

    for 序号 in range(1, 3):                           # 绘制九宫格四条黑色分割网格线
        pygame.draw.line(窗口, (0, 0, 0), (序号 * 100, 0), (序号 * 100, 300), 2)    # 纵向竖线
        pygame.draw.line(窗口, (0, 0, 0), (0, 序号 * 100), (300, 序号 * 100), 2)    # 横向水平线

    for 索引, 棋子 in enumerate(棋盘数据):             # 新增代码：遍历棋盘数据绘制双方棋子
        中心x = (索引 % 3) * 100 + 50
        中心y = (索引 // 3) * 100 + 50
        if 棋子 == 1:
            pygame.draw.circle(窗口, (255, 60, 60), (中心x, 中心y), 30, 3)          # 新增代码：玩家1红色圆圈
        elif 棋子 == 2:
            pygame.draw.rect(窗口, (50, 120, 255), (中心x - 25, 中心y - 25, 50, 50), 3) # 新增代码：玩家2蓝色方块

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
