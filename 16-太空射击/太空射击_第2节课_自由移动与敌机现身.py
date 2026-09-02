import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Space Shooter - Lesson 2")
时钟 = pygame.time.Clock()

飞船x, 飞船y = 200, 500                               # 玩家飞船基准坐标
敌机列表 = []                                          # 新增变量：敌机坐标列表[[x, y], ...]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    按键 = pygame.key.get_pressed()                   # 新增代码：按键控制战机左右移动
    if 按键[pygame.K_LEFT] and 飞船x > 25:
        飞船x -= 6
    if 按键[pygame.K_RIGHT] and 飞船x < 375:
        飞船x += 6

    if random.random() < 0.025:                        # 新增代码：随机在屏幕顶部生成向下俯冲的敌机
        敌机列表.append([random.randint(25, 375), -20])

    for 索引 in range(len(敌机列表) - 1, -1, -1):      # 新增代码：遍历敌机向下推进
        敌机列表[索引][1] += 3

        if 敌机列表[索引][1] > 620:                    # 移出底边后销毁
            敌机列表.pop(索引)

    窗口.fill((10, 10, 30))                           # 深空藏蓝色背景全屏填充

    飞船顶点 = [(飞船x, 飞船y - 20), (飞船x - 15, 飞船y + 15), (飞船x + 15, 飞船y + 15)]
    pygame.draw.polygon(窗口, (0, 200, 255), 飞船顶点)

    for 敌机 in 敌机列表:                              # 新增代码：循环绘制红色圆形敌机
        pygame.draw.circle(窗口, (255, 60, 60), 敌机, 15)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
