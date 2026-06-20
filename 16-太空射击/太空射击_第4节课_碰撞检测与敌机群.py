# 太空射击_第4节课_碰撞检测与敌机群.py
# 学习目标：掌握数学公式(勾股定理)判定碰撞，并学习动态管理多个敌人的生成与销毁

import pygame, random, math  # 导入库（是什么），支持核心、随机与数学（为什么），必备环境（怎么用）

pygame.init()  # 初始化（是什么），引擎预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 600))  # 窗口（是什么），舞台（为什么），元组参数（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），控制FPS（为什么），锁定60FPS（怎么用）

feichuan, zidan_list = [200, 500], []  # 初始化船与子弹（是什么），变量准备（为什么），列表存储对象（怎么用）
# 新增变量：敌机列表
diren_list = []  # 敌人容器（是什么），管理多机群（为什么），空列表初始化（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理逻辑（为什么），不断重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），判断退出（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE: zidan_list.append([feichuan[0], feichuan[1]-20])  # 发射（是什么），生成子弹（为什么），追加坐标（怎么用）

    jp = pygame.key.get_pressed()  # 读键盘（是什么），位移控制（为什么），变量更新（怎么用）
    if jp[pygame.K_LEFT] and feichuan[0]>20: feichuan[0]-=5; 
    if jp[pygame.K_RIGHT] and feichuan[0]<380: feichuan[0]+=5; 

    # 新增代码：随机生成敌人机群
    if random.random() < 0.02: diren_list.append([random.randint(20, 380), -20])  # 产生敌人（是什么），控制出机率（为什么），追加到列表（怎么用）

    for i in range(len(zidan_list)-1, -1, -1):  # 遍历子弹（是什么），控制飞行（为什么），倒序循环（怎么用）
        zidan_list[i][1] -= 8  # 移动（是什么），向上飞行（为什么），y值更新（怎么用）
        # 新增代码：子弹击中敌人的碰撞检测
        for j in range(len(diren_list)-1, -1, -1):  # 嵌套敌人（是什么），双重检测（为什么），再次倒序（怎么用）
            if math.sqrt((zidan_list[i][0]-diren_list[j][0])**2 + (zidan_list[i][1]-diren_list[j][1])**2) < 25:  # 击中判断（是什么），距离公式（为什么），pop共同销毁（怎么用）
                zidan_list.pop(i); diren_list.pop(j); break  # 记录碰撞（是什么），消除物体（为什么），删除并中断（怎么用）

    for i in range(len(diren_list)-1, -1, -1):  # 遍历敌人（是什么），控制位移与自毁（为什么），倒序循环（怎么用）
        diren_list[i][1] += 3; (diren_list[i][1]>600) and diren_list.pop(i) # 敌人下落（是什么），出界清理（为什么），pop弹出（怎么用）

    chuangkou.fill((10, 10, 30))  # 刷深蓝（是什么），清屏（为什么），RGB填充（怎么用）
    pygame.draw.polygon(chuangkou, (0, 200, 255), [(feichuan[0], feichuan[1]-20), (feichuan[0]-15, feichuan[1]+15), (feichuan[0]+15, feichuan[1]+15)])  # 画船（是什么），蓝色飞机（为什么），绘图方法（怎么用）
    for dr in diren_list: pygame.draw.circle(chuangkou, (255, 50, 50), dr, 20)  # 画敌群（是什么），红色（为什么），循环绘制（怎么用）
    for zd in zidan_list: pygame.draw.circle(chuangkou, (255, 255, 0), zd, 5)  # 画弹幕（是什么），黄色（为什么），循环绘制（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新并定帧（是什么），完成一帧（为什么），同步频率（怎么用）

pygame.quit()  # 退出（是什么），清理内存（为什么），程序结束（怎么用）
