# 井字棋对战_第2节课_落子逻辑.py
# 学习目标：在第1节课基础上，学习捕捉鼠标点击位置，并实现 X 和 O 玩家的轮流落子逻辑

import pygame  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((300, 300))
shizhong = pygame.time.Clock()

qipan_shuju = [0] * 9
# 新增变量：记录当前轮到哪个玩家（1代表X，2代表O）
dangqian_wanjia = 1 # 轮次标志（是什么），控制谁落子（为什么），1和2交替（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        
        # 新增代码：监听鼠标点击落子
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            idx = (my // 100) * 3 + (mx // 100)  # 换算索引（是什么），根据坐标找格子（为什么），行列公式计算（怎么用）
            
            # 只有在空格子才能落子
            if qipan_shuju[idx] == 0:  # 空位判定（是什么），防止重复落子（为什么），判断数组值为0（怎么用）
                qipan_shuju[idx] = dangqian_wanjia  # 占领格子（是什么），修改数据模型（为什么），赋值当前色号（怎么用）
                # 切换玩家：1变2，2变1
                dangqian_wanjia = 2 if dangqian_wanjia == 1 else 1  # 切换角色（是什么），实现对战（为什么），三元运算切换（怎么用）

    chuangkou.fill((255, 255, 255))
    for i in range(1, 3):
        pygame.draw.line(chuangkou, (0, 0, 0), (i*100, 0), (i*100, 300), 2)
        pygame.draw.line(chuangkou, (0, 0, 0), (0, i*100), (300, i*100), 2)
    
    # 新增代码：根据数据绘制棋子
    for i, zhi in enumerate(qipan_shuju):
        x, y = (i % 3) * 100 + 50, (i // 3) * 100 + 50 # 找到中心点
        if zhi == 1: pygame.draw.circle(chuangkou, (255, 0, 0), (x, y), 30, 3) # 画红色圆圈代表X
        if zhi == 2: pygame.draw.rect(chuangkou, (0, 0, 255), (x-25, y-25, 50, 50), 3) # 画蓝色方块代表O

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
