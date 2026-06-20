# 水果切切乐_第1节课_水果抛射.py
# 学习目标：掌握如何使用初速度与重力模拟物体的抛物线运动，实现水果从屏幕下方抛出的效果

import pygame, random  # 导入库（是什么），驱动逻辑与随机（为什么），必备环境（怎么用）

pygame.init()  # 初始化（是什么），引擎预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），400x400舞台（为什么），元组参数（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），定帧器（为什么），锁定60FPS（怎么用）

# 水果属性：[x, y, vx, vy]
shuiguo_list = []  # 容器（是什么），存储所有水果（为什么），列表初始化（怎么用）
zhongli = 0.2  # 重力（是什么），持续向下的加速度（为什么），变量控制难度（怎么用）

while True:  # 主循环
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()

    # 随机生成抛出的水果
    if random.random() < 0.02:  # 生成判定（是什么），控制出机率（为什么），随机小数判断（怎么用）
        # 初始位置在底部，带有向上的初速度(vy为负)
        shuiguo_list.append([random.randint(50, 350), 410, random.uniform(-2, 2), -8]) # 存入[x,y,水平速,垂直速]（是什么），定义初始冲力（为什么），追加列表项（怎么用）

    # 更新位置
    for i in range(len(shuiguo_list)-1, -1, -1):
        s = shuiguo_list[i]
        s[0] += s[2]; s[1] += s[3]  # 位置更新（是什么），实现移动（为什么），坐标累加速度（怎么用）
        s[3] += zhongli  # 重力模拟（是什么），垂直速度变大（为什么），实现抛物线（怎么用）
        if s[1] > 420: shuiguo_list.pop(i)  # 掉落销毁（是什么），清理资源（为什么），索引弹出（怎么用）

    chuangkou.fill((30, 30, 30))  # 刷黑背景（是什么），清屏（为什么），填充（怎么用）
    for s in shuiguo_list: pygame.draw.circle(chuangkou, (255, 100, 0), (int(s[0]), int(s[1])), 20) # 画橙子（是什么），显示圆（为什么），绘制（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成一帧（为什么），同步频率（怎么用）
