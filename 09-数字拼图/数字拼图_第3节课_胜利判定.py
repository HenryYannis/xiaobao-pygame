import pygame, random

pygame.init()
窗口 = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Number Puzzle - Lesson 3")
时钟 = pygame.time.Clock()
大字体 = pygame.font.Font(None, 50)                   # 创建绘制数字的纯内置默认字体
提示字体 = pygame.font.Font(None, 36)                 # 新增变量：创建绘制胜利提示的默认字体

目标列表 = [1, 2, 3, 4, 5, 6, 7, 8, 0]                 # 新增变量：拼图正确还原的目标序列(0代表空格)
数字列表 = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def 随机打乱(列表):                                   # 新增函数：通过有效相邻滑块交换打乱，保证100%可解性
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

随机打乱(数字列表)
已获胜 = False                                         # 新增变量：标记当前是否已完全还原拼图
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 新增代码：按空格键重新打乱重开
            随机打乱(数字列表)
            已获胜 = False

        if not 已获胜 and 事件.type == pygame.MOUSEBUTTONDOWN:
            鼠标x, 鼠标y = pygame.mouse.get_pos()
            点击索引 = (鼠标y // 100) * 3 + (鼠标x // 100)
            空位索引 = 数字列表.index(0)

            # 曼哈顿距离精确判定：仅当点击方块与空位在上下左右严格相邻时允许滑动
            点击行, 点击列 = 点击索引 // 3, 点击索引 % 3
            空位行, 空位列 = 空位索引 // 3, 空位索引 % 3
            if abs(点击行 - 空位行) + abs(点击列 - 空位列) == 1:
                数字列表[点击索引], 数字列表[空位索引] = 数字列表[空位索引], 数字列表[点击索引]

                if 数字列表 == 目标列表:              # 新增代码：还原比对，核对当前序列是否完全符合目标
                    已获胜 = True                     # 新增代码：触发获胜状态

    窗口.fill((240, 240, 240))                         # 浅灰色背景全屏填充

    for 索引 in range(9):                              # 遍历绘制9个网格方块
        行 = 索引 // 3
        列 = 索引 % 3
        数字 = 数字列表[索引]
        if 数字 != 0:
            底色 = (100, 220, 100) if 已获胜 else (200, 200, 200)  # 新增代码：获胜时变绿高亮反馈
            pygame.draw.rect(窗口, 底色, (列 * 100 + 5, 行 * 100 + 5, 90, 90))
            数字画面 = 大字体.render(str(数字), True, (0, 0, 0))  # 默认字体渲染数字图像
            文字位置 = (列 * 100 + 36, 行 * 100 + 28)
            窗口.blit(数字画面, 文字位置)

    if 已获胜:                                         # 新增代码：获胜居中提示纯英文文本
        提示画面 = 提示字体.render("YOU WIN! - Press SPACE", True, (220, 40, 40))
        窗口.blit(提示画面, (15, 135))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
