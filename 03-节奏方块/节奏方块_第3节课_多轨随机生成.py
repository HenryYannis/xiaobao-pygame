import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Rhythm Block - Lesson 3")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 36)                     # 新增变量：纯内置默认字体(是什么)，用来在轨道下方显示按键字母(为什么)，字号36(怎么用)

方块列表 = []                                          # 活动节奏方块列表[[x, y], ...]
轨道列表 = [75, 175, 275]                             # 新增变量：三条下落轨道的固定横坐标(方块宽度50)
按键轨道 = {pygame.K_d: 0, pygame.K_f: 1, pygame.K_j: 2}  # 新增变量：字典把按键对应到轨道序号，D左、F中、J右
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key in 按键轨道:  # 新增代码：按下 D/F/J 中的一个键才触发打击
            轨道x = 轨道列表[按键轨道[事件.key]]      # 新增代码：查字典得到这个键负责的那条轨道的横坐标
            for 索引 in range(len(方块列表) - 1, -1, -1):  # 倒序遍历方块
                方块 = 方块列表[索引]
                if 方块[0] == 轨道x and abs(方块[1] + 25 - 500) <= 35:  # 新增代码：必须是同一条轨道，且方块中心离判定线35像素内
                    方块列表.pop(索引)                # 命中并移除方块
                    break

    if random.random() < 0.025:                        # 新增代码：随机选择三条轨道之一生成下落方块
        方块列表.append([random.choice(轨道列表), -50])

    for 索引 in range(len(方块列表) - 1, -1, -1):     # 倒序遍历方块下落移动
        方块列表[索引][1] += 5                        # 垂直下落位移

        if 方块列表[索引][1] > 600:                   # 掉落销毁：方块穿过判定线掉出底部
            方块列表.pop(索引)

    窗口.fill((30, 30, 30))                           # 暗灰黑色背景全屏填充
    pygame.draw.line(窗口, (120, 120, 120), (0, 500), (400, 500), 4)  # 绘制位于y=500高度的灰色节奏判定横线

    for 方块 in 方块列表:                             # 绘制所有下落的蓝色霓虹方块
        pygame.draw.rect(窗口, (0, 200, 255), (方块[0], 方块[1], 50, 50))

    for 字母, 轨道x in zip("DFJ", 轨道列表):          # 新增代码：zip把字母和轨道横坐标一一配对
        字母画面 = 字体.render(字母, True, (150, 150, 150))
        窗口.blit(字母画面, 字母画面.get_rect(center=(轨道x + 25, 550)))  # 新增代码：字母居中显示在每条轨道正下方

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
