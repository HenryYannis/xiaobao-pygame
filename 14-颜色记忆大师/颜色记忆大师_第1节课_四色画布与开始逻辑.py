# 颜色记忆大师_第1节课_四色画布与开始逻辑.py
# 学习目标：掌握 2x2 网格排列算法，并学习使用“状态变量”管理游戏的开始界面

import pygame  # 导入库（是什么），2D开发基础（为什么），直接调用（怎么用）

pygame.init()  # 初始化（是什么），激活硬件（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 300))  # 窗口（是什么），400x300（为什么），元组坐标（怎么用）
pygame.display.set_caption("Color Memory - Lesson 1")  # 标题（是什么），标识项目（为什么），传入文本（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36) # 组件（是什么），时钟与字体（为什么），一次性定义（怎么用）

# 变量初始化
zt = "ready"  # 状态标志（是什么），ready为准备, showing为演示（为什么），字符串记录（怎么用）
ys_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # 颜色库（是什么），红绿蓝黄（为什么），RGB元组列表（怎么用）

while True:  # 主循环
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit() # 退出（是什么），彻底关闭（为什么），直接退出（怎么用）

    chuangkou.fill((50, 50, 80))  # 刷背景（是什么），深蓝底色（为什么），填充（怎么用）
    
    if zt == "ready":  # 准备状态逻辑
        chuangkou.blit(ziti.render("Click to Start", True, (255, 255, 255)), (110, 130)) # 写字（是什么），提示开始（为什么），贴图（怎么用）
        if pygame.mouse.get_pressed()[0]: zt = "showing" # 点击鼠标（是什么），接收信号（为什么），切换状态位（怎么用）

    elif zt == "showing":  # 演示状态布局
        for i in range(4):  # 循环绘制 2x2 网格
            x, y = 50 + (i%2)*175, 50 + (i//2)*125 # 计算位置（是什么），取余与整除排列（为什么），数学公式（怎么用）
            pygame.draw.rect(chuangkou, ys_list[i], (x, y, 125, 100)) # 画矩形（是什么），展示色块（为什么），绘制（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成一帧（为什么），同步频率（怎么用）
