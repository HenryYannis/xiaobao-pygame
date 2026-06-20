# 颜色记忆大师_第4节课_分数与难度提升.py
# 学习目标：掌握通过列表追加(append)实现动态难度进阶，并掌握实时分数的反馈显示

import pygame, random, time  # 导入库（是什么），核心支持（为什么），必备环境（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 300))  # 窗口（是什么），舞台（为什么），元组参数（怎么用）
shizhong, ziti, defen = pygame.time.Clock(), pygame.font.SysFont(None, 30), 0 # 组件与分数

yanses, zt, xl, wj, idx, nt = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)], "ready", [], [], 0, 0

while True:  # 主循环
    now = time.time()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        if ev.type == pygame.MOUSEBUTTONDOWN and zt == "playing":
            mx, my = pygame.mouse.get_pos(); wj.append((0 if mx<175 else 1) if my<150 else (2 if mx<175 else 3))

    chuangkou.fill((50, 50, 80))
    if zt == "ready":
        if pygame.mouse.get_pressed()[0]: zt, xl, wj, idx, nt = "showing", [random.randint(0,3)], [], 0, now + 1
    elif zt == "showing":
        if now >= nt: idx += 1; nt = now + 0.8
        (idx < len(xl)) and pygame.draw.rect(chuangkou, yanses[xl[idx]], (100, 100, 200, 100))
        (idx >= len(xl)) and (zt := "playing")
    elif zt == "playing":
        for i in range(4): pygame.draw.rect(chuangkou, yanses[i], (50+(i%2)*175, 50+(i//2)*125, 125, 100))
        # 新增代码：对错判定与进度逻辑
        if len(wj) == len(xl):
            if wj == xl: zt, xl, wj, idx, nt, defen = "showing", xl+[random.randint(0,3)], [], 0, now+1, defen+10 # 答对（是什么），难度升级并加分（为什么），列表追加（怎么用）
            else: zt, defen = "ready", 0 # 答错重置分数

    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10)) # 显示分数
    pygame.display.flip(); shizhong.tick(60)  # 刷新并定帧（是什么），同步频率（为什么），锁定60FPS（怎么用）
