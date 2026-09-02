import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Maze Escape - Lesson 5")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 28)                     # 创建纯内置默认字体(是什么)，避免跨平台字体报错(为什么)，字号28(怎么用)

地图 = [                                               # 10x10迷宫网格数据模型(0代表通路，1代表实体墙壁)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def 重置游戏():                                       # 新增函数：重置游戏状态与玩家初始坐标
    return 45, 45, False, pygame.time.get_ticks(), 0   # 返回[玩家x, 玩家y, 游戏结束, 开始时间, 通关用时]

玩家x, 玩家y, 游戏结束, 开始时间, 通关用时 = 重置游戏()
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 游戏结束 and 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 新增代码：通关后按空格重开新局
            玩家x, 玩家y, 游戏结束, 开始时间, 通关用时 = 重置游戏()

    if not 游戏结束:
        按键 = pygame.key.get_pressed()
        尝试x, 尝试y = 玩家x, 玩家y
        if 按键[pygame.K_LEFT]:
            尝试x -= 2
        if 按键[pygame.K_RIGHT]:
            尝试x += 2
        if 按键[pygame.K_UP]:
            尝试y -= 2
        if 按键[pygame.K_DOWN]:
            尝试y += 2

        # 墙壁碰撞预测检测：同时检测玩家30x30四角包围盒是否都处于通路(0)内
        左上角通路 = 地图[尝试y // 40][尝试x // 40] == 0
        右下角通路 = 地图[(尝试y + 29) // 40][(尝试x + 29) // 40] == 0
        if 左上角通路 and 右下角通路:
            玩家x, 玩家y = 尝试x, 尝试y

        if 玩家x >= 320 and 玩家y >= 320:              # 终点判定：到达右下角绿色终点格子(x>=320, y>=320)
            游戏结束 = True
            通关用时 = (当前时间 - 开始时间) // 1000

    窗口.fill((20, 20, 20))                           # 暗灰黑色背景全屏填充

    for 行 in range(10):                               # 循环遍历绘制10x10迷宫网格
        for 列 in range(10):
            if 地图[行][列] == 1:
                pygame.draw.rect(窗口, (90, 90, 90), (列 * 40, 行 * 40, 40, 40))  # 绘制灰色墙壁方块

    pygame.draw.rect(窗口, (0, 200, 80), (320, 320, 40, 40))           # 绘制右下角绿色终点通关区域
    pygame.draw.rect(窗口, (255, 60, 60), (玩家x, 玩家y, 30, 30))      # 绘制红色方块探险玩家(宽30, 高30)

    if not 游戏结束:
        已用秒数 = (当前时间 - 开始时间) // 1000
        提示画面 = 字体.render(f"TIME: {已用秒数}s", True, (255, 255, 255))
    else:
        提示画面 = 字体.render(f"ESCAPED IN {通关用时}s! - Press SPACE", True, (255, 220, 0))  # 新增代码：通关展示成绩并提示按空格重置

    窗口.blit(提示画面, (10, 10))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
