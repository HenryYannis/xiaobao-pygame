# 贪吃蛇_第4节课_身体增长逻辑.py
# 学习目标：在第3节课基础上，学习使用列表管理蛇身坐标，并实现进食后身体变长的核心算法

import pygame, random  # 导入库（是什么），功能支撑（为什么），必备（怎么用）

pygame.init()  # 初始化（是什么），准备引擎（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），设置舞台（为什么），宽高元组（怎么用）
pygame.display.set_caption("Snake - Lesson 4")  # 标题（是什么），第4课（为什么），传入文本（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），控制FPS（为什么），定帧10（怎么用）

gedian, sudu = 20, [0, 0]  # 基础参数（是什么），格点和初始速度（为什么），多变量定义（怎么用）
shetou_x, shetou_y = 200, 200  # 坐标初始化（是什么），起始位置（为什么），变量赋值（怎么用）

# 新增变量：蛇身列表，存储所有关节的坐标
she_shen = [[200, 200]]  # 蛇身容器（是什么），存储一串[x,y]坐标（为什么），用列表存储多个关节实现跟随（怎么用）
shiwu_x, shiwu_y = random.randint(0, 19) * gedian, random.randint(0, 19) * gedian  # 食物初态（是什么），随机位置（为什么），对齐格点（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理每一帧（为什么），不断重复（怎么用）
    for shijian in pygame.event.get():  # 事件监听（是什么），捕捉动作（为什么），轮询获取（怎么用）
        if shijian.type == pygame.QUIT: yunxing = False  # 退出（是什么），点击关闭（为什么），改状态位（怎么用）
        if shijian.type == pygame.KEYDOWN:  # 方向控制（是什么），改变移动轨迹（为什么），判断常量（怎么用）
            if shijian.key == pygame.K_UP: sudu = [0, -gedian]  # 向上（是什么），y减（为什么），赋值（怎么用）
            if shijian.key == pygame.K_DOWN: sudu = [0, gedian]  # 向下（是什么），y加（为什么），赋值（怎么用）
            if shijian.key == pygame.K_LEFT: sudu = [-gedian, 0]  # 向左（是什么），x减（为什么），赋值（怎么用）
            if shijian.key == pygame.K_RIGHT: sudu = [gedian, 0]  # 向右（是什么），x加（为什么），赋值（怎么用）

    # 新增代码：核心移动算法——“加头去尾”
    shetou_x += sudu[0]; shetou_y += sudu[1]  # 更新虚拟头位置（是什么），计算新坐标（为什么），累加速度（怎么用）
    she_shen.insert(0, [shetou_x, shetou_y])  # 增加新头部（是什么），让蛇向前伸展（为什么），在列表首位插入新坐标（怎么用）

    if shetou_x == shiwu_x and shetou_y == shiwu_y:  # 进食判断（是什么），判定重合（为什么），双等号判断（怎么用）
        shiwu_x, shiwu_y = random.randint(0, 19) * gedian, random.randint(0, 19) * gedian  # 刷食物（是什么），消失并重现（为什么），重新随机（怎么用）
    else:  # 新增逻辑：如果没有吃到食物，则删除末尾
        she_shen.pop()  # 删除尾部（是什么），维持长度不变（为什么），移除列表最后一项（怎么用）

    chuangkou.fill((0, 0, 0))  # 刷黑（是什么），清除旧像（为什么），黑色填充（怎么用）
    pygame.draw.rect(chuangkou, (255, 0, 0), (shiwu_x, shiwu_y, gedian, gedian))  # 画食物（是什么），红色方块（为什么），矩形绘制（怎么用）
    
    # 新增代码：遍历蛇身列表绘制所有关节
    for guanjie in she_shen:  # 遍历身体（是什么），画出整条蛇（为什么），for in循环读取坐标（怎么用）
        pygame.draw.rect(chuangkou, (0, 255, 0), (guanjie[0], guanjie[1], gedian, gedian))  # 画关节（是什么），绿色显示（为什么），使用关节坐标（怎么用）

    pygame.display.flip()  # 刷新（是什么），可见更新（为什么），flip方法（怎么用）
    shizhong.tick(10)  # 定帧10（是什么），方便观察（为什么），锁定低FPS（怎么用）

pygame.quit()  # 退出（是什么），资源回收（为什么），收尾工作（怎么用）
