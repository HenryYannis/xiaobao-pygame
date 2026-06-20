# 黄金矿工_第4节课_抓取与载重.py
# 学习目标：在第3节课基础上，学习如何实现物体粘连跟随效果，并模拟不同重量的拉回速度

import pygame, math, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong = pygame.time.Clock()

zx, cd, jd, zt = [200, 50], 50, 0, 0
jinks = [[random.randint(50,350), random.randint(150,350), random.randint(10,30)] for _ in range(5)]
# 新增变量：记录当前抓到的物体属性，None表示没抓到
zhua_dao = None  # 抓取物（是什么），存储当前在钩子上的物体信息（为什么），None或[半径]列表（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE and zt == 0: zt = 1

    if zt == 0: jd = math.sin(pygame.time.get_ticks() / 500) * 80
    elif zt == 1: cd += 5
    elif zt == 2:  # 收回模式
        # 新增逻辑：根据抓到物体的大小减慢回收速度
        sudu = 5 - (zhua_dao[2]//10 if zhua_dao else 0)  # 载重计算（是什么），实现重量感（为什么），减小cd的递减量（怎么用）
        cd -= max(1, sudu)  # 至少保持1的速度回收（是什么），防止拉不动（为什么），减去速度值（怎么用）
        if cd <= 50: zt, cd, zhua_dao = 0, 50, None  # 卸货重置（是什么），抓到顶后清除抓取物（为什么），变量清空（怎么用）

    if cd > 350: zt = 2
    hudu = math.radians(jd + 90)
    mx, my = zx[0] + cd * math.cos(hudu), zx[1] + cd * math.sin(hudu)

    # 新增代码：碰撞后不再直接删除，而是转为“抓取”状态
    if zt == 1:  # 只有在下放时才检测抓取
        for i, jk in enumerate(jinks):
            if math.hypot(mx - jk[0], my - jk[1]) < jk[2]:
                zhua_dao = jinks.pop(i); zt = 2; break  # 转移对象（是什么），从地面转到钩子上（为什么），赋值给zhua_dao变量（怎么用）

    chuangkou.fill((255, 255, 200))
    for jx, jy, jr in jinks: pygame.draw.circle(chuangkou, (255, 215, 0), (jx, jy), jr)
    if zhua_dao: pygame.draw.circle(chuangkou, (255, 215, 0), (mx, my), zhua_dao[2]) # 绘制抓到的金块（是什么），随钩子移动（为什么），坐标设为(mx,my)（怎么用）
    pygame.draw.line(chuangkou, (0, 0, 0), zx, (mx, my), 3); pygame.draw.circle(chuangkou, (100, 50, 0), zx, 10)

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
