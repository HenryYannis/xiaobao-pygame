# 数字拼图_第1节课_棋盘生成与洗牌.py
# 学习目标：掌握列表数据结构，利用随机打乱(random.shuffle)生成一个可玩的 3x3 拼图阵列

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((300, 300))  # 窗口设为300x300（是什么），每格100像素（为什么），宽高元组（怎么用）
pygame.display.set_caption("Puzzle - Lesson 1")
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 60)

# 变量定义：数字列表 1-8，再加上 0 代表空位
shuzi_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # 数字池（是什么），拼图的所有元素（为什么），0表示可以移动的空位（怎么用）
random.shuffle(shuzi_list)  # 洗牌（是什么），打乱顺序（为什么），直接修改列表（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False

    chuangkou.fill((255, 255, 255))
    
    # 绘制 3x3 拼图网格
    for i in range(9):
        num = shuzi_list[i]
        # 根据索引 i 计算格子的行列坐标
        x, y = (i % 3) * 100, (i // 3) * 100  # 位置换算（是什么），将1维转为2维坐标（为什么），格长100（怎么用）
        
        if num != 0:  # 只有非零数字才绘制方块
            pygame.draw.rect(chuangkou, (200, 200, 200), (x+5, y+5, 90, 90))  # 画格（是什么），背景方块（为什么），参数含间距（怎么用）
            wenzi = ziti.render(str(num), True, (0, 0, 0))  # 画字（是什么），显示数字（为什么），render渲染（怎么用）
            chuangkou.blit(wenzi, (x+35, y+25))  # 贴图（是什么），文字居中（为什么），blit贴到指定位（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
