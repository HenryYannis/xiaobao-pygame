import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Rhythm Block - Lesson 4")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 36)                     # 新增变量：纯内置默认字体(是什么)，避免跨平台字体报错(为什么)，字号36(怎么用)

方块列表 = []                                          # 活动节奏方块列表[[x, y], ...]
轨道列表 = [75, 175, 275]                             # 三条下落轨道的固定横坐标(方块宽度50)
得分 = 0                                              # 新增变量：累计命中得分
连击数 = 0                                            # 新增变量：连续完美命中的连击次数
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 监听空格键判定打击
            命中 = False                              # 命中标志位
            for 索引 in range(len(方块列表) - 1, -1, -1):
                方块 = 方块列表[索引]
                if abs(方块[1] + 25 - 500) <= 35:      # 判定区间：方块中心(y+25)与判定线(y=500)的距离在35像素内
                    方块列表.pop(索引)                 # 击中消除方块
                    命中 = True
                    连击数 += 1                       # 新增代码：连击数累加1
                    得分 += 10 * 连击数               # 新增代码：连击越多单次得分越高(乘数奖励)
                    break
            if not 命中:                              # 新增代码：落空打偏中断连击
                连击数 = 0

    if random.random() < 0.025:                        # 随机生成：每帧2.5%概率随机在三条轨道之一生成下落方块
        方块列表.append([random.choice(轨道列表), -50])

    for 索引 in range(len(方块列表) - 1, -1, -1):      # 倒序遍历移动方块并清理越界方块
        方块列表[索引][1] += 5                        # 垂直下落位移

        if 方块列表[索引][1] > 600:                    # 掉落销毁：方块穿过判定线掉出底部
            方块列表.pop(索引)
            连击数 = 0                                # 新增代码：漏接方块清零连击

    窗口.fill((30, 30, 30))                           # 暗灰黑色背景全屏填充
    pygame.draw.line(窗口, (120, 120, 120), (0, 500), (400, 500), 4)  # 绘制位于y=500高度的灰色节奏判定横线

    for 方块 in 方块列表:                              # 绘制所有下落的蓝色霓虹方块
        pygame.draw.rect(窗口, (0, 200, 255), (方块[0], 方块[1], 50, 50))

    得分画面 = 字体.render(f"SCORE: {得分}", True, (255, 255, 255))   # 新增代码：默认字体渲染纯英文得分
    窗口.blit(得分画面, (10, 10))

    if 连击数 > 1:                                     # 新增代码：连击数大于1时展示金黄色连击英文提示
        连击画面 = 字体.render(f"{连击数} COMBO!", True, (255, 220, 0))
        窗口.blit(连击画面, (140, 100))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
