# 太空射击_第2节课_自由移动与敌机现身.py
# 学习目标：掌握键盘长按检测实现流畅位移，并学习随机生成单个下落的敌机

import pygame, random  # 导入库（是什么），驱动逻辑与随机（为什么），组合导入（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 600))  # 窗口（是什么），竖屏舞台（为什么），元组参数（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），控制频率（为什么），锁定60FPS（怎么用）

feichuan = [200, 500]  # 飞船坐标（是什么），初始位置（为什么），变量初始化（怎么用）
# 新增变量：敌人的随机坐标与速度
diren = [random.randint(20, 380), -20]  # 敌人坐标（是什么），屏幕外随机出现（为什么），[x,y]列表（怎么用）
diren_sudu = 3  # 下落速度（是什么），控制运动节奏（为什么），每帧增加的像素（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理逻辑（为什么），不断重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），轮询读取（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）

    # 新增代码：长按检测控制位移
    jp = pygame.key.get_pressed()  # 读按键（是什么），实现多键并发（为什么），返回布尔列表（怎么用）
    if jp[pygame.K_LEFT] and feichuan[0] > 20: feichuan[0] -= 5  # 左移（是什么），x减小且限位（为什么），变量更新（怎么用）
    if jp[pygame.K_RIGHT] and feichuan[0] < 380: feichuan[0] += 5  # 右移（是什么），x增加且限位（为什么），变量更新（怎么用）

    # 新增代码：敌人下落逻辑
    diren[1] += diren_sudu  # 垂直下落（是什么），实现移动（为什么），y坐标累加（怎么用）
    if diren[1] > 600: diren[1], diren[0] = -20, random.randint(20, 380)  # 越界重置（是什么），循环挑战（为什么），重新设坐标（怎么用）

    chuangkou.fill((10, 10, 30))  # 刷深蓝背景（是什么），清除旧像（为什么），RGB填充（怎么用）
    dianji = [(feichuan[0], feichuan[1]-20), (feichuan[0]-15, feichuan[1]+15), (feichuan[0]+15, feichuan[1]+15)]  # 计算顶点（是什么），跟随位置（为什么），定义三角形（怎么用）
    pygame.draw.polygon(chuangkou, (0, 200, 255), dianji)  # 画飞船（是什么），蓝色物体（为什么），绘制多边形（怎么用）
    pygame.draw.circle(chuangkou, (255, 50, 50), diren, 20)  # 画敌人（是什么），红色圆球（为什么），绘制圆形（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新并定帧（是什么），完成一帧（为什么），同步频率（怎么用）

pygame.quit()  # 退出（是什么），资源清理（为什么），程序末尾（怎么用）
