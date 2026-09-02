import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Catch Fruit - Lesson 1")
时钟 = pygame.time.Clock()

篮子x = 160                                           # 篮子左上角横坐标
篮子y = 550                                           # 篮子固定纵坐标
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

    窗口.fill((135, 206, 235))                         # 天蓝色天空背景全屏覆盖
    pygame.draw.rect(窗口, (139, 69, 19), (篮子x, 篮子y, 80, 20))      # 绘制深褐色接水果篮子(宽80, 高20)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
