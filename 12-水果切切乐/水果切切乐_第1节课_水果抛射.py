import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Fruit Slice - Lesson 1")
时钟 = pygame.time.Clock()

水果列表 = []                                          # 存储所有抛出的水果数据[x, y, 水平速度, 垂直速度]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    if random.random() < 0.03:                         # 随机生成：每帧3%概率从底部向上抛出新水果
        水果列表.append([random.randint(50, 350), 410, random.uniform(-2, 2), -9.0])

    for 索引 in range(len(水果列表) - 1, -1, -1):      # 倒序遍历水果列表，防止pop删除元素时索引越界
        水果 = 水果列表[索引]
        水果[0] += 水果[2]                             # 坐标更新：累加水平移动速度
        水果[1] += 水果[3]                             # 坐标更新：累加垂直移动速度
        水果[3] += 0.25                                # 重力模拟：垂直速度每帧增加，形成下落抛物线

        if 水果[1] > 420:                              # 掉落销毁：水果掉出屏幕底部边界后从列表移除
            水果列表.pop(索引)

    窗口.fill((20, 20, 20))                           # 暗色背景：RGB深灰黑(20, 20, 20)全屏填充
    for 水果 in 水果列表:
        pygame.draw.circle(窗口, (255, 140, 0), (int(水果[0]), int(水果[1])), 20)  # 绘制橙色水果(半径20)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
