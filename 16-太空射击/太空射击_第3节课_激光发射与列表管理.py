# 太空射击_第3节课_激光发射与列表管理.py
# 学习目标：掌握列表(List)对多个物体的管理，实现子弹的连发、移动与自动销毁

import pygame, random  # 导入库（是什么），驱动核心（为什么），必备环境（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 600))  # 窗口（是什么），竖屏舞台（为什么），元组参数（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），控制节奏（为什么），锁定60FPS（怎么用）

feichuan, diren = [200, 500], [random.randint(20, 380), -20]  # 初始化坐标（是什么），定义初态（为什么），变量赋值（怎么用）
# 新增变量：子弹列表
zidan_list = []  # 子弹容器（是什么），管理多发火力（为什么），空列表初始化（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），逻辑中枢（为什么），重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），轮询读取（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）
        # 新增代码：按下空格生成子弹
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE: zidan_list.append([feichuan[0], feichuan[1]-20])  # 发射（是什么），生成弹药（为什么），追加坐标到列表（怎么用）

    jp = pygame.key.get_pressed()  # 读键盘（是什么），控制移动（为什么），长按检测（怎么用）
    if jp[pygame.K_LEFT] and feichuan[0] > 20: feichuan[0] -= 5  # 左移（是什么），x减小（为什么），变量更新（怎么用）
    if jp[pygame.K_RIGHT] and feichuan[0] < 380: feichuan[0] += 5  # 右移（是什么），x增加（为什么），变量更新（怎么用）

    # 新增代码：倒序遍历子弹列表，实现统一移动与出界清理
    for i in range(len(zidan_list)-1, -1, -1):  # 倒序循环（是什么），安全删除元素（为什么），从后往前遍历（怎么用）
        zidan_list[i][1] -= 8  # 向上飞（是什么），垂直位移（为什么），更新y值（怎么用）
        if zidan_list[i][1] < 0: zidan_list.pop(i)  # 出界销毁（是什么），释放内存（为什么），pop弹出项（怎么用）

    diren[1] += 3; (diren[1] > 600) and (diren.__setitem__(1, -20), diren.__setitem__(0, random.randint(20, 380))) # 敌人移动（是什么），循环逻辑（为什么），紧凑写法（怎么用）
    chuangkou.fill((10, 10, 30))  # 刷背景（是什么），清屏（为什么），填充（怎么用）
    pygame.draw.polygon(chuangkou, (0, 200, 255), [(feichuan[0], feichuan[1]-20), (feichuan[0]-15, feichuan[1]+15), (feichuan[0]+15, feichuan[1]+15)])  # 画船（是什么），蓝色三角形（为什么），polygon绘图（怎么用）
    pygame.draw.circle(chuangkou, (255, 50, 50), diren, 20)  # 画敌人（是什么），红色（为什么），circle绘图（怎么用）
    # 新增代码：循环绘制列表中的所有子弹
    for zd in zidan_list: pygame.draw.circle(chuangkou, (255, 255, 0), zd, 5)  # 画弹幕（是什么），黄色点（为什么），循环遍历（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成一帧（为什么），同步频率（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序结束（怎么用）
