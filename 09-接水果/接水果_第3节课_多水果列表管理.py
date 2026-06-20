# 接水果_第3节课_多水果列表管理.py
# 学习目标：掌握使用列表(List)管理多个随机生成的物体，并实现动态生成与销毁逻辑

import pygame, random  # 导入库（是什么），逻辑与随机（为什么），组合导入（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 600))  # 窗口（是什么），舞台（为什么），元组参数（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），定帧器（为什么），锁定60FPS（怎么用）

lanzi_x, lanzi_y = 160, 550  # 篮子坐标（是什么），位置数据（为什么），变量初始化（怎么用）
# 新增变量：水果容器列表
shuiguo_list = []  # 水果列表（是什么），存储所有水果坐标（为什么），空列表初始化（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理逻辑（为什么），重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），判断退出（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）

    jp = pygame.key.get_pressed()  # 读键盘控制篮子
    if jp[pygame.K_LEFT] and lanzi_x > 0: lanzi_x -= 5
    if jp[pygame.K_RIGHT] and lanzi_x < 320: lanzi_x += 5

    # 新增代码：随机生成水果并加入列表
    if random.random() < 0.02: shuiguo_list.append([random.randint(20, 380), -20])  # 生成（是什么），控制频率（为什么），追加坐标项（怎么用）

    # 新增逻辑：遍历列表更新位置与判定
    for i in range(len(shuiguo_list)-1, -1, -1):  # 倒序遍历（是什么），安全删除元素（为什么），从后往前（怎么用）
        shuiguo_list[i][1] += 4  # 下落（是什么），垂直位移（为什么），更新y值（怎么用）
        if shuiguo_list[i][1]+15 >= lanzi_y and lanzi_x <= shuiguo_list[i][0] <= lanzi_x+80:  # 接住（是什么），范围判断（为什么），删除该项（怎么用）
            shuiguo_list.pop(i)  # 移除水果（是什么），消失效果（为什么），pop操作（怎么用）
        elif shuiguo_list[i][1] > 600: shuiguo_list.pop(i)  # 落地移除（是什么），清理资源（为什么），索引删除（怎么用）

    chuangkou.fill((135, 206, 235))  # 刷天蓝（是什么），清屏（为什么），RGB填充（怎么用）
    pygame.draw.rect(chuangkou, (139, 69, 19), (lanzi_x, lanzi_y, 80, 20))  # 画篮子（是什么），矩形（为什么），绘制（怎么用）
    # 新增代码：循环绘制所有水果
    for sg in shuiguo_list: pygame.draw.circle(chuangkou, (255, 0, 0), sg, 15)  # 画水果群（是什么），显示多个（为什么），循环调用（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新并定帧（是什么），同步频率（为什么），锁定60FPS（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序末尾（怎么用）
