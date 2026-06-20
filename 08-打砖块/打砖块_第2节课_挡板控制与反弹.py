# 打砖块_第2节课_挡板控制与反弹.py
# 学习目标：掌握鼠标控制挡板移动、范围限位逻辑，以及球与挡板的碰撞反弹算法

import pygame, random  # 导入库（是什么），支持核心逻辑与随机（为什么），组合导入（怎么用）

pygame.init()  # 初始化环境（是什么），引擎预备（为什么），开头调用一次（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 创建窗口（是什么），400x400舞台（为什么），元组坐标（怎么用）
pygame.display.set_caption("Breakout - Lesson 2")  # 标题（是什么），标识当前进度（为什么），传入文本（怎么用）
shizhong = pygame.time.Clock()  # 时钟（是什么），让运动平滑（为什么），锁定60FPS（怎么用）

qiu_weizhi = [200, 200]  # 球位置（是什么），记录坐标（为什么），列表存储[x,y]（怎么用）
qiu_sudu = [random.choice([-3, 3]), random.choice([-3, 3])]  # 球速度（是什么），运动轨迹（为什么），增加位移（怎么用）
# 新增变量：挡板中心点
dangban_x = 200  # 挡板x坐标（是什么），控制水平位置（为什么），变量初始化（怎么用）

yunxing = True  # 开关（是什么），逻辑条件（为什么），控制循环（怎么用）
while yunxing:  # 主循环（是什么），处理每一帧（为什么），不断重复执行（怎么用）
    for shijian in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），判断退出（怎么用）
        if shijian.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）

    # 新增代码：鼠标跟随与限位
    dangban_x = max(50, min(350, pygame.mouse.get_pos()[0]))  # 读鼠标并限位（是什么），控制挡板（为什么），嵌套函数处理（怎么用）

    qiu_weizhi[0] += qiu_sudu[0]; qiu_weizhi[1] += qiu_sudu[1]  # 更新球（是什么），实现位移（为什么），累加坐标（怎么用）
    if qiu_weizhi[0] <= 10 or qiu_weizhi[0] >= 390: qiu_sudu[0] *= -1  # 左右反弹（是什么），防止出界（为什么），速度取反（怎么用）
    if qiu_weizhi[1] <= 10: qiu_sudu[1] *= -1  # 顶部反弹（是什么），判断y上限（为什么），y速度取反（怎么用）

    # 新增代码：挡板碰撞检测
    if qiu_weizhi[1] >= 360 and dangban_x-50 <= qiu_weizhi[0] <= dangban_x+50:  # 碰撞判定（是什么），接住球（为什么），区间判定（怎么用）
        qiu_weizhi[1], qiu_sudu[1] = 359, qiu_sudu[1] * -1  # 修正并反弹（是什么），防止粘连（为什么），同步赋值（怎么用）
    
    # 新增代码：失败判定
    if qiu_weizhi[1] >= 390: yunxing = False  # 漏球失败（是什么），游戏结束（为什么），判断落底（怎么用）

    chuangkou.fill((0, 0, 0))  # 刷黑（是什么），清除旧帧（为什么），填充（怎么用）
    pygame.draw.circle(chuangkou, (255, 255, 255), qiu_weizhi, 10)  # 画球（是什么），白色圆（为什么），指定位置（怎么用）
    pygame.draw.rect(chuangkou, (0, 255, 0), (dangban_x - 50, 370, 100, 10))  # 画挡板（是什么），绿色矩形（为什么），传入矩形参数（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成一帧（为什么），同步频率（怎么用）

pygame.quit()  # 退出（是什么），资源清理（为什么），程序结束（怎么用）
