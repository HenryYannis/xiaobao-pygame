# 贪吃蛇_第1节课_基础框架.py
# 学习目标：掌握Pygame窗口初始化，理解游戏格点化(Grid)思维，并绘制出静止的蛇头

import pygame  # 导入pygame库（是什么），2D游戏开发的核心工具（为什么），直接调用其功能（怎么用）

pygame.init()  # 初始化所有模块（是什么），准备硬件资源（为什么），代码开头第一个调用（怎么用）

pingmu_kuan, pingmu_gao = 400, 400  # 定义窗口大小变量（是什么），设定400x400规格（为什么），方便后续统一修改（怎么用）
chuangkou = pygame.display.set_mode((pingmu_kuan, pingmu_gao))  # 创建游戏窗口（是什么），定义可见舞台（为什么），传入宽高的元组（怎么用）
pygame.display.set_caption("Snake - Lesson 1")  # 设置窗口标题（是什么），标识项目名称（为什么），传入字符串即可（怎么用）

shizhong = pygame.time.Clock()  # 创建时钟对象（是什么），控制游戏更新频率（为什么），调用tick锁定帧率（怎么用）

# 贪吃蛇游戏通常基于方格移动，这里设定每个方格为 20x20 像素
gedian_daxiao = 20  # 设定格点大小（是什么），定义蛇和食物的基础尺寸（为什么），后续所有坐标都应是这个值的倍数（怎么用）
# 蛇头初始坐标，设在窗口中心位置
shetou_weizhi = [200, 200]  # 定义蛇头位置（是什么），存储[x, y]坐标（为什么），列表格式方便后面修改数值（怎么用）

yunxing = True  # 定义运行标志（是什么），作为主循环的开关（为什么），True代表正在运行（怎么用）
while yunxing:  # 开启主循环（是什么），不断刷新游戏状态（为什么），只要yunxing为真就一直执行（怎么用）
    for shijian in pygame.event.get():  # 遍历事件队列（是什么），监听玩家动作（为什么），通过get获取所有新事件（怎么用）
        if shijian.type == pygame.QUIT:  # 检查退出事件（是什么），点击关闭按钮（为什么），判断事件类型（怎么用）
            yunxing = False  # 停止循环（是什么），安全关闭窗口（为什么），将变量设为False（怎么用）

    chuangkou.fill((0, 0, 0))  # 刷黑背景（是什么），擦除旧画面（为什么），传入(0,0,0)代表黑色RGB（怎么用）
    
    # 绘制蛇头：在当前位置画一个绿色正方形
    # 参数说明：(窗口, 颜色, (x, y, 宽度, 高度))
    pygame.draw.rect(chuangkou, (0, 255, 0), (shetou_weizhi[0], shetou_weizhi[1], gedian_daxiao, gedian_daxiao))  # 画矩形（是什么），代表蛇头（为什么），传入位置和尺寸参数（怎么用）

    pygame.display.flip()  # 刷新显示（是什么），将画好的内容呈现在屏幕上（为什么），循环最后一步必做（怎么用）
    shizhong.tick(60)  # 锁定60帧（是什么），统一不同电脑上的速度（为什么），每秒刷新60次（怎么用）

pygame.quit()  # 退出程序（是什么），释放系统内存（为什么），整个代码最后运行（怎么用）
