# 迷宫逃脱_第2节课_墙壁阻挡逻辑.py
# 学习目标：掌握“碰撞预判”算法，通过地图列表索引换算实现物理墙壁的阻挡效果

import pygame  # 导入库（是什么），核心驱动（为什么），必备（怎么用）

pygame.init()  # 初始化（是什么），准备引擎（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），定义舞台（为什么），元组坐标（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），定帧器（为什么），锁定60FPS（怎么用）

wx, wy = 40, 40  # 玩家位置
dt = [[1,1,1,1,1,1,1,1,1,1],[1,0,0,0,1,0,0,0,0,1],[1,0,1,0,1,0,1,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,0,1,0,1],[1,0,0,0,0,1,0,0,0,1],[1,1,1,1,0,1,1,1,0,1],[1,0,0,1,0,0,0,1,0,1],[1,0,0,0,0,1,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]] # 地图数据

while True:  # 主循环
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: pygame.quit(); exit()

    # 新增代码：碰撞预判移动
    jp, nx, ny = pygame.key.get_pressed(), wx, wy  # 读键与暂存（是什么），准备预测（为什么），同步赋值（怎么用）
    if jp[pygame.K_LEFT]: nx -= 2
    if jp[pygame.K_RIGHT]: nx += 2
    if jp[pygame.K_UP]: ny -= 2
    if jp[pygame.K_DOWN]: ny += 2

    # 新增代码：墙壁索引检测
    # 判断玩家尝试到达的格子是否为通道(0)
    if dt[ny//40][nx//40] == 0 and dt[(ny+39)//40][(nx+39)//40] == 0:  # 阻挡判定（是什么），核对新坐标（为什么），索引换算（怎么用）
        wx, wy = nx, ny  # 批准位移（是什么），确认安全后更新（为什么），变量赋值（怎么用）

    chuangkou.fill((20, 20, 20))  # 刷背景
    for r, h in enumerate(dt):
        for c, g in enumerate(h):
            if g == 1: pygame.draw.rect(chuangkou, (100, 100, 100), (c*40, r*40, 40, 40))

    pygame.draw.rect(chuangkou, (255, 50, 50), (wx + 5, wy + 5, 30, 30))  # 画玩家
    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），同步频率（为什么），锁定60FPS（怎么用）
