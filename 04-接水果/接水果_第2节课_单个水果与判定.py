import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Catch Fruit - Lesson 2")
时钟 = pygame.time.Clock()

篮子x = 160                                           # 篮子左上角横坐标
篮子y = 550                                           # 篮子固定纵坐标
水果 = [200, 0]                                       # 新增变量：单个水果初始位置[x, y]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    按键 = pygame.key.get_pressed()                   # 监听键盘方向键连续按下状态
    if 按键[pygame.K_LEFT] and 篮子x > 0:             # 篮子左移且不越出左边界
        篮子x -= 6
    if 按键[pygame.K_RIGHT] and 篮子x < 320:          # 篮子右移且不越出右边界(400 - 宽度80 = 320)
        篮子x += 6

    水果[1] += 4                                      # 新增代码：水果垂直下落更新

    if 篮子y - 15 <= 水果[1] <= 篮子y + 5 and 篮子x <= 水果[0] <= 篮子x + 80:  # 新增代码：接住判定，重置新水果到顶部(只在篮口附近20像素内算接住，掉过篮子就捞不回来)
        水果 = [random.randint(20, 380), 0]
    elif 水果[1] > 600:                                # 新增代码：掉落底部后重置新水果(初课练习循环)
        水果 = [random.randint(20, 380), 0]

    窗口.fill((135, 206, 235))                         # 天蓝色天空背景全屏覆盖
    pygame.draw.rect(窗口, (139, 69, 19), (篮子x, 篮子y, 80, 20))      # 绘制深褐色接水果篮子(宽80, 高20)
    pygame.draw.circle(窗口, (255, 50, 50), 水果, 15)  # 新增代码：绘制红色圆形小水果(圆心, 半径15)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
