import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake - Lesson 1")
时钟 = pygame.time.Clock()

格点 = 20                                             # 每个网格单元的像素跨度
蛇身 = [[200, 200]]                                   # 蛇身节点列表，初始只有位于中央的单个蛇头
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    窗口.fill((0, 0, 0))                               # 经典纯黑色背景全屏填充
    for 节点 in 蛇身:                                  # 绘制蛇身初始节点方块
        pygame.draw.rect(窗口, (0, 255, 120), (节点[0], 节点[1], 格点 - 1, 格点 - 1))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定60FPS高帧率流畅运行

pygame.quit()
