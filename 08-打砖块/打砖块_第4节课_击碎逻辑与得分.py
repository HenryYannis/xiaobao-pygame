# 打砖块_第4节课_击碎逻辑与得分.py
# 学习目标：掌握小球与砖块的碰撞检测、列表中安全删除元素的技巧，以及显示实时分数

import pygame, random  # 导入库（是什么），驱动逻辑（为什么），必备环境（怎么用）

pygame.init()  # 初始化（是什么），引擎预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），400像素舞台（为什么），元组参数（怎么用）
# 新增变量：字体与得分
shizhong, ziti, defen = pygame.time.Clock(), pygame.font.SysFont(None, 36), 0  # 组件初始化（是什么），分数设为0（为什么），一次性定义（怎么用）

qiu_weizhi, qiu_sudu = [200, 200], [random.choice([-3, 3]), random.choice([-3, 3])]  # 球属性（是什么），初态（为什么），变量初始化（怎么用）
dangban_x, zhuan_list = 200, []  # 挡板与砖块容器（是什么），初始化（为什么），变量多重赋值（怎么用）
for hang in range(4):  # 生成砖块（是什么），嵌套循环（为什么），排列阵列（怎么用）
    for lie in range(5): zhuan_list.append([lie*70+30, hang*30+40, 60, 20])  # 存入列表（是什么），记录坐标（为什么），append添加（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理逻辑（为什么），不断重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），判断退出（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）

    dangban_x = max(50, min(350, pygame.mouse.get_pos()[0]))  # 鼠标跟随（是什么），限制移动（为什么），限位处理（怎么用）
    qiu_weizhi[0] += qiu_sudu[0]; qiu_weizhi[1] += qiu_sudu[1]  # 移动球（是什么），更新坐标（为什么），位移更新（怎么用）

    if qiu_weizhi[0] <= 10 or qiu_weizhi[0] >= 390: qiu_sudu[0] *= -1  # 墙壁反弹（是什么），x轴反向（为什么），取反速度（怎么用）
    if qiu_weizhi[1] <= 10: qiu_sudu[1] *= -1  # 顶反弹（是什么），y轴反向（为什么），取反速度（怎么用）
    if qiu_weizhi[1] >= 360 and dangban_x-50 <= qiu_weizhi[0] <= dangban_x+50: qiu_weizhi[1], qiu_sudu[1] = 359, qiu_sudu[1] * -1 # 接球反弹（是什么），修正粘连（为什么），同步赋值（怎么用）

    # 新增代码：小球击碎砖块的碰撞检测
    for i, zhuan in enumerate(zhuan_list):  # 遍历砖块（是什么），带索引循环（为什么），enumerate获取(序号,内容)（怎么用）
        if zhuan[0] <= qiu_weizhi[0] <= zhuan[0]+zhuan[2] and zhuan[1] <= qiu_weizhi[1] <= zhuan[1]+zhuan[3]: # 碰撞判断（是什么），击中砖块（为什么），范围判断（怎么用）
            zhuan_list.pop(i); qiu_sudu[1] *= -1; defen += 10; break  # 处理击碎（是什么），删除并反弹加分（为什么），执行复合动作（怎么用）

    if len(zhuan_list) == 0 or qiu_weizhi[1] >= 390: yunxing = False  # 胜负判定（是什么），全部消除或触底（为什么），改状态位（怎么用）

    chuangkou.fill((0, 0, 0))  # 刷黑（是什么），清屏（为什么），填充（怎么用）
    pygame.draw.circle(chuangkou, (255, 255, 255), qiu_weizhi, 10)  # 画球（是什么），白色圆（为什么），绘图（怎么用）
    pygame.draw.rect(chuangkou, (0, 255, 0), (dangban_x-50, 370, 100, 10))  # 画板（是什么），绿色板（为什么），绘制矩形（怎么用）
    for zhuan in zhuan_list: pygame.draw.rect(chuangkou, (255, 0, 0), zhuan)  # 画砖群（是什么），循环显示（为什么），遍历调用draw（怎么用）
    # 新增代码：显示得分
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10))  # 显分（是什么），分数看板（为什么），文字贴图（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新并定帧（是什么），完成一帧（为什么），同步节奏（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序结束（怎么用）
