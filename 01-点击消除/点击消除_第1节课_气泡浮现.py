# 点击消除_第1节课_气泡浮现.py
# 学习目标：掌握如何使用列表管理多个对象，并利用随机数与概率在屏幕上生成气泡

import pygame, random  # 导入库（是什么），2D引擎与随机数（为什么），必备组件（怎么用）

pygame.init()  # 初始化（是什么），引擎预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），400x400舞台（为什么），元组参数（怎么用）
pygame.display.set_caption("Click Pop - Lesson 1")  # 标题（是什么），项目名（为什么），传入文本（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），定帧器（为什么），锁定60FPS（怎么用）

# 变量定义：使用列表存储气泡坐标
qipao_list = []  # 气泡容器（是什么），存储所有气泡的[x, y]坐标（为什么），初始为空列表（怎么用）

yunxing = True  # 标志位（是什么），控制循环（为什么），布尔变量（怎么用）
while yunxing:  # 主循环（是什么），逻辑中枢（为什么），不断重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），轮询读取（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）

    # 逻辑更新：以 3% 的概率产生新气泡
    if random.random() < 0.03:  # 生成频率（是什么），控制气泡出现速度（为什么），random返回0-1小数（怎么用）
        # 气泡坐标随机分布在屏幕内（留出半径20的边距）
        qipao_list.append([random.randint(20, 380), random.randint(20, 380)])  # 追加气泡（是什么），增加新目标（为什么），append添加[x,y]列表（怎么用）

    chuangkou.fill((255, 255, 255))  # 刷白背景（是什么），清屏（为什么），RGB全白填充（怎么用）
    
    # 遍历列表绘制所有气泡
    for qp in qipao_list:  # 循环绘制（是什么），显示多个气泡（为什么），for in遍历坐标（怎么用）
        # 画空心圆气泡
        pygame.draw.circle(chuangkou, (0, 150, 255), qp, 20, 2)  # 绘图（是什么），蓝色空心圆（为什么），参数含位置半径及边框宽度（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成这一帧（为什么），同步频率（怎么用）

pygame.quit()  # 退出（是什么），清理内存（为什么），程序结束（怎么用）
