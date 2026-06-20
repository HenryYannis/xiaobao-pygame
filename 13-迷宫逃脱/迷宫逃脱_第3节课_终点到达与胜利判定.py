# 迷宫逃脱_第3节课_终点到达与胜利判定.py
# 学习目标：掌握区域碰撞判定逻辑，并学习如何根据游戏状态位切换逻辑分支

import pygame  # 导入库（是什么），驱动核心（为什么），必备（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），定义舞台（为什么），元组坐标（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 40)  # 初始化组件（是什么），时钟与字体（为什么），一次性定义（怎么用）

wx, wy, js = 40, 40, False  # 状态量（是什么），玩家坐标与结束标志（为什么），多重初始化（怎么用）
# 新增变量：终点区域
zx, zy = 320, 320  # 终点坐标（是什么），逃离目标（为什么），初始坐标赋值（怎么用）

dt = [[1,1,1,1,1,1,1,1,1,1],[1,0,0,0,1,0,0,0,0,1],[1,0,1,0,1,0,1,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,0,1,0,1],[1,0,0,0,0,1,0,0,0,1],[1,1,1,1,0,1,1,1,0,1],[1,0,0,1,0,0,0,1,0,1],[1,0,0,0,0,1,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]] # 地图

while True:  # 主循环
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()

    if not js:  # 未结束时允许逻辑运行
        jp, nx, ny = pygame.key.get_pressed(), wx, wy
        if jp[pygame.K_LEFT]: nx -= 2; 
        if jp[pygame.K_RIGHT]: nx += 2; 
        if jp[pygame.K_UP]: ny -= 2; 
        if jp[pygame.K_DOWN]: ny += 2; 
        if dt[ny//40][nx//40] == 0 and dt[(ny+39)//40][(nx+39)//40] == 0: wx, wy = nx, ny
        # 新增代码：终点判定
        if wx >= zx - 10 and wy >= zy - 10: js = True  # 判定胜利（是什么），检测到达（为什么），状态位改True（怎么用）

    chuangkou.fill((20, 20, 20))  # 刷背景
    for r, h in enumerate(dt):
        for c, g in enumerate(h):
            if g == 1: pygame.draw.rect(chuangkou, (100, 100, 100), (c*40, r*40, 40, 40))

    # 新增代码：绘制终点
    pygame.draw.rect(chuangkou, (0, 255, 0), (zx, zy, 40, 40))  # 画终点（是什么），绿色格子（为什么），指定位置（怎么用）
    pygame.draw.rect(chuangkou, (255, 50, 50), (wx + 5, wy + 5, 30, 30))  # 画玩家
    if js: chuangkou.blit(ziti.render("YOU ESCAPED!", True, (255, 255, 0)), (100, 180)) # 显文字（是什么），反馈成果（为什么），渲染贴图（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成一帧（为什么），同步频率（怎么用）
