# 像素画家_第1节课_空白画布.py
# 学习目标：掌握使用二维列表表达“画布数据”，并学习如何遍历列表绘制方格阵列

import pygame  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))  # 创建400x400窗口
pygame.display.set_caption("Pixel Painter - Lesson 1")
shizhong = pygame.time.Clock()

# 变量定义：画布数据，10x10 阵列。0表示白色背景
# 这是一个列表推导式嵌套，生成 10x10 的全0列表
huabu = [[0 for _ in range(10)] for _ in range(10)]  # 画布数据（是什么），记录每个格子的颜色索引（为什么），初始化为全0（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False

    chuangkou.fill((200, 200, 200))  # 刷灰色背景（是什么），作为外框颜色（为什么），填充RGB（怎么用）
    
    # 绘制 10x10 画布格点
    for r_idx, hang in enumerate(huabu):  # 遍历行（是什么），获取行索引（为什么），enumerate获取(idx, val)（怎么用）
        for l_idx, gezi in enumerate(hang):  # 遍历列（是什么），获取列索引（为什么），嵌套遍历（怎么用）
            # 每个格子大小为 38 像素，留出 2 像素间隙
            x, y = l_idx * 40, r_idx * 40  # 坐标换算（是什么），根据索引确定位置（为什么），乘以步长40（怎么用）
            # 根据格子数值绘制颜色（本课先画白色）
            pygame.draw.rect(chuangkou, (255, 255, 255), (x+2, y+2, 36, 36))  # 画画布（是什么），视觉显示（为什么），参数含间距（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
