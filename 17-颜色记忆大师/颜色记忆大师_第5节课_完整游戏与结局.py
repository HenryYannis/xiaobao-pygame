import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Memory Master - Lesson 5")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 32)                     # 创建纯内置默认字体(是什么)，避免跨平台字体报错(为什么)，字号32(怎么用)

四色列表 = [                                           # 四种基础高亮颜色(红、绿、蓝、黄)
    (255, 60, 60),
    (60, 200, 60),
    (60, 120, 255),
    (255, 220, 40)
]

游戏状态 = "准备"                                     # 状态机当前状态("准备", "演示", "答题", "失败")
记忆序列 = []                                          # 电脑随机生成的目标颜色编号序列[0, 2, 1, ...]
玩家序列 = []                                          # 玩家按顺序点击输入的颜色编号序列
得分 = 0                                              # 累计答对轮数得分
演示索引 = 0                                          # 当前正在高亮演示的序列下标
下次切换时间 = 0                                      # 控制序列逐个亮起间隔的毫秒时间戳
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.MOUSEBUTTONDOWN:
            if 游戏状态 == "准备":
                记忆序列 = [random.randint(0, 3)]     # 生成第一关单颜色序列
                玩家序列 = []
                演示索引 = 0
                下次切换时间 = 当前时间 + 800
                游戏状态 = "演示"
            elif 游戏状态 == "答题":
                鼠标x, 鼠标y = pygame.mouse.get_pos()  # 根据点击坐标判断点击了哪个象限的方块(0红1绿2蓝3黄)
                if 50 <= 鼠标x <= 350 and 50 <= 鼠标y <= 275:
                    列 = 0 if 鼠标x < 200 else 1
                    行 = 0 if 鼠标y < 162 else 1
                    选号 = 行 * 2 + 列
                    玩家序列.append(选号)

                    # 实时比对最新落子是否正确
                    当前步 = len(玩家序列) - 1
                    if 玩家序列[当前步] != 记忆序列[当前步]:  # 新增代码：点错立即判定挑战失败
                        游戏状态 = "失败"
                    elif len(玩家序列) == len(记忆序列):     # 本轮全部点对，通关升级
                        得分 += 10
                        记忆序列.append(random.randint(0, 3)) # 序列增加一节新颜色
                        玩家序列 = []
                        演示索引 = 0
                        下次切换时间 = 当前时间 + 800
                        游戏状态 = "演示"

        if 游戏状态 == "失败" and 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 新增代码：失败后按空格重开
            得分 = 0
            游戏状态 = "准备"

    窗口.fill((40, 40, 60))                           # 深蓝灰色背景全屏填充

    if 游戏状态 == "准备":
        提示画面 = 字体.render("CLICK TO START", True, (255, 255, 255))
        窗口.blit(提示画面, (110, 130))
    elif 游戏状态 == "演示":
        if 当前时间 > 下次切换时间:
            演示索引 += 1
            下次切换时间 = 当前时间 + 600
            if 演示索引 >= len(记忆序列):
                游戏状态 = "答题"

        提示画面 = 字体.render("WATCH CAREFULLY", True, (255, 220, 0))
        窗口.blit(提示画面, (100, 20))
        if 演示索引 < len(记忆序列):
            当前色 = 四色列表[记忆序列[演示索引]]
            pygame.draw.rect(窗口, 当前色, (125, 80, 150, 150))  # 在中央放大高亮展示当前正在演示的颜色

    elif 游戏状态 == "答题":
        提示画面 = 字体.render("REPEAT SEQUENCE", True, (0, 255, 150))
        窗口.blit(提示画面, (100, 15))
        for 编号 in range(4):                          # 绘制四色可点击按钮
            横 = 50 + (编号 % 2) * 160
            纵 = 60 + (编号 // 2) * 110
            pygame.draw.rect(窗口, 四色列表[编号], (横, 纵, 140, 95))

    elif 游戏状态 == "失败":                           # 新增代码：失败结算界面展示
        提示画面 = 字体.render("GAME OVER - Press SPACE", True, (255, 60, 60))
        窗口.blit(提示画面, (40, 130))

    得分画面 = 字体.render(f"SCORE: {得分}", True, (255, 255, 255))
    窗口.blit(得分画面, (10, 10))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
