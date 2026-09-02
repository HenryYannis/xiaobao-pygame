import pygame, math

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Gold Miner - Lesson 2")
时钟 = pygame.time.Clock()

锚点x, 锚点y = 200, 50                                 # 矿工绳索顶部悬挂中心固定锚点坐标
绳长 = 50.0                                           # 绳索当前伸缩长度
角度 = 0.0                                            # 钩子摆动角度
钩子状态 = "摆动"                                     # 新增变量：钩子状态("摆动", "出钩", "收钩")
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 新增代码：按空格释放飞钩
            if 钩子状态 == "摆动":
                钩子状态 = "出钩"

    if 钩子状态 == "摆动":
        角度 = math.sin(当前时间 / 500.0) * 75.0
    elif 钩子状态 == "出钩":                           # 新增代码：沿角度直线伸长
        绳长 += 6.0
    elif 钩子状态 == "收钩":                           # 新增代码：匀速收回
        绳长 -= 6.0
        if 绳长 <= 50.0:
            绳长 = 50.0
            钩子状态 = "摆动"

    弧度 = math.radians(角度 + 90.0)
    钩尖x = 锚点x + 绳长 * math.cos(弧度)
    钩尖y = 锚点y + 绳长 * math.sin(弧度)

    if 钩子状态 == "出钩":                             # 新增代码：出界判定转入收钩
        if 钩尖x < 10 or 钩尖x > 390 or 钩尖y > 390:
            钩子状态 = "收钩"

    窗口.fill((245, 235, 195))                         # 暖沙黄色地下矿洞背景全屏填充

    pygame.draw.line(窗口, (70, 50, 30), (锚点x, 锚点y), (钩尖x, 钩尖y), 3)
    pygame.draw.circle(窗口, (120, 120, 120), (int(钩尖x), int(钩尖y)), 6)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
