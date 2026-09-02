import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Rhythm Block - Lesson 1")
时钟 = pygame.time.Clock()

方块列表 = []                                          # 活动节奏方块列表[[x, y], ...]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    if random.random() < 0.02:                         # 随机生成：每帧2%概率在中央轨道生成下落方块
        方块列表.append([175, -50])

    for 索引 in range(len(方块列表) - 1, -1, -1):      # 倒序遍历方块下落移动
        方块列表[索引][1] += 5                        # 垂直下落位移

        if 方块列表[索引][1] > 600:                    # 掉落销毁：方块穿过判定线掉出底部
            方块列表.pop(索引)

    窗口.fill((30, 30, 30))                           # 暗灰黑色背景全屏填充
    pygame.draw.line(窗口, (120, 120, 120), (0, 500), (400, 500), 4)  # 绘制位于y=500高度的灰色节奏判定横线

    for 方块 in 方块列表:                              # 绘制所有下落的蓝色霓虹方块
        pygame.draw.rect(窗口, (0, 200, 255), (方块[0], 方块[1], 50, 50))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
