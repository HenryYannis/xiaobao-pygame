# 节奏方块_第2节课_精准节奏判定.py
# 学习目标：在第1节课基础上，学习如何捕捉空格键点击，并根据方块与判定线的重合度进行判定

import pygame  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 600))
shizhong = pygame.time.Clock()

xian_y = 500  # 判定线
fang_x, fang_y = 175, -50  # 方块位置

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        
        # 新增代码：按下空格键进行节奏判定
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:  # 空格按下（是什么），捕捉瞬间时机（为什么），判断KEYDOWN事件（怎么用）
            # 新增逻辑：计算方块中心与判定线的垂直距离
            # 如果距离小于 30 像素，则视为“击中”，方块重置
            if abs(fang_y + 25 - xian_y) < 30:  # 距离判定（是什么），核对点击准确度（为什么），使用abs取绝对值（怎么用）
                fang_y = -100  # 击中消失（是什么），给玩家成功反馈（为什么），重置y坐标回到顶部（怎么用）

    fang_y += 5
    if fang_y > 600: fang_y = -50

    chuangkou.fill((30, 30, 30))
    pygame.draw.line(chuangkou, (100, 100, 100), (0, xian_y), (400, xian_y), 5)
    
    # 绘制下落方块
    pygame.draw.rect(chuangkou, (0, 255, 255), (fang_x, fang_y, 50, 50))

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
