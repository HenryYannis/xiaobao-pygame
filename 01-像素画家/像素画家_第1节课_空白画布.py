import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 460))
pygame.display.set_caption("Pixel Painter - Lesson 1")
时钟 = pygame.time.Clock()

画布 = [[0 for _ in range(10)] for _ in range(10)]     # 二维画布数据：10行10列网格，存储每个格子的状态(0代表白色)
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    窗口.fill((200, 200, 200))                         # 浅灰色背景：充当网格间隙与底部分割线外框

    for 行 in range(10):                               # 嵌套循环：遍历二维画布的所有行与列
        for 列 in range(10):
            pygame.draw.rect(窗口, (255, 255, 255), (列 * 40 + 2, 行 * 40 + 2, 36, 36))  # 绘制带2像素外边框的36x36白色方格

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
