# 点击消除_第2节课_精准消除.py
# 学习目标：在第1节课基础上，学习捕捉鼠标点击位置，并利用距离公式判定是否击中并消除气泡

import pygame, random, math  # 导入库（是什么），增加数学库计算距离（为什么），组合导入（怎么用）

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong = pygame.time.Clock()

qipao_list = []  # 气泡容器

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        
        # 新增代码：监听鼠标按下事件
        if ev.type == pygame.MOUSEBUTTONDOWN:  # 点击判定（是什么），触发消除动作（为什么），判断事件类型（怎么用）
            mx, my = pygame.mouse.get_pos()  # 读坐标（是什么），获取点击位置（为什么），返回x,y元组（怎么用）
            # 新增逻辑：遍历气泡列表，检测哪个气泡被点中了
            for i in range(len(qipao_list)-1, -1, -1):  # 倒序遍历（是什么），安全删除气泡（为什么），从后往前遍历索引（怎么用）
                qx, qy = qipao_list[i]  # 提取气泡坐标（是什么），准备计算（为什么），解包变量（怎么用）
                # 利用勾股定理计算点击点与圆心的距离
                if math.hypot(mx - qx, my - qy) < 20:  # 碰撞检测（是什么），判断是否点在圆内（为什么），距离小于半径20（怎么用）
                    qipao_list.pop(i)  # 气泡消除（是什么），给玩家成功反馈（为什么），执行pop操作（怎么用）
                    break  # 跳出循环（是什么），一键只消一泡（为什么），结束当前for（怎么用）

    if random.random() < 0.03: qipao_list.append([random.randint(20, 380), random.randint(20, 380)])

    chuangkou.fill((255, 255, 255))
    for qp in qipao_list: pygame.draw.circle(chuangkou, (0, 150, 255), qp, 20, 2)

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
