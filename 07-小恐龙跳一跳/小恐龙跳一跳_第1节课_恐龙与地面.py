import pygame

pygame.init()
窗口 = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Dino Run - Lesson 1")
时钟 = pygame.time.Clock()

地面y = 250                                           # 地面水平基准线高度
恐龙x = 100                                           # 恐龙水平固定位置
恐龙y = 200                                           # 恐龙垂直坐标(40x50大小，站立时y为200)
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    窗口.fill((255, 255, 255))                         # 纯白背景全屏覆盖
    pygame.draw.rect(窗口, (200, 200, 200), (0, 地面y, 600, 50))       # 绘制浅灰色平整地面(高50)
    pygame.draw.rect(窗口, (67, 160, 72), (恐龙x, 恐龙y, 40, 50))       # 绘制翠绿色小恐龙方块(宽40, 高50)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
