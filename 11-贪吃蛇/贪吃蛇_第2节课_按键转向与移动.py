# 贪吃蛇_第2节课_按键转向与移动.py
# 学习目标：在第1节课基础上，学习如何监听键盘按键并控制蛇头按格点持续移动

import pygame  # 导入库（是什么），基础工具（为什么），必需（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），400像素舞台（为什么），元组定义大小（怎么用）
pygame.display.set_caption("Snake - Lesson 2")  # 标题（是什么），第2课（为什么），传入文本（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），控制节奏（为什么），锁定帧率（怎么用）

gedian = 20  # 格点大小（是什么），统一方块尺寸（为什么），变量名使用拼音缩写（怎么用）
shetou_x, shetou_y = 200, 200  # 蛇头坐标（是什么），初始中点位置（为什么），变量初始化（怎么用）

# 新增变量：移动方向速度，[x轴速度, y轴速度]
# 初始设为(0,0)表示静止，直到玩家按键
sudu = [0, 0]  # 方向向量（是什么），控制移动轨迹（为什么），[20, 0]代表每帧向右跳一格（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理每一帧（为什么），不断重复（怎么用）
    for shijian in pygame.event.get():  # 事件监听（是什么），捕捉动作（为什么），轮询获取（怎么用）
        if shijian.type == pygame.QUIT: yunxing = False  # 退出（是什么），点击关闭（为什么），改标志位（怎么用）
        
        # 新增代码：根据按下的方向键修改速度方向
        if shijian.type == pygame.KEYDOWN:  # 键盘按下事件（是什么），监听按键（为什么），判断常量是否匹配（怎么用）
            if shijian.key == pygame.K_UP: sudu = [0, -gedian]  # 向上（是什么），y坐标减小（为什么），速度设为(0,-20)（怎么用）
            if shijian.key == pygame.K_DOWN: sudu = [0, gedian]  # 向下（是什么），y坐标增加（为什么），速度设为(0,20)（怎么用）
            if shijian.key == pygame.K_LEFT: sudu = [-gedian, 0]  # 向左（是什么），x坐标减小（为什么），速度设为(-20,0)（怎么用）
            if shijian.key == pygame.K_RIGHT: sudu = [gedian, 0]  # 向右（是什么），x坐标增加（为什么），速度设为(20,0)（怎么用）

    # 新增代码：更新蛇头位置
    shetou_x += sudu[0]  # 水平位移（是什么），根据速度移动（为什么），原坐标累加速度（怎么用）
    shetou_y += sudu[1]  # 垂直位移（是什么），根据速度移动（为什么），原坐标累加速度（怎么用）

    chuangkou.fill((0, 0, 0))  # 清屏（是什么），刷黑背景（为什么），fill方法（怎么用）
    pygame.draw.rect(chuangkou, (0, 255, 0), (shetou_x, shetou_y, gedian, gedian))  # 画蛇头（是什么），显示位置（为什么），传入矩形参数（怎么用）

    pygame.display.flip()  # 刷新（是什么），更新屏幕（为什么），flip方法（怎么用）
    # 贪吃蛇不能太快，这里设定为每秒刷新10次，即每秒走10格
    shizhong.tick(10)  # 控制速度（是什么），让蛇动得清晰（为什么），传入较低的FPS如10（怎么用）

pygame.quit()  # 退出（是什么），资源回收（为什么），收尾工作（怎么用）
