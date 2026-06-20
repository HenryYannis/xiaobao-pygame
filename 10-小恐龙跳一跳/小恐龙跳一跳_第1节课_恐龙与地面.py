# 小恐龙跳一跳_第1节课_恐龙与地面.py
# 学习目标：掌握如何划分游戏图层（背景、地面、角色），并绘制静态的游戏世界

import pygame  # 导入库

pygame.init()  # 初始化
chuangkou = pygame.display.set_mode((600, 300))  # 窗口（是什么），横版长条显示（为什么），元组坐标（怎么用）
pygame.display.set_caption("Dino Run - Lesson 1")
shizhong = pygame.time.Clock()

# 基础参数：地面高度、恐龙坐标
dimian_y = 250  # 地面位置（是什么），决定角色站立高度（为什么），固定数值（怎么用）
konglong_x, konglong_y = 100, 200 # 恐龙位置（是什么），起始点（为什么），变量初始化（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False

    chuangkou.fill((255, 255, 255)) # 刷白色背景
    
    # 绘制地面：灰色长方形
    pygame.draw.rect(chuangkou, (200, 200, 200), (0, dimian_y, 600, 50)) # 地面（是什么），视觉基准（为什么），draw.rect绘图（怎么用）
    
    # 绘制静态恐龙：绿色方块
    pygame.draw.rect(chuangkou, (67, 160, 72), (konglong_x, konglong_y, 40, 50)) # 恐龙（是什么），游戏主角（为什么），draw.rect绘图（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
