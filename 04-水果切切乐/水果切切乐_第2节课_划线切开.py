# 水果切切乐_第2节课_划线切开.py
# 学习目标：掌握鼠标轨迹捕捉逻辑，并学习如何判定“线与圆”的交叉接触实现切割效果

import pygame, random, math  # 导入库（是什么），支持核心、随机与数学（为什么），必备环境（怎么用）

pygame.init()  # 初始化
chuangkou = pygame.display.set_mode((400, 400))
shizhong = pygame.time.Clock()

sg_list = []  # 水果列表
guiji = []  # 新增变量：鼠标轨迹点列表（是什么），记录滑动路线（为什么），用于碰撞判定（怎么用）

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()

    # 捕捉鼠标轨迹
    mx, my = pygame.mouse.get_pos()  # 读鼠标（是什么），获取坐标（为什么），返回元组（怎么用）
    if pygame.mouse.get_pressed()[0]: guiji.append((mx, my))  # 记录点（是什么），生成轨迹（为什么），追加到列表（怎么用）
    if len(guiji) > 10: guiji.pop(0)  # 保持长度（是什么），只留最近10点（为什么），删除首项（怎么用）
    if not pygame.mouse.get_pressed()[0]: guiji.clear() # 松开清空

    if random.random() < 0.02: sg_list.append([random.randint(50, 350), 410, random.uniform(-2, 2), -8])

    for i in range(len(sg_list)-1, -1, -1):
        s = sg_list[i]; s[0] += s[2]; s[1] += s[3]; s[3] += 0.2
        # 新增代码：切割碰撞检测
        for p in guiji:  # 遍历轨迹点（是什么），检测交叉（为什么），循环比对（怎么用）
            if math.hypot(p[0]-s[0], p[1]-s[1]) < 20: # 划中判定（是什么），两点间距（为什么），调用math.hypot（怎么用）
                sg_list.pop(i); break # 切开效果（是什么），移除物体（为什么），终止内层循环（怎么用）
        if i < len(sg_list) and s[1] > 420: sg_list.pop(i)

    chuangkou.fill((30, 30, 30))
    for s in sg_list: pygame.draw.circle(chuangkou, (255, 100, 0), (int(s[0]), int(s[1])), 20)
    # 新增代码：绘制白色刀光轨迹
    if len(guiji) > 1: pygame.draw.lines(chuangkou, (255, 255, 255), False, guiji, 3) # 画线条（是什么），视觉回馈（为什么），lines方法绘制（怎么用）

    pygame.display.flip(); shizhong.tick(60)
