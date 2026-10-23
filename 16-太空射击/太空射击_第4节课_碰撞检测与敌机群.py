import pygame, random, math

pygame.init()
窗口 = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Space Shooter - Lesson 4")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 36)                     # 新增变量：纯内置默认字体(是什么)，用来显示英文 GAME OVER(为什么)，字号36(怎么用)

飞船x, 飞船y = 200, 500                               # 玩家飞船基准坐标
敌机列表 = []                                          # 敌机坐标列表[[x, y], ...]
子弹列表 = []                                          # 激光子弹坐标列表[[x, y], ...]
游戏结束 = False                                      # 新增变量：标记飞船是否被撞毁(撞毁后画面停住，而不是直接关窗口)
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if not 游戏结束 and 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 未撞毁时按空格发射
            子弹列表.append([飞船x, 飞船y - 20])      # 发射子弹：从飞船顶端生成一枚向上激光

    if not 游戏结束:                                  # 新增代码：撞毁后不再更新飞行与战斗，画面停在撞击那一刻
        按键 = pygame.key.get_pressed()
        if 按键[pygame.K_LEFT] and 飞船x > 25:        # 飞船向左移动限位
            飞船x -= 6
        if 按键[pygame.K_RIGHT] and 飞船x < 375:      # 飞船向右移动限位
            飞船x += 6

        if random.random() < 0.025:                   # 随机生成：每帧2.5%概率在顶部生成新敌机
            敌机列表.append([random.randint(25, 375), -20])

        for 索引 in range(len(敌机列表) - 1, -1, -1):  # 遍历敌机向下推进
            敌机 = 敌机列表[索引]
            敌机[1] += 3

            if math.hypot(飞船x - 敌机[0], 飞船y - 敌机[1]) <= 30:  # 新增代码：勾股定理算飞船与敌机中心距离，30以内算撞上
                游戏结束 = True                       # 新增代码：撞毁后进入结束状态(不要用 运行中 = False，那样窗口会直接消失)

            if 敌机[1] > 620:                         # 越过底部边界后销毁
                敌机列表.pop(索引)

        for 子弹索引 in range(len(子弹列表) - 1, -1, -1):  # 遍历子弹向上发射
            子弹 = 子弹列表[子弹索引]
            子弹[1] -= 8

            已命中 = False
            for 敌机索引 in range(len(敌机列表) - 1, -1, -1):  # 新增代码：嵌套循环检测子弹击中敌机
                敌机 = 敌机列表[敌机索引]
                if math.hypot(子弹[0] - 敌机[0], 子弹[1] - 敌机[1]) <= 25:  # 新增代码：激光击中敌机判定
                    敌机列表.pop(敌机索引)            # 新增代码：消灭敌机
                    已命中 = True
                    break

            if 已命中:
                子弹列表.pop(子弹索引)
            elif 子弹[1] < -10:                       # 飞出顶部边界后销毁子弹
                子弹列表.pop(子弹索引)

    窗口.fill((10, 10, 30))                           # 深空藏蓝色背景全屏填充

    飞船顶点 = [(飞船x, 飞船y - 20), (飞船x - 15, 飞船y + 15), (飞船x + 15, 飞船y + 15)]  # 三角形战机的三个顶点(机头、左翼、右翼)
    pygame.draw.polygon(窗口, (0, 200, 255), 飞船顶点)

    for 敌机 in 敌机列表:                             # 循环绘制红色圆形敌机(半径15)
        pygame.draw.circle(窗口, (255, 60, 60), 敌机, 15)

    for 子弹 in 子弹列表:                             # 循环绘制黄色高能激光子弹(半径4)
        pygame.draw.circle(窗口, (255, 220, 0), 子弹, 4)

    if 游戏结束:
        提示画面 = 字体.render("GAME OVER", True, (255, 60, 60))  # 新增代码：红色英文提示飞船被撞毁
        窗口.blit(提示画面, 提示画面.get_rect(center=(200, 300)))  # 新增代码：get_rect(center=...)让文字正好居中

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
