# 像素画家_第2节课_画笔涂鸦.py
# 学习目标：在第1节课基础上，学习捕捉鼠标点击位置，并反向计算二维数组索引以实现“填色”效果

import pygame  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong = pygame.time.Clock()

huabu = [[0 for _ in range(10)] for _ in range(10)]

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        
        # 新增代码：监听鼠标点击（左键按下）
        if pygame.mouse.get_pressed()[0]:  # 鼠标左键状态（是什么），实现持续涂鸦（为什么），get_pressed获取实时状态（怎么用）
            mx, my = pygame.mouse.get_pos()  # 读位置（是什么），获取落笔点（为什么），返回坐标元组（怎么用）
            # 新增逻辑：坐标反向换算为列表索引
            col, row = mx // 40, my // 40  # 索引换算（是什么），找到对应的格子（为什么），整除步长40（怎么用）
            # 新增逻辑：修改对应格子的数值（1代表被涂色）
            if 0 <= col < 10 and 0 <= row < 10:  # 边界保护（是什么），防止索引溢出（为什么），判断范围（怎么用）
                huabu[row][col] = 1  # 填色（是什么），修改数据模型（为什么），赋值为1（怎么用）

    chuangkou.fill((200, 200, 200))
    for r, hang in enumerate(huabu):
        for l, ge in enumerate(hang):
            # 新增逻辑：根据数值决定绘制颜色
            # 如果是1画黑色，否则画白色
            yanse = (0, 0, 0) if ge == 1 else (255, 255, 255)  # 颜色选择（是什么），视觉反馈（为什么），三元运算（怎么用）
            pygame.draw.rect(chuangkou, yanse, (l*40+2, r*40+2, 36, 36))

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
