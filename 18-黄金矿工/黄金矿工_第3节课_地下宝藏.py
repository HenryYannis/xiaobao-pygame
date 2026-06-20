# 黄金矿工_第3节课_地下宝藏.py
# 学习目标：在第2节课基础上，学习使用列表生成地下金块，并实现钩子对物体的碰撞检测

import pygame, math, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong = pygame.time.Clock()

zhongxin, changdu, jiaodu, zhuangtai = [200, 50], 50, 0, 0
# 新增变量：金块列表，存储每个金块的 [x, y, 半径]
jinkuan_list = [[random.randint(50, 350), random.randint(150, 350), random.randint(10, 30)] for _ in range(5)]  # 宝藏容器（是什么），存储5个随机金块（为什么），列表推导式高效生成（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE and zhuangtai == 0: zhuangtai = 1

    if zhuangtai == 0: jiaodu = math.sin(pygame.time.get_ticks() / 500) * 80
    elif zhuangtai == 1: changdu += 5
    elif zhuangtai == 2: changdu -= 5
    if changdu > 350: zhuangtai = 2
    if changdu <= 50: zhuangtai = 0; changdu = 50

    hudu = math.radians(jiaodu + 90)
    mx, my = zhongxin[0] + changdu * math.cos(hudu), zhongxin[1] + changdu * math.sin(hudu)

    # 新增代码：碰撞检测逻辑。如果钩子末端接近金块，本课先简单实现金块消失并收钩
    for i in range(len(jinkuan_list)-1, -1, -1):  # 倒序遍历（是什么），检查每个金块（为什么），for in索引循环（怎么用）
        jx, jy, jr = jinkuan_list[i]  # 提取属性（是什么），金块坐标半径（为什么），解包变量（怎么用）
        if math.hypot(mx - jx, my - jy) < jr:  # 碰撞判定（是什么），核对距离（为什么），调用math.hypot（怎么用）
            jinkuan_list.pop(i); zhuangtai = 2; break  # 处理击中（是什么），金块消失并强制收钩（为什么），pop操作加改状态（怎么用）

    chuangkou.fill((255, 255, 200))
    for jx, jy, jr in jinkuan_list: pygame.draw.circle(chuangkou, (255, 215, 0), (jx, jy), jr)  # 画金块（是什么），金色圆圈（为什么），循环调用draw.circle（怎么用）
    pygame.draw.line(chuangkou, (0, 0, 0), zhongxin, (mx, my), 3)
    pygame.draw.circle(chuangkou, (100, 50, 0), zhongxin, 10)

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
