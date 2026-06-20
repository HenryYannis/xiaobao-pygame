# 横版飞行避障_第2节课_障碍物横移.py
# 学习目标：掌握横版游戏的核心逻辑：玩家水平不动，障碍物向左横移，模拟出向右飞行的错觉

import pygame, random  # 导入库（是什么），支持核心与随机（为什么），组合导入（怎么用）

pygame.init()  # 初始化
chuangkou = pygame.display.set_mode((400, 500))
shizhong = pygame.time.Clock()

bird = [50, 250, 0] # 玩家
# 新增变量：障碍物列表 [x, 上高度, 下高度, 宽]
zhangai_list = []  # 容器（是什么），管理管子（为什么），列表初始化（怎么用）

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE: bird[2] = -8

    bird[2] += 0.4; bird[1] += bird[2] # 物理更新

    # 新增代码：随机生成障碍物
    if len(zhangai_list) == 0 or zhangai_list[-1][0] < 200: # 间距判定（是什么），保持管子疏密（为什么），判断最后管子位置（怎么用）
        h = random.randint(100, 300) # 随机高度（是什么），增加难度（为什么），randint计算（怎么用）
        zhangai_list.append([400, h]) # 生成在最右侧（是什么），准备左移（为什么），追加[x, y]（怎么用）

    # 更新障碍物位置
    for i in range(len(zhangai_list)-1, -1, -1):
        zhangai_list[i][0] -= 3  # 向左移（是什么），产生飞行错觉（为什么），x坐标递减（怎么用）
        if zhangai_list[i][0] < -50: zhangai_list.pop(i) # 移出屏幕删除

    chuangkou.fill((100, 200, 255))
    pygame.draw.circle(chuangkou, (255, 255, 0), (int(bird[0]), int(bird[1])), 15)
    # 新增代码：绘制障碍物（管子）
    for za in zhangai_list:
        pygame.draw.rect(chuangkou, (0, 200, 0), (za[0], 0, 50, za[1])) # 上管子（是什么），矩形显示（为什么），(x,0,w,h)（怎么用）
        pygame.draw.rect(chuangkou, (0, 200, 0), (za[0], za[1]+120, 50, 500)) # 下管子（是什么），留出120空隙（为什么），(x,y,w,h)（怎么用）

    pygame.display.flip(); shizhong.tick(60)
