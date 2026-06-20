# 节奏方块_第4节课_完整挑战与分数.py
# 学习目标：在第3节课基础上，加入分数系统与连击(Combo)机制，完成一款完整的节奏游戏

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 600))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)

# 新增变量：分数与连击数
defen, lianji = 0, 0  # 状态变量（是什么），记录成绩与连击（为什么），初始化为0（怎么用）
fang_list, guidao = [], [75, 175, 275]

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            hit = False  # 命中标志位
            for i in range(len(fang_list)-1, -1, -1):
                if abs(fang_list[i][1] + 25 - 500) < 30:
                    # 新增代码：击中后处理连击与加分
                    fang_list.pop(i); hit = True; lianji += 1; defen += 10 * lianji  # 奖励机制（是什么），连击越多分越高（为什么），变量累加（怎么用）
                    break
            if not hit: lianji = 0  # 新增逻辑：落空则连击中断（是什么），惩罚机制（为什么），重置变量（怎么用）

    if random.random() < 0.02: fang_list.append([random.choice(guidao), -50])
    for f in fang_list: f[1] += 5
    
    # 新增代码：检查是否有方块落地，落地也中断连击
    if any(f[1] > 600 for f in fang_list): lianji = 0  # 落地检测（是什么），保持挑战度（为什么），any函数判断列表（怎么用）
    fang_list = [f for f in fang_list if f[1] < 600]

    chuangkou.fill((30, 30, 30))
    pygame.draw.line(chuangkou, (100, 100, 100), (0, 500), (400, 500), 5)
    for f in fang_list: pygame.draw.rect(chuangkou, (0, 255, 255 if lianji < 5 else 255), (f[0], f[1], 50, 50))  # 变色反馈（是什么），增强视觉（为什么），三元运算选色（怎么用）

    # 新增代码：实时显示分数和连击数
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10))  # 显分（是什么），成果反馈（为什么），贴图（怎么用）
    if lianji > 1: chuangkou.blit(ziti.render(f"{lianji} Combo!", True, (255, 255, 0)), (150, 100)) # 显连击（是什么），成就感增强（为什么），黄字贴图（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
