# 颜色记忆大师_第3节课_玩家点击与比对.py
# 学习目标：掌握鼠标坐标到格点索引的映射换算，并学习列表的逻辑比对算法

import pygame, random, time  # 导入库（是什么），核心支持（为什么），必备环境（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 300))  # 窗口（是什么），舞台（为什么），元组参数（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 30)  # 组件（是什么），时钟与字体（为什么），一次性定义（怎么用）

yanses, zt, xl, wj = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)], "ready", [], [] # 基础变量
idx, nt = 0, 0

while True:  # 主循环
    now = time.time()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        # 新增代码：点击检测
        if ev.type == pygame.MOUSEBUTTONDOWN and zt == "playing":
            mx, my = pygame.mouse.get_pos() # 读鼠标（是什么），获取点击位（为什么），返回x,y（怎么用）
            # 新增逻辑：坐标映射到 0-3 索引
            h = (0 if mx<175 else 1) if my<150 else (2 if mx<175 else 3) # 索引换算（是什么），判断象限（为什么），三元运算（怎么用）
            wj.append(h) # 记点击（是什么），记录答案（为什么），追加到列表（怎么用）

    chuangkou.fill((50, 50, 80))
    if zt == "ready":
        if pygame.mouse.get_pressed()[0]: zt, xl, wj, idx, nt = "showing", [random.randint(0,3)], [], 0, now + 1
    elif zt == "showing":
        if now >= nt: idx += 1; nt = now + 0.8
        (idx < len(xl)) and pygame.draw.rect(chuangkou, yanses[xl[idx]], (100, 100, 200, 100))
        if idx >= len(xl): zt = "playing" # 演示完切换到输入
    elif zt == "playing": # 答题状态
        for i in range(4): pygame.draw.rect(chuangkou, yanses[i], (50+(i%2)*175, 50+(i//2)*125, 125, 100))
        # 新增逻辑：序列比对
        if len(wj) == len(xl): # 填满判断（是什么），触发核对（为什么），长度比对（怎么用）
            zt = "ready" # 对错先回起点

    pygame.display.flip(); shizhong.tick(60)  # 刷新并定帧（是什么），同步频率（为什么），锁定60FPS（怎么用）
