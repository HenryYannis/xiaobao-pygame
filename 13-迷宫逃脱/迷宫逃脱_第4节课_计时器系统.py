# 迷宫逃脱_第4节课_计时器系统.py
# 学习目标：掌握Pygame内置时钟获取毫秒数并换算为秒，学习在屏幕实时渲染计时器UI

import pygame  # 导入库（是什么），核心驱动（为什么），必备（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），定义舞台（为什么），元组坐标（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 30)  # 组件初始化（是什么），时钟与字体（为什么），一次性定义（怎么用）

wx, wy, js, zx, zy = 40, 40, False, 320, 320  # 状态变量组（是什么），位置与终点坐标（为什么），变量初始化（怎么用）
# 新增变量：计时器
ys = 0  # 用时（是什么），记录逃脱秒数（为什么），初始设为0（怎么用）

dt = [[1,1,1,1,1,1,1,1,1,1],[1,0,0,0,1,0,0,0,0,1],[1,0,1,0,1,0,1,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,0,1,0,1],[1,0,0,0,0,1,0,0,0,1],[1,1,1,1,0,1,1,1,0,1],[1,0,0,1,0,0,0,1,0,1],[1,0,0,0,0,1,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]] # 地图

while True:  # 主循环
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: pygame.quit(); exit()

    if not js:  # 未结束时运行逻辑
        # 新增代码：更新用时
        ys = pygame.time.get_ticks() // 1000  # 获取秒数（是什么），记录进度（为什么），毫秒除以1000（怎么用）
        jp, nx, ny = pygame.key.get_pressed(), wx, wy
        if jp[pygame.K_LEFT]: nx -= 2; 
        if jp[pygame.K_RIGHT]: nx += 2; 
        if jp[pygame.K_UP]: ny -= 2; 
        if jp[pygame.K_DOWN]: ny += 2; 
        if dt[ny//40][nx//40] == 0 and dt[(ny+39)//40][(nx+39)//40] == 0: wx, wy = nx, ny
        if wx >= zx - 10 and wy >= zy - 10: js = True

    chuangkou.fill((20, 20, 20))  # 刷背景
    for r, h in enumerate(dt):
        for c, g in enumerate(h):
            if g == 1: pygame.draw.rect(chuangkou, (100, 100, 100), (c*40, r*40, 40, 40))
    pygame.draw.rect(chuangkou, (0, 255, 0), (zx, zy, 40, 40))  # 画终点
    pygame.draw.rect(chuangkou, (255, 50, 50), (wx + 5, wy + 5, 30, 30))  # 画玩家
    # 新增代码：绘制计时器UI
    chuangkou.blit(ziti.render(f"Time: {ys}s", True, (255, 255, 255)), (10, 10))  # 显用时（是什么），UI反馈（为什么），文字贴图（怎么用）
    if js: chuangkou.blit(ziti.render("YOU ESCAPED!", True, (255, 255, 0)), (100, 180)) # 显示胜利文字

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成一帧（为什么），同步频率（怎么用）
