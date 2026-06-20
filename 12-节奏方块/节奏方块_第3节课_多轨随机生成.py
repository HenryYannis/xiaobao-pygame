# 节奏方块_第3节课_多轨随机生成.py
# 学习目标：在第2节课基础上，学习使用列表管理多个方块，并利用随机数在不同轨道生成它们

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 600))
shizhong = pygame.time.Clock()

# 新增变量：使用列表存储多个方块的 [x, y] 坐标
fang_list = []  # 方块容器（是什么），管理屏幕上所有节奏块（为什么），初始为空列表（怎么用）
# 预设三个轨道中心：100, 200, 300
guidao = [75, 175, 275]  # 轨道列表（是什么），定义方块下落的路径（为什么），预设三个x坐标（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            # 新增代码：遍历列表检测是否有任何方块被击中
            for i in range(len(fang_list)-1, -1, -1):  # 倒序循环（是什么），安全删除元素（为什么），遍历列表索引（怎么用）
                if abs(fang_list[i][1] + 25 - 500) < 30:  # 击中判断（是什么），检测所有方块（为什么），公式计算距离（怎么用）
                    fang_list.pop(i); break  # 消除并跳出（是什么），一键一消（为什么），pop删除并break（怎么用）

    # 新增代码：以一定概率随机产生新方块
    if random.random() < 0.02:  # 概率生成（是什么），控制游戏节奏（为什么），随机数判断（怎么用）
        fang_list.append([random.choice(guidao), -50])  # 添加方块（是什么），放入随机轨道（为什么），列表追加坐标（怎么用）

    # 逻辑更新：遍历更新所有方块位置
    for f in fang_list: f[1] += 5  # 更新位置（是什么），群体移动（为什么），循环修改y值（怎么用）
    fang_list = [f for f in fang_list if f[1] < 600]  # 出界清理（是什么），防止列表过长（为什么），列表推导式重构（怎么用）

    chuangkou.fill((30, 30, 30))
    pygame.draw.line(chuangkou, (100, 100, 100), (0, 500), (400, 500), 5)
    for f in fang_list: pygame.draw.rect(chuangkou, (0, 255, 255), (f[0], f[1], 50, 50))  # 循环绘制（是什么），显示所有块（为什么），draw绘图（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
