import pygame, random                                # 新增代码：导入随机数模块用于反弹角度随机化

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Ball Catch - Lesson 2")
时钟 = pygame.time.Clock()

球x, 球y = 200, 50                                     # 小球初始坐标(中上方)
球速度x = 0                                            # 新增变量：小球水平初速度
球速度y = 4                                            # 小球垂直下落初速度
挡板x = 160                                           # 挡板左上角横坐标
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    球x += 球速度x                                    # 新增代码：累加横向速度实现水平位移
    球y += 球速度y                                    # 垂直位移：累加纵向速度实现垂直下落

    if 球x <= 10 or 球x >= 390:                       # 新增代码：小球碰到左右墙壁时横向速度取反反弹
        球速度x *= -1
    if 球y <= 10:                                     # 新增代码：小球碰到顶部天花板时向下反弹
        球速度y = abs(球速度y)

    if 球y >= 360 and 挡板x <= 球x <= 挡板x + 80:     # 新增代码：挡板接球判定(球到达挡板高度且在宽度区间内)
        球速度y = -5                                  # 新增代码：给球向上初速度实现反弹
        球速度x = random.randint(-3, 3)               # 新增代码：反弹时随机改变水平速度增加接球趣味

    if 球y > 400:                                     # 掉落重置：漏接掉出底部后重置球的位置与速度
        球x, 球y = 200, 50
        球速度x, 球速度y = 0, 4

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
