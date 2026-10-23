import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Memory Master - Lesson 2")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 32)                     # 创建纯内置默认字体(是什么)，避免跨平台字体报错(为什么)，字号32(怎么用)

四色列表 = [                                           # 四种基础高亮颜色(红、绿、蓝、黄)
    (255, 60, 60),
    (60, 200, 60),
    (60, 120, 255),
    (255, 220, 40)
]

游戏状态 = "准备"                                     # 状态机当前状态("准备", "演示")
记忆序列 = []                                          # 新增变量：随机记忆序列
演示索引 = 0                                          # 新增变量：当前正在演示的步骤
下次切换时间 = 0                                      # 新增变量：控制切换节奏的毫秒计时器
亮灯中 = True                                         # 新增变量：演示时当前颜色是亮着还是处于熄灭间隔，相同颜色连续出现时也能分清
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.MOUSEBUTTONDOWN and 事件.button == 1 and 游戏状态 == "准备":  # 只响应鼠标左键，滚轮和右键不算点击
            记忆序列 = [random.randint(0, 3), random.randint(0, 3)]  # 新增代码：生成2个颜色演示序列
            演示索引 = 0
            下次切换时间 = 当前时间 + 800
            亮灯中 = True
            游戏状态 = "演示"                         # 新增代码：进入演示状态

    窗口.fill((40, 40, 60))                           # 深蓝灰色背景全屏填充

    if 游戏状态 == "准备":
        提示画面 = 字体.render("CLICK TO START", True, (255, 255, 255))
        窗口.blit(提示画面, (110, 130))
    elif 游戏状态 == "演示":                           # 新增代码：逐个展示序列中的颜色方块
        if 当前时间 > 下次切换时间:
            if 亮灯中:                                # 新增代码：亮够时间了：先熄灭150毫秒，形成明显的间隔
                亮灯中 = False
                下次切换时间 = 当前时间 + 150
            else:                                     # 新增代码：熄灭间隔结束：切到下一个颜色并亮500毫秒
                演示索引 += 1
                亮灯中 = True
                下次切换时间 = 当前时间 + 500
                if 演示索引 >= len(记忆序列):
                    游戏状态 = "准备"                 # 演示结束后回到准备状态重新练习

        提示画面 = 字体.render("WATCH CAREFULLY", True, (255, 220, 0))
        窗口.blit(提示画面, 提示画面.get_rect(center=(200, 283)))  # 提示放到底部居中，不再和左上角分数重叠
        if 亮灯中 and 演示索引 < len(记忆序列):       # 新增代码：只在亮灯阶段画出颜色，熄灭阶段画面留空
            当前色 = 四色列表[记忆序列[演示索引]]
            pygame.draw.rect(窗口, 当前色, (125, 80, 150, 150))  # 中央高亮展示

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
