# 黄金矿工_第5节课_完整矿工挑战.py
# 学习目标：在第4节课基础上，加入分数系统与限时挑战，完成一款具备完整数值反馈的作品

import pygame, math, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 30)

zx, cd, jd, zt, fenshu = [200, 50], 50, 0, 0, 0  # 状态变量
jinks = [[random.randint(50,350), random.randint(150,350), random.randint(10,30)] for _ in range(5)]
zhua_dao = None

while True:
    now = pygame.time.get_ticks()
    sheng_t = max(0, 30 - now // 1000)  # 倒计时（是什么），设定30秒限时（为什么），计算剩余时间（怎么用）
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        if sheng_t > 0 and ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE and zt == 0: zt = 1

    if sheng_t > 0:  # 只有在时间未结束时运行逻辑
        if zt == 0: jd = math.sin(now / 500) * 80
        elif zt == 1: cd += 5
        elif zt == 2:
            cd -= max(1, 5 - (zhua_dao[2]//10 if zhua_dao else 0))
            if cd <= 50: 
                # 新增代码：回收成功后计算分数。金块半径越大，分越高
                if zhua_dao: fenshu += zhua_dao[2] * 2  # 加分（是什么），成果转化为成绩（为什么），半径乘倍数计算（怎么用）
                zt, cd, zhua_dao = 0, 50, None
        
        mx, my = zx[0] + cd * math.cos(math.radians(jd+90)), zx[1] + cd * math.sin(math.radians(jd+90))
        if zt == 1:
            for i, jk in enumerate(jinks):
                if math.hypot(mx - jk[0], my - jk[1]) < jk[2]: zhua_dao = jinks.pop(i); zt = 2; break

    chuangkou.fill((255, 255, 200))
    for jx, jy, jr in jinks: pygame.draw.circle(chuangkou, (255, 215, 0), (jx, jy), jr)
    if zhua_dao: pygame.draw.circle(chuangkou, (255, 215, 0), (mx, my), zhua_dao[2])
    pygame.draw.line(chuangkou, (0, 0, 0), zx, (mx, my), 3)
    
    # 绘制分数与时间界面
    chuangkou.blit(ziti.render(f"Score: {fenshu}", True, (0,0,0)), (10, 10))
    chuangkou.blit(ziti.render(f"Time: {sheng_t}s", True, (255,0,0)), (300, 10))
    if sheng_t <= 0: chuangkou.blit(ziti.render("TIME UP!", True, (255, 0, 0)), (160, 180))

    pygame.display.flip(); shizhong.tick(60)
