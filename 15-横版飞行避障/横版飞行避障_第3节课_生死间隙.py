# 横版飞行避障_第3节课_生死间隙.py
# 学习目标：掌握矩形碰撞判定(colliderect)的应用，并完成具有分数结算的完整横版生存游戏

import pygame, random  # 导入库
pygame.init()
chuangkou = pygame.display.set_mode((400, 500))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)

# 变量初始化
bird, za_list, defen, js = [50, 250, 0], [], 0, False # 状态量汇总（是什么），包含分数与结束位（为什么），多重赋值（怎么用）

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        if not js and ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE: bird[2] = -7
        if js and ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE: bird, za_list, defen, js = [50, 250, 0], [], 0, False # 重置

    if not js: # 运行逻辑
        bird[2] += 0.4; bird[1] += bird[2]
        if bird[1] < 0 or bird[1] > 480: js = True # 触界失败
        
        if len(za_list) == 0 or za_list[-1][0] < 200: za_list.append([400, random.randint(100, 300)])
        for i in range(len(za_list)-1, -1, -1):
            za_list[i][0] -= 4; 
            # 新增代码：碰撞检测。将圆形玩家简化为矩形判定
            b_rect = pygame.Rect(bird[0]-15, bird[1]-15, 30, 30) # 玩家矩形
            s_rect = pygame.Rect(za_list[i][0], 0, 50, za_list[i][1]) # 上矩形
            x_rect = pygame.Rect(za_list[i][0], za_list[i][1]+120, 50, 500) # 下矩形
            if b_rect.colliderect(s_rect) or b_rect.colliderect(x_rect): js = True # 撞管判定（是什么），判定失败（为什么），调用colliderect（怎么用）
            
            # 新增代码：计分逻辑
            if za_list[i][0] == 52: defen += 1 # 通过加分（是什么），越过障碍奖励（为什么），坐标判断累加（怎么用）
            if za_list[i][0] < -50: za_list.pop(i)

    chuangkou.fill((100, 200, 255))
    pygame.draw.circle(chuangkou, (255, 255, 0), (int(bird[0]), int(bird[1])), 15)
    for za in za_list:
        pygame.draw.rect(chuangkou, (0, 150, 0), (za[0], 0, 50, za[1]))
        pygame.draw.rect(chuangkou, (0, 150, 0), (za[0], za[1]+120, 50, 500))
    # 显示分值
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10))
    if js: chuangkou.blit(ziti.render("GAME OVER", True, (255, 0, 0)), (130, 230))

    pygame.display.flip(); shizhong.tick(60)
