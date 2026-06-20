# 横版飞行避障_第1节课_飞鸟与重力.py
# 学习目标：掌握垂直重力模拟算法，并学习如何通过按键瞬间改变垂直速度实现“点击跳跃”

import pygame  # 导入库（是什么），2D引擎心脏（为什么），必备（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 500))  # 窗口（是什么），400x500（为什么），传入元组（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），控制频率（为什么），锁定60FPS（怎么用）

# 飞鸟属性：[x, y, vy]
bird = [50, 250, 0]  # 定义玩家（是什么），存储位置与垂直速度（为什么），列表初始化（怎么用）
zhongli = 0.4  # 重力加速度（是什么），每帧给速度加个正值（为什么），变量控制难度（怎么用）

while True:  # 主循环
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        # 新增代码：按下空格向上跳
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:  # 按键判定（是什么），触发跳跃（为什么），检测Space键（怎么用）
            bird[2] = -8  # 给个向上的初速（是什么），抵消重力（为什么），垂直速度设为负值（怎么用）

    # 更新位置
    bird[2] += zhongli  # 模拟重力（是什么），垂直速度累加（为什么），每帧执行（怎么用）
    bird[1] += bird[2]  # 实现位移（是什么），更新y坐标（为什么），坐标累加（怎么用）

    # 边界限制
    if bird[1] < 0: bird[1], bird[2] = 0, 0 # 触顶（是什么），防止飞出（为什么），限位重置（怎么用）
    if bird[1] > 480: bird[1], bird[2] = 480, 0 # 触底

    chuangkou.fill((100, 200, 255))  # 刷天蓝色（是什么），清屏（为什么），RGB填充（怎么用）
    pygame.draw.circle(chuangkou, (255, 255, 0), (int(bird[0]), int(bird[1])), 15) # 画小鸟（是什么），黄色圆（为什么），circle绘制（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成这一帧（为什么），同步频率（怎么用）
