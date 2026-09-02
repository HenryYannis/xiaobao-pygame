import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Flappy Bird - Lesson 2")
时钟 = pygame.time.Clock()

小鸟x = 60                                             # 小鸟水平固定横坐标
小鸟y = 250.0                                         # 小鸟垂直当前高度
速度y = 0.0                                           # 小鸟垂直移动速度
管道列表 = []                                          # 新增变量：存储管道数据列表[[x, 间隙上边缘y], ...]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:
            速度y = -7.0

    速度y += 0.4
    小鸟y += 速度y

    if 小鸟y > 485:
        小鸟y = 485
        速度y = 0.0
    elif 小鸟y < 15:
        小鸟y = 15
        速度y = 0.0

    if len(管道列表) == 0 or 管道列表[-1][0] < 220:      # 新增代码：间距控制，每隔一定距离生成新管道
        管道列表.append([400, random.randint(80, 280)])

    for 索引 in range(len(管道列表) - 1, -1, -1):      # 新增代码：遍历管道向左移动
        管道列表[索引][0] -= 4

        if 管道列表[索引][0] < -60:                    # 新增代码：移出左边界后安全销毁
            管道列表.pop(索引)

    窗口.fill((100, 200, 255))                         # 蓝天背景全屏填充
    pygame.draw.circle(窗口, (255, 220, 0), (小鸟x, int(小鸟y)), 15)  # 绘制黄色圆形小鸟(半径15)

    for 管道 in 管道列表:                              # 新增代码：循环绘制上下绿色障碍管道
        pygame.draw.rect(窗口, (30, 160, 50), (管道[0], 0, 50, 管道[1]))
        pygame.draw.rect(窗口, (30, 160, 50), (管道[0], 管道[1] + 120, 50, 500))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
