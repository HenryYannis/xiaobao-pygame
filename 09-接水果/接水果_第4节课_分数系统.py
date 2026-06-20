# 接水果_第4节课_分数系统.py
# 学习目标：掌握使用字体库显示实时分数，并为游戏加入基础的得分反馈机制

import pygame, random  # 导入库（是什么），逻辑与随机（为什么），组合导入（怎么用）

pygame.init()  # 初始化（是什么），硬件预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 600))  # 窗口（是什么），舞台（为什么），元组参数（怎么用）
# 新增变量：分数与字体对象
shizhong, ziti, defen = pygame.time.Clock(), pygame.font.SysFont(None, 36), 0  # 初始化组件（是什么），分数设为0（为什么），一次性定义（怎么用）

lanzi_x, lanzi_y, shuiguo_list = 160, 550, []  # 变量组初始化（是什么），位置与容器（为什么），变量赋值（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理逻辑（为什么），不断重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），动作捕捉（为什么），轮询读取（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）

    jp = pygame.key.get_pressed()  # 读键盘
    if jp[pygame.K_LEFT] and lanzi_x > 0: lanzi_x -= 5
    if jp[pygame.K_RIGHT] and lanzi_x < 320: lanzi_x += 5

    if random.random() < 0.02: shuiguo_list.append([random.randint(20, 380), -20])  # 生成（是什么），控制频率（为什么），追加坐标（怎么用）

    for i in range(len(shuiguo_list)-1, -1, -1):  # 遍历水果（是什么），更新判定（为什么），倒序循环（怎么用）
        shuiguo_list[i][1] += 4  # 下落（是什么），垂直位移（为什么），y值累加（怎么用）
        if shuiguo_list[i][1]+15 >= lanzi_y and lanzi_x <= shuiguo_list[i][0] <= lanzi_x+80:  # 接住判定（是什么），碰撞反馈（为什么），pop项并加分（怎么用）
            shuiguo_list.pop(i); defen += 10  # 新增逻辑：接住加分（是什么），记录成绩（为什么），变量累加（怎么用）
        elif shuiguo_list[i][1] > 600: shuiguo_list.pop(i)  # 落地清理（是什么），释放资源（为什么），索引删除（怎么用）

    chuangkou.fill((135, 206, 235))  # 刷背景（是什么），清屏（为什么），填充（怎么用）
    pygame.draw.rect(chuangkou, (139, 69, 19), (lanzi_x, lanzi_y, 80, 20))  # 画篮子（是什么），矩形（为什么），绘制（怎么用）
    for sg in shuiguo_list: pygame.draw.circle(chuangkou, (255, 0, 0), sg, 15)  # 画水果群（是什么），红色圆（为什么），循环（怎么用）
    # 新增代码：显示分数
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10))  # 显分（是什么），看板反馈（为什么），渲染贴图（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成一帧（为什么），同步频率（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序结束（怎么用）
