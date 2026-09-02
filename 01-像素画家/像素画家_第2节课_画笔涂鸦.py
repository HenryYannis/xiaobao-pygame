import pygame

pygame.init()
窗口 = pygame.display.set_mode((400, 460))
pygame.display.set_caption("Pixel Painter - Lesson 2")
时钟 = pygame.time.Clock()

画布 = [[0 for _ in range(10)] for _ in range(10)]     # 二维画布数据：10行10列网格，存储每个格子的状态(0白1黑)
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    if pygame.mouse.get_pressed()[0]:                  # 新增代码：监听鼠标左键按住状态，支持连续画线涂色
        鼠标x, 鼠标y = pygame.mouse.get_pos()          # 新增代码：获取鼠标当前坐标
        if 鼠标y < 400:                                # 新增代码：限制在上方400x400画布范围内
            列 = 鼠标x // 40                           # 新增代码：索引换算，鼠标横坐标整除40得到列索引
            行 = 鼠标y // 40                           # 新增代码：索引换算，鼠标纵坐标整除40得到行索引
            if 0 <= 列 < 10 and 0 <= 行 < 10:          # 新增代码：防止坐标临界值导致数组越界
                画布[行][列] = 1                       # 新增代码：修改格点状态，1代表涂黑

    窗口.fill((200, 200, 200))                         # 浅灰色背景：充当网格间隙与底部分割线外框

    for 行 in range(10):                               # 嵌套循环：遍历二维画布的所有行与列
        for 列 in range(10):
            颜色 = (0, 0, 0) if 画布[行][列] == 1 else (255, 255, 255)  # 新增代码：根据格子状态决定显示黑白颜色
            pygame.draw.rect(窗口, 颜色, (列 * 40 + 2, 行 * 40 + 2, 36, 36))  # 绘制带2像素外边框的36x36像素格点

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
