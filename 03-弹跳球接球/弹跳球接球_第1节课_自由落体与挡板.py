# 弹跳球接球_第1节课_自由落体与挡板.py
# 学习目标：掌握如何模拟简单的物理下落运动，并实现挡板的水平控制逻辑

import pygame  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))  # 窗口
pygame.display.set_caption("Ball Catch - Lesson 1")
shizhong = pygame.time.Clock()

# 变量定义：球的位置/速度，挡板的位置
qiu_pos, qiu_sudu = [200, 50], [0, 3]  # 球状态（是什么），初始中上方且匀速下落（为什么），列表存储[x,y]（怎么用）
ban_x = 160  # 挡板x（是什么），水平控制核心（为什么），变量初始化（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False

    # 逻辑更新：球的下落与挡板移动
    qiu_pos[1] += qiu_sudu[1]  # 下落（是什么），垂直位移（为什么），y轴坐标累加（怎么用）
    if qiu_pos[1] > 400: qiu_pos[1] = 0  # 循环（是什么），保持练习（为什么），出界重置（怎么用）
    
    jp = pygame.key.get_pressed()
    if jp[pygame.K_LEFT] and ban_x > 0: ban_x -= 5  # 左移（是什么），限位锁定（为什么），判断Left键（怎么用）
    if jp[pygame.K_RIGHT] and ban_x < 320: ban_x += 5  # 右移（是什么），限位锁定（为什么），判断Right键（怎么用）

    chuangkou.fill((30, 30, 30))  # 刷背景
    
    # 绘制：球与挡板
    pygame.draw.circle(chuangkou, (255, 255, 255), qiu_pos, 10)  # 画球（是什么），白色小圆（为什么），draw.circle（怎么用）
    pygame.draw.rect(chuangkou, (0, 255, 100), (ban_x, 370, 80, 10))  # 画板（是什么），绿色横条（为什么），draw.rect（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
