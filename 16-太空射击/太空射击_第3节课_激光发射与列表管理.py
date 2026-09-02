import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Space Shooter - Lesson 3")
时钟 = pygame.time.Clock()

飞船x, 飞船y = 200, 500                               # 玩家飞船基准坐标
敌机列表 = []                                          # 敌机坐标列表[[x, y], ...]
子弹列表 = []                                          # 新增变量：激光子弹坐标列表[[x, y], ...]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 新增代码：按空格键发射激光子弹
            子弹列表.append([飞船x, 飞船y - 20])

    按键 = pygame.key.get_pressed()
    if 按键[pygame.K_LEFT] and 飞船x > 25:
        飞船x -= 6
    if 按键[pygame.K_RIGHT] and 飞船x < 375:
        飞船x += 6

    if random.random() < 0.025:
        敌机列表.append([random.randint(25, 375), -20])

    for 索引 in range(len(敌机列表) - 1, -1, -1):
        敌机列表[索引][1] += 3

        if 敌机列表[索引][1] > 620:
            敌机列表.pop(索引)

    for 子弹索引 in range(len(子弹列表) - 1, -1, -1):  # 新增代码：遍历子弹向上发射并销毁越界子弹
        子弹列表[子弹索引][1] -= 8

        if 子弹列表[子弹索引][1] < -10:                # 飞出顶部后销毁
            子弹列表.pop(子弹索引)

    窗口.fill((10, 10, 30))                           # 深空藏蓝色背景全屏填充

    飞船顶点 = [(飞船x, 飞船y - 20), (飞船x - 15, 飞船y + 15), (飞船x + 15, 飞船y + 15)]
    pygame.draw.polygon(窗口, (0, 200, 255), 飞船顶点)

    for 敌机 in 敌机列表:
        pygame.draw.circle(窗口, (255, 60, 60), 敌机, 15)

    for 子弹 in 子弹列表:                              # 新增代码：循环绘制黄色激光子弹
        pygame.draw.circle(窗口, (255, 220, 0), 子弹, 4)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
