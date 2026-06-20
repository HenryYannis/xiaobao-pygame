# 打地鼠_第3节课_完整地鼠挑战.py
# 学习目标：在第2节课基础上，加入分数系统与限时挑战，完成一个完整的动作小游戏

import pygame, random, math  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)

# 新增变量：得分与倒计时
defen, sheng_t = 0, 15  # 状态量（是什么），记录成绩与剩余时间（为什么），初始化变量（怎么用）
didong_list = [[l*120+80, h*120+80] for h in range(3) for l in range(3)]
dishu_idx, next_t = -1, 0

yunxing = True
while yunxing:
    now = pygame.time.get_ticks()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        # 新增代码：只有在倒计时大于0时才允许击打
        if sheng_t > 0 and ev.type == pygame.MOUSEBUTTONDOWN and dishu_idx != -1:
            mx, my = pygame.mouse.get_pos()
            if math.hypot(mx - didong_list[dishu_idx][0], my - didong_list[dishu_idx][1]) < 30:
                dishu_idx, defen, next_t = -1, defen + 10, now + 300  # 击中反馈（是什么），加分并加速冒头（为什么），同步重置变量（怎么用）

    # 新增代码：倒计时逻辑
    sheng_t = max(0, 15 - now // 1000)  # 计算时间（是什么），控制游戏终点（为什么），上限减去运行秒数（怎么用）

    if sheng_t > 0 and now > next_t: dishu_idx, next_t = random.randint(0, 8), now + 800  # 冒头更新
    elif sheng_t <= 0: dishu_idx = -1  # 时间到后地鼠隐藏

    chuangkou.fill((34, 139, 34))
    for idx, pos in enumerate(didong_list):
        pygame.draw.circle(chuangkou, (50, 25, 0), pos, 40)
        if idx == dishu_idx: pygame.draw.circle(chuangkou, (200, 150, 100), pos, 30)

    # 新增代码：绘制分数与计时界面
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10))  # 显分（是什么），成果反馈（为什么），贴图显示（怎么用）
    chuangkou.blit(ziti.render(f"Time: {sheng_t}s", True, (255, 0, 0)), (280, 10))  # 显时（是什么），提示剩余（为什么），贴图显示（怎么用）
    if sheng_t <= 0: chuangkou.blit(ziti.render("TIME UP!", True, (255, 255, 0)), (140, 180)) # 结局提示

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
