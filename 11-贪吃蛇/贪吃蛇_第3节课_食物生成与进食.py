# 贪吃蛇_第3节课_食物生成与进食.py
# 学习目标：在第2节课基础上，学习如何随机生成食物并在蛇头经过时完成“进食”逻辑

import pygame, random  # 导入库（是什么），增加随机数功能（为什么），组合导入（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），设置舞台（为什么），传入元组（怎么用）
pygame.display.set_caption("Snake - Lesson 3")  # 标题（是什么），第3课（为什么），传入文本（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），控制FPS（为什么），定速10（怎么用）

gedian, sudu = 20, [0, 0]  # 基础参数（是什么），格点和初始速度（为什么），多变量同时定义（怎么用）
shetou_x, shetou_y = 200, 200  # 蛇头坐标（是什么），初始位置（为什么），变量初始化（怎么用）

# 新增变量：随机生成食物的坐标（必须是格点的整数倍）
# random.randint(0, 19)生成0到19的随机整数，乘以20后正好对齐格点
shiwu_x = random.randint(0, 19) * gedian  # 食物x（是什么），水平随机位置（为什么），公式对齐格点（怎么用）
shiwu_y = random.randint(0, 19) * gedian  # 食物y（是什么），垂直随机位置（为什么），公式对齐格点（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理每一帧（为什么），不断重复（怎么用）
    for shijian in pygame.event.get():  # 事件监听（是什么），捕捉动作（为什么），轮询获取（怎么用）
        if shijian.type == pygame.QUIT: yunxing = False  # 退出（是什么），点击关闭（为什么），改状态位（怎么用）
        if shijian.type == pygame.KEYDOWN:  # 按键判断（是什么），改变移动方向（为什么），判断常量（怎么用）
            if shijian.key == pygame.K_UP: sudu = [0, -gedian]  # 向上移动（是什么），y坐标减小（为什么），设为负速（怎么用）
            if shijian.key == pygame.K_DOWN: sudu = [0, gedian]  # 向下移动（是什么），y坐标增加（为什么），设为正速（怎么用）
            if shijian.key == pygame.K_LEFT: sudu = [-gedian, 0]  # 向左移动（是什么），x坐标减小（为什么），设为负速（怎么用）
            if shijian.key == pygame.K_RIGHT: sudu = [gedian, 0]  # 向右移动（是什么），x坐标增加（为什么），设为正速（怎么用）

    shetou_x += sudu[0]; shetou_y += sudu[1]  # 更新位置（是什么），持续位移（为什么），原坐标累加速度（怎么用）

    # 新增代码：检查是否吃到食物（蛇头坐标与食物坐标完全重合）
    if shetou_x == shiwu_x and shetou_y == shiwu_y:  # 进食判断（是什么），判定重合（为什么），使用双等号判断相等（怎么用）
        shiwu_x = random.randint(0, 19) * gedian  # 重新生成食物（是什么），让游戏继续（为什么），重复随机计算（怎么用）
        shiwu_y = random.randint(0, 19) * gedian  # 重新生成位置（是什么），位置变化（为什么），重复随机计算（怎么用）

    chuangkou.fill((0, 0, 0))  # 刷黑（是什么），清除旧像（为什么），黑色填充（怎么用）
    pygame.draw.rect(chuangkou, (0, 255, 0), (shetou_x, shetou_y, gedian, gedian))  # 画蛇头（是什么），显示位置（为什么），绿色矩形（怎么用）
    
    # 新增代码：绘制红色方块作为食物
    pygame.draw.rect(chuangkou, (255, 0, 0), (shiwu_x, shiwu_y, gedian, gedian))  # 画食物（是什么），给玩家目标（为什么），红色矩形区分（怎么用）

    pygame.display.flip()  # 刷新（是什么），可见更新（为什么），flip方法（怎么用）
    shizhong.tick(10)  # 定帧10（是什么），方便观察（为什么），锁定低FPS（怎么用）

pygame.quit()  # 退出（是什么），资源回收（为什么），收尾工作（怎么用）
