# 像素画家_第3节课_彩色调色盘.py
# 学习目标：在第2节课基础上，加入多颜色选择与清屏功能，完成一个完整的交互式像素画工具

import pygame  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 450)) # 增加下方空间放调色盘
shizhong = pygame.time.Clock()

# 变量：画布、当前色号、颜色表
huabu = [[0 for _ in range(10)] for _ in range(10)]
yanses = [(255,255,255), (0,0,0), (255,0,0), (0,255,0), (0,0,255)] # 白黑红绿蓝
bi_idx = 1 # 当前笔触色号索引

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        # 新增代码：按右键清空画布
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 3: # 右键（是什么），清屏动作（为什么），重置数组（怎么用）
            huabu = [[0 for _ in range(10)] for _ in range(10)]

    # 涂鸦逻辑
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        if my < 400: # 在画布区点击
            huabu[my//40][mx//40] = bi_idx # 填入当前色（是什么），实现变色绘制（为什么），使用变量色号（怎么用）
        else: # 新增逻辑：在调色盘区点击，切换笔色
            bi_idx = mx // 80 # 选色（是什么），根据底部位置选颜色（为什么），400宽/5色=每格80（怎么用）

    chuangkou.fill((200, 200, 200))
    # 绘制画布
    for r, h in enumerate(huabu):
        for l, g in enumerate(h): pygame.draw.rect(chuangkou, yanses[g], (l*40+2, r*40+2, 36, 36))
    
    # 新增代码：绘制底部调色盘按钮
    for i, c in enumerate(yanses):
        pygame.draw.rect(chuangkou, c, (i*80+5, 405, 70, 40)) # 调色块（是什么），视觉指引（为什么），循环绘图（怎么用）
        if i == bi_idx: pygame.draw.rect(chuangkou, (255,255,0), (i*80+5, 405, 70, 40), 3) # 高亮选中（是什么），提示当前色（为什么），画金色边框（怎么用）

    pygame.display.flip(); shizhong.tick(60)
