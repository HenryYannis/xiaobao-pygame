# 弹跳球接球_第2节课_弹性反弹.py
# 学习目标：在第1节课基础上，学习判定挡板接球的逻辑，并实现物理反弹与随机偏移

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong = pygame.time.Clock()

qiu_pos, qiu_sudu = [200, 50], [0, 4]
ban_x = 160

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False

    # 逻辑更新：球的位置更新（包含x和y）
    qiu_pos[0] += qiu_sudu[0]  # 水平移动（是什么），增加横向轨迹（为什么），坐标累加（怎么用）
    qiu_pos[1] += qiu_sudu[1]  # 垂直移动
    
    # 左右墙壁反弹
    if qiu_pos[0] <= 10 or qiu_pos[0] >= 390: qiu_sudu[0] *= -1  # 墙壁碰撞（是什么），防止球出界（为什么），速度取反（怎么用）
    # 顶部反弹
    if qiu_pos[1] <= 10: qiu_sudu[1] = abs(qiu_sudu[1])  # 撞顶（是什么），向下反弹（为什么），确保速度为正数（怎么用）

    # 新增代码：挡板接球判定与反弹
    if qiu_pos[1] >= 360 and ban_x <= qiu_pos[0] <= ban_x + 80:  # 接球判定（是什么），触发反弹动作（为什么），坐标区间判断（怎么用）
        qiu_sudu[1] = -5  # 向上反弹（是什么），给球升力（为什么），速度设为负值（怎么用）
        # 新增逻辑：反弹时加入随机的水平偏移速度
        qiu_sudu[0] = random.randint(-3, 3)  # 随机角度（是什么），增加难度（为什么），randint设定横向分量（怎么用）

    if qiu_pos[1] > 400: qiu_pos, qiu_sudu = [200, 50], [0, 4] # 掉落重置

    jp = pygame.key.get_pressed()
    if jp[pygame.K_LEFT] and ban_x > 0: ban_x -= 6
    if jp[pygame.K_RIGHT] and ban_x < 320: ban_x += 6

    chuangkou.fill((30, 30, 30))
    pygame.draw.circle(chuangkou, (255, 255, 255), qiu_pos, 10)
    pygame.draw.rect(chuangkou, (0, 255, 100), (ban_x, 370, 80, 10))

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
