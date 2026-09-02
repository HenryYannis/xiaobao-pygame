import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Click Pop - Lesson 1")
时钟 = pygame.time.Clock()

气泡列表 = []                                          # 坐标容器：存储屏幕上所有活动气泡坐标[x, y]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    if random.random() < 0.03:                         # 随机生成：每帧3%概率产生新气泡，控制出现节奏
        气泡列表.append([random.randint(20, 380), random.randint(20, 380)])

    窗口.fill((255, 255, 255))                         # 清空画布：擦除上一帧残留画面，白色RGB(255,255,255)全屏覆盖
    for 气泡 in 气泡列表:
        pygame.draw.circle(窗口, (0, 150, 255), 气泡, 20, 2)  # 绘制图形：天蓝色空心圆呈现气泡(圆心坐标, 半径20, 线宽2)

    pygame.display.flip()                              # 双缓冲刷新：将后台绘制好的画面一次性呈现在屏幕上，防闪烁
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
