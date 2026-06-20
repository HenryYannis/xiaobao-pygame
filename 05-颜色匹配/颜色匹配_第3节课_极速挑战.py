# 颜色匹配_第3节课_极速挑战.py
# 学习目标：在第2节课基础上，加入倒计时进度条与分数系统，完成一款节奏紧张的消除游戏

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 300))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)

yanses = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255)]
def xin_t(): return random.sample(range(len(yanses)), 2), 0 # 简化版

# 变量：选项、答案索引(0或1)、分数、剩余生命(时间)
opts, daan_idx = random.sample(range(5), 2), random.randint(0, 1)
defen, shengming = 0, 1.0 # 状态量（是什么），生命值/时间条（为什么），范围0.0到1.0（怎么用）

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        if ev.type == pygame.MOUSEBUTTONDOWN and shengming > 0:
            mx, my = pygame.mouse.get_pos()
            # 简化判定：左半边选0，右半边选1
            xuan = 0 if mx < 200 else 1 # 二选一（是什么），判断点击方位（为什么），简化坐标判断（怎么用）
            if xuan == daan_idx:
                defen += 10; shengming = min(1.0, shengming + 0.2) # 加分补血（是什么），鼓励正确操作（为什么），变量累加（怎么用）
                opts, daan_idx = random.sample(range(5), 2), random.randint(0, 1) # 刷新

    # 新增代码：生命值（时间）随帧数衰减
    shengming -= 0.005 # 衰减（是什么），产生时间压力（为什么），每帧递减（怎么用）
    if shengming <= 0: shengming = 0 # 结束判定（是什么），判定输掉（为什么），底限保护（怎么用）

    chuangkou.fill((255, 255, 255))
    pygame.draw.rect(chuangkou, yanses[opts[daan_idx]], (150, 50, 100, 40)) # 目标
    for i in range(2): pygame.draw.rect(chuangkou, yanses[opts[i]], (50+i*180, 180, 120, 80)) # 绘制两个选项
    
    # 新增代码：绘制顶部的红色倒计时进度条
    pygame.draw.rect(chuangkou, (255, 0, 0), (0, 0, 400 * shengming, 10)) # 进度条（是什么），视觉化剩余时间（为什么），宽=总宽*比例（怎么用）
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (0,0,0)), (10, 20)) # 显分

    if shengming <= 0: chuangkou.blit(ziti.render("OUT OF TIME!", True, (255, 0, 0)), (120, 130))
    pygame.display.flip(); shizhong.tick(60)
