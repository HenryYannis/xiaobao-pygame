import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Ball Catch - Lesson 1")
时钟 = pygame.time.Clock()

球x, 球y = 200, 50                                     # 小球初始坐标(中上方)
球速度y = 3                                           # 小球垂直下落速度
挡板x = 160                                           # 挡板左上角横坐标
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    球y += 球速度y                                    # 垂直位移：每帧累加垂直速度实现下落
    if 球y > 400:                                     # 练习循环：小球掉出屏幕底部后重置回顶部
        球y = 0

    按键 = pygame.key.get_pressed()                   # 获取键盘连续按下状态
    if 按键[pygame.K_LEFT] and 挡板x > 0:             # 挡板左移且防止移出左边界
        挡板x -= 6
    if 按键[pygame.K_RIGHT] and 挡板x < 320:          # 挡板右移且防止移出右边界(400 - 宽度80 = 320)
        挡板x += 6

    窗口.fill((30, 30, 30))                           # 深灰黑背景：RGB颜色(30, 30, 30)全屏覆盖
    pygame.draw.circle(窗口, (255, 255, 255), (球x, 球y), 10)  # 绘制白色小球(圆心, 半径10)
    pygame.draw.rect(窗口, (0, 255, 100), (挡板x, 370, 80, 10))  # 绘制翠绿色挡板(矩形左上角, 宽80, 高10)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
