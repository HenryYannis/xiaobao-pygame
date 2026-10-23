import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake - Lesson 4")
时钟 = pygame.time.Clock()

格点 = 20                                             # 每个网格单元的像素跨度
蛇身 = [[200, 200], [180, 200], [160, 200]]           # 蛇身节点列表，初始设置3节
速度 = [格点, 0]                                      # 初始移动方向与步长
上步方向 = 速度[:]                                    # 蛇上一步实际走的方向，防掉头要和它比较，不能和刚按键改过的速度比

def 生成食物():                                       # 随机挑一个格子放食物，落在蛇身上就重新挑
    while True:
        点 = [random.randint(0, 19) * 格点, random.randint(0, 19) * 格点]  # 随机生成对齐格点的坐标
        if 点 not in 蛇身:                            # 不在蛇身上才算合格
            return 点

食物 = 生成食物()
下次移动时间 = 0
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN:
            if 事件.key == pygame.K_UP and 上步方向 != [0, 格点]:
                速度 = [0, -格点]
            elif 事件.key == pygame.K_DOWN and 上步方向 != [0, -格点]:
                速度 = [0, 格点]
            elif 事件.key == pygame.K_LEFT and 上步方向 != [格点, 0]:
                速度 = [-格点, 0]
            elif 事件.key == pygame.K_RIGHT and 上步方向 != [-格点, 0]:
                速度 = [格点, 0]

    if 当前时间 > 下次移动时间:
        下次移动时间 = 当前时间 + 120
        新蛇头 = [蛇身[0][0] + 速度[0], 蛇身[0][1] + 速度[1]]
        上步方向 = 速度[:]                            # 这一步真的走出去了，才记下实际方向(连按两个键也不会掉头)
        蛇身.insert(0, 新蛇头)

        if 新蛇头 == 食物:                             # 进食判定：吃到食物不执行pop去尾，实现长度增长
            食物 = 生成食物()
        else:
            蛇身.pop()                                # 未吃到食物时去尾维持原长

    窗口.fill((0, 0, 0))                               # 经典纯黑色背景全屏填充
    pygame.draw.rect(窗口, (255, 60, 60), (食物[0], 食物[1], 格点, 格点))

    for 序号, 节点 in enumerate(蛇身):                 # 新增代码：区分绘制蛇头与躯干颜色
        颜色 = (0, 255, 120) if 序号 == 0 else (0, 180, 80)  # 新增代码：蛇头亮绿、躯干深绿
        pygame.draw.rect(窗口, 颜色, (节点[0], 节点[1], 格点 - 1, 格点 - 1))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定60FPS高帧率流畅运行

pygame.quit()
