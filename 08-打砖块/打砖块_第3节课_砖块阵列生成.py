# 打砖块_第3节课_砖块阵列生成.py
# 学习目标：学习使用嵌套循环(Nested Loops)创建和排列砖块列表，掌握批量绘制物体的技巧

import pygame, random  # 导入库（是什么），核心驱动（为什么），必选（怎么用）

pygame.init()  # 初始化（是什么），准备引擎（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），400x400（为什么），传入元组（怎么用）
pygame.display.set_caption("Breakout - Lesson 3")  # 标题（是什么），标识第3课（为什么），传入文本（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），控制频率（为什么），60FPS（怎么用）

qiu_weizhi, qiu_sudu = [200, 200], [random.choice([-3, 3]), random.choice([-3, 3])]  # 球属性（是什么），初态定义（为什么），多重赋值（怎么用）
dangban_x = 200  # 挡板x（是什么），初始中点（为什么），变量初始化（怎么用）

# 新增变量：砖块列表与阵列生成
zhuan_list = []  # 砖块容器（是什么），存储数据（为什么），空列表初始化（怎么用）
# 新增代码：使用嵌套循环生成 4行 x 5列 的砖块
for hang in range(4):  # 遍历行（是什么），生成4层（为什么），循环4次（怎么用）
    for lie in range(5):  # 遍历列（是什么），每层5个（为什么），循环5次（怎么用）
        zhuan_list.append([lie*70+30, hang*30+40, 60, 20])  # 存入列表（是什么），记录[x,y,宽,高]（为什么），append方法（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），逻辑中心（为什么），不断重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），动作捕捉（为什么），轮询读取（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）

    dangban_x = max(50, min(350, pygame.mouse.get_pos()[0]))  # 挡板跟随（是什么），限制移动（为什么），组合调用（怎么用）
    qiu_weizhi[0] += qiu_sudu[0]; qiu_weizhi[1] += qiu_sudu[1]  # 移动球（是什么），更新坐标（为什么），累加速度（怎么用）

    if qiu_weizhi[0] <= 10 or qiu_weizhi[0] >= 390: qiu_sudu[0] *= -1  # 墙壁反弹（是什么），防止出界（为什么），取反速度（怎么用）
    if qiu_weizhi[1] <= 10: qiu_sudu[1] *= -1  # 顶部反弹（是什么），判断y上限（为什么），取反速度（怎么用）
    if qiu_weizhi[1] >= 360 and dangban_x-50 <= qiu_weizhi[0] <= dangban_x+50: qiu_weizhi[1], qiu_sudu[1] = 359, qiu_sudu[1] * -1 # 接球判定（是什么），反弹动作（为什么），同步赋值（怎么用）
    if qiu_weizhi[1] >= 390: yunxing = False  # 落地失败（是什么），逻辑终结（为什么），标志位更新（怎么用）

    chuangkou.fill((0, 0, 0))  # 刷黑（是什么），清屏（为什么），fill填充（怎么用）
    pygame.draw.circle(chuangkou, (255, 255, 255), qiu_weizhi, 10)  # 画球（是什么），显示圆（为什么），传入坐标（怎么用）
    pygame.draw.rect(chuangkou, (0, 255, 0), (dangban_x-50, 370, 100, 10))  # 画板（是什么），绿色条（为什么），绘制矩形（怎么用）
    
    # 新增代码：循环绘制所有砖块
    for zhuan in zhuan_list: pygame.draw.rect(chuangkou, (255, 0, 0), zhuan)  # 画砖（是什么），渲染阵列（为什么），遍历调用draw（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成这一帧（为什么），同步节奏（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序结束（怎么用）
