import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake - Lesson 2")
时钟 = pygame.time.Clock()

格点 = 20                                             # 每个网格单元的像素跨度
蛇身 = [[200, 200]]                                   # 蛇身节点列表
速度 = [格点, 0]                                      # 新增变量：初始移动方向与步长(向右)
上步方向 = 速度[:]                                    # 新增变量：蛇上一步实际走的方向，防掉头要和它比较，不能和刚按键改过的速度比
下次移动时间 = 0                                      # 新增变量：控制移动节奏的毫秒计时器
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN:                # 新增代码：按键转向与防自撞反向保护
            if 事件.key == pygame.K_UP and 上步方向 != [0, 格点]:
                速度 = [0, -格点]
            elif 事件.key == pygame.K_DOWN and 上步方向 != [0, -格点]:
                速度 = [0, 格点]
            elif 事件.key == pygame.K_LEFT and 上步方向 != [格点, 0]:
                速度 = [-格点, 0]
            elif 事件.key == pygame.K_RIGHT and 上步方向 != [-格点, 0]:
                速度 = [格点, 0]

    if 当前时间 > 下次移动时间:                       # 新增代码：定时器控制移动，每隔120毫秒移动一步
        下次移动时间 = 当前时间 + 120
        新蛇头 = [蛇身[0][0] + 速度[0], 蛇身[0][1] + 速度[1]]  # 新增代码：计算新蛇头坐标
        上步方向 = 速度[:]                            # 新增代码：这一步真的走出去了，才记下实际方向(连按两个键也不会掉头)
        蛇身.insert(0, 新蛇头)                         # 新增代码：在列表首部插入新头部(加头)
        蛇身.pop()                                    # 新增代码：移除末尾尾部(去尾维持原长)

    窗口.fill((0, 0, 0))                               # 经典纯黑色背景全屏填充
    for 节点 in 蛇身:
        pygame.draw.rect(窗口, (0, 255, 120), (节点[0], 节点[1], 格点 - 1, 格点 - 1))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定60FPS高帧率流畅运行

pygame.quit()
