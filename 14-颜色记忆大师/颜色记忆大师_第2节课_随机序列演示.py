# 颜色记忆大师_第2节课_随机序列演示.py
# 学习目标：掌握随机列表的生成，并利用时间戳控制物体演示的节奏与时长

import pygame, random, time  # 导入库（是什么），增加随机与时间（为什么），必备环境（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 300))  # 窗口（是什么），定义舞台（为什么），元组参数（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)  # 组件（是什么），时钟与字体（为什么），一次性定义（怎么用）

yanses, zt, xulie = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)], "ready", []  # 基础变量（是什么），包含状态与序列（为什么），变量初始化（怎么用）
# 新增变量：演示控制
idx, next_t = 0, 0  # 进度与切换点（是什么），控制播放节奏（为什么），变量记录（怎么用）

while True:  # 主循环
    now = time.time()  # 获取时间（是什么），实现秒级对比（为什么），调用time.time（怎么用）
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()

    chuangkou.fill((50, 50, 80))
    if zt == "ready":
        chuangkou.blit(ziti.render("Click to Start", True, (255, 255, 255)), (110, 130))
        if pygame.mouse.get_pressed()[0]:
            # 新增逻辑：产生 3 个随机色号
            zt, xulie, idx, next_t = "showing", [random.randint(0, 3) for _ in range(3)], 0, now + 1.0

    elif zt == "showing":
        # 新增代码：定时切换演示
        if now >= next_t:  # 时机已到（是什么），切换下一个（为什么），对比当前时间（怎么用）
            idx += 1; next_t = now + 0.8  # 步进（是什么），0.8秒跳变（为什么），更新索引与时间（怎么用）
            if idx >= len(xulie): zt = "ready" # 本课先循环回起点

        if idx < len(xulie): # 绘制演示块
            pygame.draw.rect(chuangkou, yanses[xulie[idx]], (100, 100, 200, 100)) # 显颜色（是什么），展示考题（为什么），绘制（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新并定帧（是什么），同步频率（为什么），锁定60FPS（怎么用）
