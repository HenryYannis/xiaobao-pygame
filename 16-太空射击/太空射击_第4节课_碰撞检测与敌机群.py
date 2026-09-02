import pygame, random, math

pygame.init()
窗口 = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Space Shooter - Lesson 4")
时钟 = pygame.time.Clock()

飞船x, 飞船y = 200, 500                               # 玩家飞船基准坐标
敌机列表 = []                                          # 敌机坐标列表[[x, y], ...]
子弹列表 = []                                          # 激光子弹坐标列表[[x, y], ...]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:
            子弹列表.append([飞船x, 飞船y - 20])

    按键 = pygame.key.get_pressed()
    if 按键[pygame.K_LEFT] and 飞船x > 25:
        飞船x -= 6
    if 按键[pygame.K_RIGHT] and 飞船x < 375:
        飞船x += 6

    if random.random() < 0.025:
        敌机列表.append([random.randint(25, 375), -20])

    for 索引 in range(len(敌机列表) - 1, -1, -1):
        敌机 = 敌机列表[索引]
        敌机[1] += 3

        if math.hypot(飞船x - 敌机[0], 飞船y - 敌机[1]) <= 30:  # 新增代码：飞船与敌机撞击检测
            运行中 = False

        if 敌机[1] > 620:
            敌机列表.pop(索引)

    for 子弹索引 in range(len(子弹列表) - 1, -1, -1):
        子弹 = 子弹列表[子弹索引]
        子弹[1] -= 8

        已命中 = False
        for 敌机索引 in range(len(敌机列表) - 1, -1, -1):  # 新增代码：嵌套循环检测子弹击中敌机
            敌机 = 敌机列表[敌机索引]
            if math.hypot(子弹[0] - 敌机[0], 子弹[1] - 敌机[1]) <= 25:
                敌机列表.pop(敌机索引)                 # 新增代码：消灭敌机
                已命中 = True
                break

        if 已命中:
            子弹列表.pop(子弹索引)
        elif 子弹[1] < -10:
            子弹列表.pop(子弹索引)

    窗口.fill((10, 10, 30))                           # 深空藏蓝色背景全屏填充

    飞船顶点 = [(飞船x, 飞船y - 20), (飞船x - 15, 飞船y + 15), (飞船x + 15, 飞船y + 15)]
    pygame.draw.polygon(窗口, (0, 200, 255), 飞船顶点)

    for 敌机 in 敌机列表:
        pygame.draw.circle(窗口, (255, 60, 60), 敌机, 15)

    for 子弹 in 子弹列表:
        pygame.draw.circle(窗口, (255, 220, 0), 子弹, 4)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
