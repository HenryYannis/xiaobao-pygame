import pygame

pygame.init()
窗口 = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Dino Run - Lesson 2")
时钟 = pygame.time.Clock()

地面y = 250                                           # 地面水平基准线高度
恐龙x = 100                                           # 恐龙水平固定位置
恐龙y = 200.0                                         # 恐龙垂直坐标(40x50大小，站立时y为200)
速度y = 0.0                                           # 新增变量：恐龙垂直移动速度
重力 = 0.8                                            # 新增变量：重力加速度
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 新增代码：按下空格键且在地面上时跳起
            if 恐龙y >= 200:                           # 新增代码：仅在恐龙着地时允许跳跃，防止二段跳
                速度y = -14.0                         # 新增代码：施加向上的初始起跳速度

    速度y += 重力                                     # 新增代码：速度受重力持续作用向下增加
    恐龙y += 速度y                                    # 新增代码：更新垂直位移
    if 恐龙y > 200:                                   # 新增代码：触地判定，踩在地面上不再下陷
        恐龙y = 200
        速度y = 0.0

    窗口.fill((255, 255, 255))                         # 纯白背景全屏覆盖
    pygame.draw.rect(窗口, (200, 200, 200), (0, 地面y, 600, 50))       # 绘制浅灰色平整地面(高50)
    pygame.draw.rect(窗口, (67, 160, 72), (恐龙x, int(恐龙y), 40, 50))  # 绘制翠绿色小恐龙方块(宽40, 高50)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
