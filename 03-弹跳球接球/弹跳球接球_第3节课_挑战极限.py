# 弹跳球接球_第3节课_挑战极限.py
# 学习目标：在第2节课基础上，引入重力加速度模拟真实手感，并加入分数与死亡判定

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)

# 变量：位置、速度、分数、是否结束
qp, qs, defen, js = [200, 50], [0, 2], 0, False # 状态打包（是什么），初始数据（为什么），变量初始化（怎么用）
bx = 160

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        # 新增逻辑：结束后按空格重启
        if js and ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            qp, qs, defen, js = [200, 50], [0, 2], 0, False # 重置状态（是什么），开始新一局（为什么），变量覆盖（怎么用）

    if not js:
        # 新增代码：模拟重力加速度。y轴速度每帧微增
        qs[1] += 0.15 # 重力效果（是什么），模拟自然下坠（为什么），速度累加（怎么用）
        qp[0] += qs[0]; qp[1] += qs[1]
        
        if qp[0] <= 10 or qp[0] >= 390: qs[0] *= -1
        if qp[1] <= 10: qs[1] = abs(qs[1])
        if qp[1] >= 360 and bx <= qp[0] <= bx + 80:
            qs[1], qs[0], defen = -6, random.randint(-4, 4), defen + 10 # 接球加分（是什么），成果奖励（为什么），多变量更新（怎么用）
        
        # 新增逻辑：掉落判定
        if qp[1] > 400: js = True # 失败判定（是什么），触发结束态（为什么），修改标志位（怎么用）

        jp = pygame.key.get_pressed()
        if jp[pygame.K_LEFT] and bx > 0: bx -= 7
        if jp[pygame.K_RIGHT] and bx < 320: bx += 7

    chuangkou.fill((30, 30, 30))
    pygame.draw.circle(chuangkou, (255, 255, 255), (int(qp[0]), int(qp[1])), 10)
    pygame.draw.rect(chuangkou, (0, 255, 100), (bx, 370, 80, 10))
    
    # 绘制分数
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255,255,255)), (10, 10))
    if js: chuangkou.blit(ziti.render("GAME OVER - Press SPACE", True, (255, 0, 0)), (40, 180))

    pygame.display.flip(); shizhong.tick(60)
