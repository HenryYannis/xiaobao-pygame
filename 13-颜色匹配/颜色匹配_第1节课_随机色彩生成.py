import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Color Match - Lesson 1")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 36)                     # 创建纯内置默认字体(是什么)，避免跨平台字体报错(为什么)，字号36(怎么用)

颜色列表 = [
    (255, 50, 50),                                    # 鲜红色
    (50, 200, 50),                                    # 翠绿色
    (50, 120, 255),                                   # 天蓝色
    (255, 200, 30),                                   # 明黄色
    (200, 50, 220)                                    # 紫罗兰色
]

def 生成题目():                                       # 题库生成函数：随机抽取两个互不相同的备选颜色并指定目标
    选色1, 选色2 = random.sample(range(len(颜色列表)), 2)
    正确答案 = random.choice([选色1, 选色2])
    return 选色1, 选色2, 正确答案

选项1, 选项2, 目标答案 = 生成题目()
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    窗口.fill((255, 255, 255))                         # 纯白背景全屏清屏覆盖

    目标标题 = 字体.render("TARGET", True, (80, 80, 80))
    窗口.blit(目标标题, (150, 20))                    # 绘制顶部英文目标提示
    pygame.draw.rect(窗口, 颜色列表[目标答案], (150, 60, 100, 50))              # 绘制目标颜色矩形(宽100, 高50)

    pygame.draw.rect(窗口, 颜色列表[选项1], (50, 160, 120, 80))                 # 绘制左侧候选颜色方块(宽120, 高80)
    pygame.draw.rect(窗口, 颜色列表[选项2], (230, 160, 120, 80))                # 绘制右侧候选颜色方块(宽120, 高80)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
