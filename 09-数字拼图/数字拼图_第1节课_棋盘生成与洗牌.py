import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Number Puzzle - Lesson 1")
时钟 = pygame.time.Clock()
大字体 = pygame.font.Font(None, 50)                   # 创建绘制数字的纯内置默认字体

数字列表 = [1, 2, 3, 4, 5, 6, 7, 8, 0]                 # 3x3拼图列表，0代表右下角空位

def 随机打乱(列表):                                   # 通过有效相邻滑块交换打乱，保证100%可解性
    for _ in range(60):
        空位 = 列表.index(0)
        空行, 空列 = 空位 // 3, 空位 % 3
        可选邻居 = []
        for 偏行, 偏列 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            新行, 新列 = 空行 + 偏行, 空列 + 偏列
            if 0 <= 新行 < 3 and 0 <= 新列 < 3:
                可选邻居.append(新行 * 3 + 新列)
        交换目标 = random.choice(可选邻居)
        列表[空位], 列表[交换目标] = 列表[交换目标], 列表[空位]
    if 列表 == [1, 2, 3, 4, 5, 6, 7, 8, 0]:           # 打乱60步后有极小概率恰好回到已还原的样子
        随机打乱(列表)                                # 那就让函数自己调用自己，再打乱一次

随机打乱(数字列表)
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    窗口.fill((240, 240, 240))                         # 浅灰色背景全屏填充

    for 索引 in range(9):                              # 遍历绘制9个网格方块
        行 = 索引 // 3
        列 = 索引 % 3
        数字 = 数字列表[索引]
        if 数字 != 0:
            pygame.draw.rect(窗口, (200, 200, 200), (列 * 100 + 5, 行 * 100 + 5, 90, 90))
            数字画面 = 大字体.render(str(数字), True, (0, 0, 0))  # 默认字体渲染数字图像
            文字位置 = (列 * 100 + 36, 行 * 100 + 28)
            窗口.blit(数字画面, 文字位置)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
