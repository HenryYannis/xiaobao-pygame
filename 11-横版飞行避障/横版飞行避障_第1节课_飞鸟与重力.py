import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Flappy Bird - Lesson 1")
时钟 = pygame.time.Clock()

小鸟x = 60                                             # 小鸟水平固定横坐标
小鸟y = 250.0                                         # 小鸟垂直当前高度
速度y = 0.0                                           # 小鸟垂直移动速度
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:
            速度y = -7.0                              # 按空格键给予向上初速度煽动起飞

    速度y += 0.4                                      # 重力持续向下微增速度
    小鸟y += 速度y                                    # 更新小鸟垂直高度

    if 小鸟y > 485:                                   # 触底保护：掉到底部后限制在地面
        小鸟y = 485
        速度y = 0.0
    elif 小鸟y < 15:                                  # 碰顶限制
        小鸟y = 15
        速度y = 0.0

    窗口.fill((100, 200, 255))                         # 蓝天背景全屏填充
    pygame.draw.circle(窗口, (255, 220, 0), (小鸟x, int(小鸟y)), 15)  # 绘制黄色圆形小鸟(半径15)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
