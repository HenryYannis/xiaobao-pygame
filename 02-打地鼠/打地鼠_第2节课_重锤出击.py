# 打地鼠_第2节课_重锤出击.py
# 学习目标：在第1节课基础上，学习捕捉鼠标点击位置，并判定是否精准点击到了地鼠

import pygame, random, math  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong = pygame.time.Clock()

didong_list = [[l*120+80, h*120+80] for h in range(3) for l in range(3)] # 列表推导式简化地洞
dishu_idx, xiayici_shijian = -1, 0

yunxing = True
while yunxing:
    shijian_now = pygame.time.get_ticks()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        
        # 新增代码：监听鼠标点击，进行“打地鼠”判定
        if ev.type == pygame.MOUSEBUTTONDOWN and dishu_idx != -1:  # 点击判定（是什么），判定是否打中（为什么），判断按下且有地鼠（怎么用）
            mx, my = pygame.mouse.get_pos()  # 读位置（是什么），获取落锤点（为什么），返回x,y（怎么用）
            # 新增逻辑：计算鼠标与当前地鼠中心的距离
            dx, dy = didong_list[dishu_idx]  # 地鼠坐标（是什么），目标点（为什么），读取索引位置（怎么用）
            if math.hypot(mx - dx, my - dy) < 30:  # 命中判定（是什么），核对打击范围（为什么），距离小于半径30（怎么用）
                dishu_idx = -1  # 成功击中（是什么），地鼠缩回（为什么），重置索引（怎么用）
                xiayici_shijian = shijian_now + 500  # 暂停间隔（是什么），缩短下次冒头间隔（为什么），减半等待时间（怎么用）

    if shijian_now > xiayici_shijian:
        dishu_idx = random.randint(0, 8)
        xiayici_shijian = shijian_now + 1000

    chuangkou.fill((34, 139, 34))
    for idx, pos in enumerate(didong_list):
        pygame.draw.circle(chuangkou, (50, 25, 0), pos, 40)
        if idx == dishu_idx: pygame.draw.circle(chuangkou, (200, 150, 100), pos, 30)

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
