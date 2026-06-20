# 颜色记忆大师_第5节课_完整游戏与结局.py
# 学习目标：掌握游戏失败结局的判定与展示，学习如何利用“休眠延时”设计结算画面

import pygame, random, time  # 导入库（是什么），核心支持（为什么），必备环境（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 300))  # 窗口（是什么），舞台（为什么），元组参数（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 30)  # 组件初始化（是什么），时钟与字体（为什么），一次性定义（怎么用）

yanses, zt, xl, wj, defen, idx, nt = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)], "ready", [], [], 0, 0, 0

while True:  # 主循环
    now = time.time()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        if ev.type == pygame.MOUSEBUTTONDOWN and zt == "playing":
            mx, my = pygame.mouse.get_pos(); wj.append((0 if mx<175 else 1) if my<150 else (2 if mx<175 else 3))

    chuangkou.fill((50, 50, 80))
    if zt == "ready":
        chuangkou.blit(ziti.render("Memory Master - Click to Start", True, (255, 255, 255)), (40, 130))
        if pygame.mouse.get_pressed()[0]: zt, xl, wj, idx, nt = "showing", [random.randint(0,3)], [], 0, now + 1
    elif zt == "showing":
        if now >= nt: idx += 1; nt = now + 0.8
        (idx < len(xl)) and pygame.draw.rect(chuangkou, yanses[xl[idx]], (100, 100, 200, 100))
        (idx >= len(xl)) and (zt := "playing")
    elif zt == "playing":
        for i in range(4): pygame.draw.rect(chuangkou, yanses[i], (50+(i%2)*175, 50+(i//2)*125, 125, 100))
        if len(wj) == len(xl):
            if wj == xl: zt, xl, wj, idx, nt, defen = "showing", xl+[random.randint(0,3)], [], 0, now+1, defen+10
            else: zt = "over" # 新增代码：错误则跳转到结算态
    
    # 新增代码：结局画面渲染
    elif zt == "over": # 结算态（是什么），展示成绩（为什么），独立分支处理（怎么用）
        chuangkou.fill((0, 0, 0)) # 黑屏（是什么），肃穆感（为什么），颜色填充（怎么用）
        chuangkou.blit(ziti.render("GAME OVER", True, (255, 0, 0)), (135, 100)) # 写大字（是什么），红色警告（为什么），blit贴图（怎么用）
        chuangkou.blit(ziti.render(f"Final Score: {defen}", True, (255, 255, 255)), (120, 150)) # 显成绩
        pygame.display.flip(); pygame.time.wait(2000); zt, defen = "ready", 0 # 停顿重置（是什么），留白观看（为什么），组合调用（怎么用）

    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10))
    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成这一帧（为什么），同步频率（怎么用）
