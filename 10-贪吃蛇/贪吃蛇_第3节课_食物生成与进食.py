import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake - Lesson 3")
时钟 = pygame.time.Clock()

格点 = 20                                             # 每个网格单元的像素跨度
蛇身 = [[200, 200]]                                   # 蛇身节点列表
速度 = [格点, 0]                                      # 初始移动方向与步长
食物 = [random.randint(0, 19) * 格点, random.randint(0, 19) * 格点]  # 新增变量：随机生成食物网格对齐坐标
下次移动时间 = 0
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN:
            if 事件.key == pygame.K_UP and 速度 != [0, 格点]:
                速度 = [0, -格点]
            elif 事件.key == pygame.K_DOWN and 速度 != [0, -格点]:
                速度 = [0, 格点]
            elif 事件.key == pygame.K_LEFT and 速度 != [格点, 0]:
                速度 = [-格点, 0]
            elif 事件.key == pygame.K_RIGHT and 速度 != [-格点, 0]:
                速度 = [格点, 0]

    if 当前时间 > 下次移动时间:
        下次移动时间 = 当前时间 + 120
        新蛇头 = [蛇身[0][0] + 速度[0], 蛇身[0][1] + 速度[1]]
        蛇身.insert(0, 新蛇头)
        蛇身.pop()

        if 新蛇头 == 食物:                             # 新增代码：进食判定，蛇头触碰食物后重新生成食物
            食物 = [random.randint(0, 19) * 格点, random.randint(0, 19) * 格点]

    窗口.fill((0, 0, 0))                               # 经典纯黑色背景全屏填充
    pygame.draw.rect(窗口, (255, 60, 60), (食物[0], 食物[1], 格点, 格点))  # 新增代码：绘制红色矩形食物方块

    for 节点 in 蛇身:
        pygame.draw.rect(窗口, (0, 255, 120), (节点[0], 节点[1], 格点 - 1, 格点 - 1))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定60FPS高帧率流畅运行

pygame.quit()
