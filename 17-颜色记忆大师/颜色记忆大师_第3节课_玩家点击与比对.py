import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Memory Master - Lesson 3")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 32)                     # 创建纯内置默认字体(是什么)，避免跨平台字体报错(为什么)，字号32(怎么用)

四色列表 = [                                           # 四种基础高亮颜色(红、绿、蓝、黄)
    (255, 60, 60),
    (60, 200, 60),
    (60, 120, 255),
    (255, 220, 40)
]

游戏状态 = "准备"                                     # 状态机当前状态("准备", "演示", "答题")
记忆序列 = []
玩家序列 = []                                          # 新增变量：记录玩家点击的序列
演示索引 = 0
下次切换时间 = 0
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.MOUSEBUTTONDOWN:
            if 游戏状态 == "准备":
                记忆序列 = [random.randint(0, 3), random.randint(0, 3)]
                玩家序列 = []
                演示索引 = 0
                下次切换时间 = 当前时间 + 800
                游戏状态 = "演示"
            elif 游戏状态 == "答题":                   # 新增代码：监听答题状态下的象限点击
                鼠标x, 鼠标y = pygame.mouse.get_pos()
                if 50 <= 鼠标x <= 350 and 50 <= 鼠标y <= 275:
                    列 = 0 if 鼠标x < 200 else 1
                    行 = 0 if 鼠标y < 162 else 1
                    选号 = 行 * 2 + 列
                    玩家序列.append(选号)              # 新增代码：追加点击记录

                    if len(玩家序列) == len(记忆序列): # 新增代码：全部选完后比对
                        if 玩家序列 == 记忆序列:
                            游戏状态 = "准备"         # 答对返回准备状态
                        else:
                            玩家序列 = []              # 答错重试

    窗口.fill((40, 40, 60))                           # 深蓝灰色背景全屏填充

    if 游戏状态 == "准备":
        提示画面 = 字体.render("CLICK TO START", True, (255, 255, 255))
        窗口.blit(提示画面, (110, 130))
    elif 游戏状态 == "演示":
        if 当前时间 > 下次切换时间:
            演示索引 += 1
            下次切换时间 = 当前时间 + 600
            if 演示索引 >= len(记忆序列):
                游戏状态 = "答题"                     # 新增代码：演示完毕无缝进入答题状态

        提示画面 = 字体.render("WATCH CAREFULLY", True, (255, 220, 0))
        窗口.blit(提示画面, (100, 20))
        if 演示索引 < len(记忆序列):
            当前色 = 四色列表[记忆序列[演示索引]]
            pygame.draw.rect(窗口, 当前色, (125, 80, 150, 150))

    elif 游戏状态 == "答题":                           # 新增代码：答题阶段渲染4个选择色块
        提示画面 = 字体.render("REPEAT SEQUENCE", True, (0, 255, 150))
        窗口.blit(提示画面, (100, 15))
        for 编号 in range(4):
            横 = 50 + (编号 % 2) * 160
            纵 = 60 + (编号 // 2) * 110
            pygame.draw.rect(窗口, 四色列表[编号], (横, 纵, 140, 95))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
