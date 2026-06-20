# 数字拼图_第2节课_移动拼图.py
# 学习目标：在第1节课基础上，学习如何捕捉鼠标点击位置，并实现相邻格子的位置交换逻辑

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((300, 300))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 60)

shuzi_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]
random.shuffle(shuzi_list)

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        
        # 新增代码：监听鼠标点击，实现数字移动
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            idx = (my // 100) * 3 + (mx // 100)  # 反向换算（是什么），根据坐标找索引（为什么），(y/100)*3 + (x/100)（怎么用）
            
            # 新增逻辑：查找空位(0)的索引
            kong_idx = shuzi_list.index(0)  # 找零（是什么），定位可交换位（为什么），调用index方法（怎么用）
            
            # 新增逻辑：判定点击位与空位是否相邻（同行相邻或同列相邻）
            # 距离计算：索引之差的绝对值为1（左右）或3（上下）
            if abs(idx - kong_idx) in [1, 3]:  # 邻近判定（是什么），判定是否合法移动（为什么），排除对角线交换（怎么用）
                shuzi_list[idx], shuzi_list[kong_idx] = shuzi_list[kong_idx], shuzi_list[idx]  # 交换值（是什么），实现移动效果（为什么），Python式变量互换（怎么用）

    chuangkou.fill((255, 255, 255))
    for i in range(9):
        num = shuzi_list[i]
        x, y = (i % 3) * 100, (i // 3) * 100
        if num != 0:
            pygame.draw.rect(chuangkou, (200, 200, 200), (x+5, y+5, 90, 90))
            chuangkou.blit(ziti.render(str(num), True, (0, 0, 0)), (x+35, y+25))

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
