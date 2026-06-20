# 迷宫逃脱_第5节课_完整游戏与重置.py
# 学习目标：掌握通过封装重置函数实现游戏循环玩耍，以及计算最终成绩并展示在结算画面的逻辑

import pygame  # 导入库（是什么），驱动核心（为什么），必备（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），400x400（为什么），元组坐标（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 30)  # 组件初始化（是什么），时钟与字体（为什么），一次性定义（怎么用）

# 新增代码：重置函数，用于快速初始化变量
def chongzhi(): return 40, 40, False, pygame.time.get_ticks() # 封装初态（是什么），支持一键重玩（为什么），返回元组（怎么用）

wx, wy, js, st = chongzhi() # 初始化变量（是什么），调用函数赋值（为什么），解包赋值（怎么用）
dt = [[1,1,1,1,1,1,1,1,1,1],[1,0,0,0,1,0,0,0,0,1],[1,0,1,0,1,0,1,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,0,1,0,1],[1,0,0,0,0,1,0,0,0,1],[1,1,1,1,0,1,1,1,0,1],[1,0,0,1,0,0,0,1,0,1],[1,0,0,0,0,1,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]] # 地图数据

while True:  # 开启死循环
    for ev in pygame.event.get():  # 监听事件
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        # 新增代码：按空格键重置游戏
        if js and ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE: wx, wy, js, st = chongzhi() # 重玩判定（是什么），触发重置（为什么），判断按键状态（怎么用）

    if not js:  # 运行中逻辑
        jp, nx, ny = pygame.key.get_pressed(), wx, wy
        if jp[pygame.K_LEFT]: nx -= 2; 
        if jp[pygame.K_RIGHT]: nx += 2; 
        if jp[pygame.K_UP]: ny -= 2; 
        if jp[pygame.K_DOWN]: ny += 2; 
        if dt[ny//40][nx//40] == 0 and dt[(ny+39)//40][(nx+39)//40] == 0: wx, wy = nx, ny
        if wx >= 320 and wy >= 320: js = True; et = (pygame.time.get_ticks() - st) // 1000 # 胜利判定并计分

    chuangkou.fill((20, 20, 20))  # 刷背景
    for r, h in enumerate(dt):
        for c, g in enumerate(h):
            if g == 1: pygame.draw.rect(chuangkou, (100, 100, 100), (c*40, r*40, 40, 40))
    pygame.draw.rect(chuangkou, (0, 255, 0), (320, 320, 40, 40)) # 终点
    pygame.draw.rect(chuangkou, (255, 50, 50), (wx+5, wy+5, 30, 30)) # 玩家
    
    # 新增代码：动态文字展示
    msg = f"Time: {(pygame.time.get_ticks()-st)//1000}s" if not js else f"ESCAPED in {et}s! SPACE to Restart" # 结算文案（是什么），展示结果（为什么），三元运算（怎么用）
    chuangkou.blit(ziti.render(msg, True, (255,255,0) if js else (255,255,255)), (10, 10)) # 显示文字

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成这一帧（为什么），同步频率（怎么用）
