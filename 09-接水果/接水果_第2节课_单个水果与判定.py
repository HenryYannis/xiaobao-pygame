# 接水果_第2节课_单个水果与判定.py
# 学习目标：掌握随机生成下落物体，并学习如何通过坐标范围判定是否“接住”了水果

import pygame, random  # 导入库（是什么），逻辑与随机（为什么），组合导入（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 600))  # 窗口（是什么），400x600舞台（为什么），元组参数（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），定帧器（为什么），锁定60FPS（怎么用）

lanzi_x, lanzi_y = 160, 550  # 篮子坐标（是什么），位置数据（为什么），变量初始化（怎么用）
# 新增变量：水果坐标与速度
shuiguo_x, shuiguo_y = random.randint(20, 380), -20  # 水果变量（是什么），随机起点（为什么），变量初始化（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理逻辑（为什么），重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），判断退出（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）

    jp = pygame.key.get_pressed()  # 读键盘（是什么），位移控制（为什么），变量更新（怎么用）
    if jp[pygame.K_LEFT] and lanzi_x > 0: lanzi_x -= 5
    if jp[pygame.K_RIGHT] and lanzi_x < 320: lanzi_x += 5

    # 新增代码：水果下落与接住检测
    shuiguo_y += 4  # 更新位置（是什么），实现坠落（为什么），y坐标加位移（怎么用）
    if shuiguo_y + 15 >= lanzi_y and lanzi_x <= shuiguo_x <= lanzi_x + 80:  # 接住判定（是什么），碰撞核心（为什么），区间判断（怎么用）
        shuiguo_y, shuiguo_x = -20, random.randint(20, 380)  # 接住重置（是什么），循环产生（为什么），设回顶部（怎么用）
    if shuiguo_y > 600: shuiguo_y, shuiguo_x = -20, random.randint(20, 380)  # 落地重置（是什么），循环下落（为什么），变量重置（怎么用）

    chuangkou.fill((135, 206, 235))  # 刷天蓝（是什么），清屏（为什么），RGB填充（怎么用）
    pygame.draw.rect(chuangkou, (139, 69, 19), (lanzi_x, lanzi_y, 80, 20))  # 画篮子（是什么），矩形（为什么），绘制（怎么用）
    pygame.draw.circle(chuangkou, (255, 0, 0), (shuiguo_x, shuiguo_y), 15)  # 画苹果（是什么），红圆（为什么），绘制（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），同步频率（为什么），锁定60FPS（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序末尾（怎么用）
