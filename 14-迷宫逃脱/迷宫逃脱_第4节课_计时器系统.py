import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Maze Escape - Lesson 4")
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

玩家x, 玩家y = 45, 45
游戏结束 = False
开始时间 = pygame.time.get_ticks()                     # 新增变量：记录本局游戏启动时的初始毫秒时间戳
通关用时 = 0                                           # 新增变量：记录逃脱成功的最终总秒数
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

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

        左上角通路 = 地图[尝试y // 40][尝试x // 40] == 0
        右下角通路 = 地图[(尝试y + 29) // 40][(尝试x + 29) // 40] == 0
        if 左上角通路 and 右下角通路:
            玩家x, 玩家y = 尝试x, 尝试y

        if 玩家x >= 320 and 玩家y >= 320:
            游戏结束 = True
            通关用时 = (当前时间 - 开始时间) // 1000    # 新增代码：到达终点时结算用时整秒数

    窗口.fill((20, 20, 20))                           # 暗灰黑色背景全屏填充

    for 行 in range(10):                               # 循环遍历绘制10x10迷宫网格
        for 列 in range(10):
            if 地图[行][列] == 1:
                pygame.draw.rect(窗口, (90, 90, 90), (列 * 40, 行 * 40, 40, 40))

    pygame.draw.rect(窗口, (0, 200, 80), (320, 320, 40, 40))
    pygame.draw.rect(窗口, (255, 60, 60), (玩家x, 玩家y, 30, 30))

    if not 游戏结束:                                   # 新增代码：进行中动态显示当前已消耗秒数
        已用秒数 = (当前时间 - 开始时间) // 1000
        提示画面 = 字体.render(f"TIME: {已用秒数}s", True, (255, 255, 255))
    else:                                              # 新增代码：通关后定格显示最终耗时
        提示画面 = 字体.render(f"YOU ESCAPED IN {通关用时}s!", True, (255, 220, 0))

    窗口.blit(提示画面, (10, 10))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
