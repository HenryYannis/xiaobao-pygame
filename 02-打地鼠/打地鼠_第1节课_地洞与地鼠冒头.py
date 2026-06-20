# 打地鼠_第1节课_地洞与地鼠冒头.py
# 学习目标：掌握如何使用列表定义多个固定位置，并利用随机数控制地鼠的“冒头”逻辑

import pygame, random  # 导入库

pygame.init()  # 初始化
chuangkou = pygame.display.set_mode((400, 400))  # 窗口
pygame.display.set_caption("Whac-A-Mole - Lesson 1")  # 标题
shizhong = pygame.time.Clock()  # 时钟

# 变量定义：地洞的中心位置列表（九宫格布局）
didong_list = []  # 洞口容器（是什么），存储9个固定的坐标（为什么），用循环生成提高效率（怎么用）
for h in range(3):  # 遍历行
    for l in range(3):  # 遍历列
        didong_list.append([l * 120 + 80, h * 120 + 80])  # 计算坐标（是什么），排列地洞阵列（为什么），列表追加[x,y]（怎么用）

# 状态变量：当前地鼠出现的洞口索引，-1表示地鼠没冒头
dishu_idx = -1  # 地鼠索引（是什么），记录地鼠在哪个洞（为什么），初始设为-1表示隐藏（怎么用）
xiayici_shijian = 0  # 计时器（是什么），控制冒头频率（为什么），变量初始化（怎么用）

yunxing = True
while yunxing:
    shijian_now = pygame.time.get_ticks()  # 获取当前毫秒数
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False

    # 逻辑更新：每隔 1 秒，地鼠随机换个洞冒头
    if shijian_now > xiayici_shijian:  # 频率控制（是什么），定时切换位置（为什么），对比时间戳（怎么用）
        dishu_idx = random.randint(0, 8)  # 随机选洞（是什么），让地鼠冒出来（为什么），randint选择0-8索引（怎么用）
        xiayici_shijian = shijian_now + 1000  # 设定下次时间（是什么），每1000毫秒（1秒）切换一次（为什么），当前时间加1000（怎么用）

    chuangkou.fill((34, 139, 34))  # 刷草地绿背景（是什么），视觉氛围（为什么），填充RGB(34,139,34)（怎么用）
    
    # 绘制所有地洞和当前地鼠
    for idx, pos in enumerate(didong_list):
        pygame.draw.circle(chuangkou, (50, 25, 0), pos, 40)  # 画洞（是什么），深褐色圆圈（为什么），draw.circle绘图（怎么用）
        if idx == dishu_idx:  # 如果是地鼠洞（是什么），执行绘制（为什么），判断索引匹配（怎么用）
            pygame.draw.circle(chuangkou, (200, 150, 100), pos, 30)  # 画地鼠（是什么），浅褐色小圆（为什么），代表地鼠身体（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
