import pygame, math, random

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Gold Miner - Lesson 4")
时钟 = pygame.time.Clock()

锚点x, 锚点y = 200, 50                                 # 矿工绳索顶部悬挂中心固定锚点坐标
绳长 = 50.0                                           # 绳索当前伸缩长度
角度 = 0.0                                            # 钩子摆动角度
钩子状态 = "摆动"                                     # 钩子状态("摆动", "出钩", "收钩")
金块列表 = [[random.randint(60, 340), random.randint(160, 350), random.randint(12, 28)] for _ in range(5)]
抓到金块 = None                                       # 新增变量：记录当前锁定的金块对象[x, y, 半径]
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:
            if 钩子状态 == "摆动":
                钩子状态 = "出钩"

    if 钩子状态 == "摆动":
        角度 = math.sin(当前时间 / 500.0) * 75.0
    elif 钩子状态 == "出钩":
        绳长 += 6.0
    elif 钩子状态 == "收钩":
        # 新增代码：金块越大收绳速度越慢(模拟重物负荷)
        收绳速度 = max(1.5, 6.0 - (抓到金块[2] / 6.0 if 抓到金块 else 0))
        绳长 -= 收绳速度
        if 绳长 <= 50.0:
            抓到金块 = None                           # 新增代码：收回后释放金块
            绳长 = 50.0
            钩子状态 = "摆动"

    弧度 = math.radians(角度 + 90.0)
    钩尖x = 锚点x + 绳长 * math.cos(弧度)
    钩尖y = 锚点y + 绳长 * math.sin(弧度)

    if 钩子状态 == "出钩":
        if 钩尖x < 10 or 钩尖x > 390 or 钩尖y > 390:
            钩子状态 = "收钩"

        # 新增代码：钩尖碰撞金块抓取判定
        for 索引 in range(len(金块列表) - 1, -1, -1):
            金块 = 金块列表[索引]
            if math.hypot(钩尖x - 金块[0], 钩尖y - 金块[1]) < 金块[2]:
                抓到金块 = 金块列表.pop(索引)           # 新增代码：拔出金块
                钩子状态 = "收钩"                     # 新增代码：切换为收钩
                break

    窗口.fill((245, 235, 195))                         # 暖沙黄色地下矿洞背景全屏填充

    for 金块 in 金块列表:
        pygame.draw.circle(窗口, (255, 200, 0), (金块[0], 金块[1]), 金块[2])

    if 抓到金块:                                       # 新增代码：绘制钩尖上锁定的金块
        pygame.draw.circle(窗口, (255, 200, 0), (int(钩尖x), int(钩尖y)), 抓到金块[2])

    pygame.draw.line(窗口, (70, 50, 30), (锚点x, 锚点y), (钩尖x, 钩尖y), 3)
    pygame.draw.circle(窗口, (120, 120, 120), (int(钩尖x), int(钩尖y)), 6)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
