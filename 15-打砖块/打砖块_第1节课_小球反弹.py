import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Breakout - Lesson 1")
时钟 = pygame.time.Clock()

球 = [200, 200]                                       # 小球当前坐标[x, y]
速度 = [3, 3]                                         # 小球水平与垂直速度[vx, vy]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    球[0] += 速度[0]                                  # 更新小球水平位移
    球[1] += 速度[1]                                  # 更新小球垂直位移

    if 球[0] <= 10 or 球[0] >= 390:                   # 左右墙壁碰撞：水平速度取反反弹
        速度[0] *= -1
    if 球[1] <= 10 or 球[1] >= 390:                   # 上下墙壁碰撞：垂直速度取反反弹(初课循环体验)
        速度[1] *= -1

    窗口.fill((20, 20, 20))                           # 暗色背景全屏填充覆盖
    pygame.draw.circle(窗口, (255, 255, 255), (int(球[0]), int(球[1])), 10)  # 绘制白色小球(圆心, 半径10)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
