# 接水果_第1节课_篮子控制.py
# 学习目标：掌握Pygame窗口初始化，并学习使用键盘左右键控制篮子在屏幕底部移动

import pygame  # 导入库（是什么），2D开发工具（为什么），直接调用（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 600))  # 窗口（是什么），400x600（为什么），传入元组（怎么用）
pygame.display.set_caption("Catch Fruit - Lesson 1")  # 标题（是什么），第1课（为什么），传入文本（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），控制频率（为什么），锁定60FPS（怎么用）

# 篮子变量
lanzi_x, lanzi_y = 160, 550  # 篮子坐标（是什么），初始在底部中央（为什么），变量初始化（怎么用）
tian_lan = (135, 206, 235)  # 定义颜色（是什么），天蓝色（为什么），RGB元组（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理逻辑（为什么），持续执行（怎么用）
    for ev in pygame.event.get():  # 监听（是什么），捕捉动作（为什么），轮询（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态（怎么用）

    # 键盘检测
    jp = pygame.key.get_pressed()  # 读按键（是什么），长按检测（为什么），返回列表（怎么用）
    if jp[pygame.K_LEFT] and lanzi_x > 0: lanzi_x -= 5  # 左移（是什么），x减小且限位（为什么），变量更新（怎么用）
    if jp[pygame.K_RIGHT] and lanzi_x < 320: lanzi_x += 5  # 右移（是什么），x增加且限位（为什么），变量更新（怎么用）

    chuangkou.fill(tian_lan)  # 刷背景（是什么），清屏（为什么），填充天蓝（怎么用）
    # 画篮子
    pygame.draw.rect(chuangkou, (139, 69, 19), (lanzi_x, lanzi_y, 80, 20))  # 画矩形（是什么），代表篮子（为什么），传入坐标尺寸（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新并定帧（是什么），同步频率（为什么），锁定60FPS（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序末尾（怎么用）
