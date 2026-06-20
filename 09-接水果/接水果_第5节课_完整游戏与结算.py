# 接水果_第5节课_完整游戏与结算.py
# 学习目标：掌握游戏失败判定的实现，并设计完整的游戏结束结算画面

import pygame, random  # 导入库（是什么），逻辑支持（为什么），必备（怎么用）

pygame.init()  # 初始化（是什么），引擎预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 600))  # 窗口（是什么），舞台规格（为什么），元组参数（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)  # 初始化组件（是什么），时钟与字体（为什么），一次性定义（怎么用）

# 新增变量：游戏结束标志
defen, jieshu = 0, False  # 状态变量（是什么），包含分数与结束标志（为什么），多重初始化（怎么用）
lanzi_x, lanzi_y, shuiguo_list = 160, 550, []  # 位置数据（是什么），初态定义（为什么），变量赋值（怎么用）

yunxing = True  # 运行开关（是什么），控制循环（为什么），布尔逻辑（怎么用）
while yunxing:  # 主循环（是什么），中枢（为什么），不断重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），动作捕捉（为什么），轮询读取（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出（是什么），点击关闭（为什么），改状态位（怎么用）

    if not jieshu:  # 新增逻辑：只有未结束时才执行运行逻辑
        jp = pygame.key.get_pressed()  # 读键盘控制移动
        if jp[pygame.K_LEFT] and lanzi_x > 0: lanzi_x -= 5
        if jp[pygame.K_RIGHT] and lanzi_x < 320: lanzi_x += 5

        if random.random() < 0.02: shuiguo_list.append([random.randint(20, 380), -20])  # 产生水果

        for i in range(len(shuiguo_list)-1, -1, -1):  # 遍历判定
            shuiguo_list[i][1] += 4  # 下落（是什么），垂直位移（为什么），y坐标更新（怎么用）
            if shuiguo_list[i][1]+15 >= lanzi_y and lanzi_x <= shuiguo_list[i][0] <= lanzi_x+80:  # 接住（是什么），范围判断（为什么），删除并加分（怎么用）
                shuiguo_list.pop(i); defen += 10
            elif shuiguo_list[i][1] > 600:  # 新增逻辑：漏接判定为失败
                jieshu = True  # 游戏结束（是什么），标志位设为True（为什么），触发结算状态（怎么用）

    chuangkou.fill((135, 206, 235))  # 刷背景（是什么），清屏（为什么），填充（怎么用）
    pygame.draw.rect(chuangkou, (139, 69, 19), (lanzi_x, lanzi_y, 80, 20))  # 画板（是什么），棕色（为什么），绘制（怎么用）
    for sg in shuiguo_list: pygame.draw.circle(chuangkou, (255, 0, 0), sg, 15)  # 画水果（是什么），红圆（为什么），循环（怎么用）
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10)) # 显分（是什么），看板反馈（为什么），渲染贴图（怎么用）

    # 新增代码：如果结束，显示结算文案
    if jieshu: chuangkou.blit(ziti.render("GAME OVER", True, (255, 0, 0)), (130, 280))  # 写结局（是什么），红色醒目（为什么），blit贴图（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新并定帧（是什么），完成一帧（为什么），同步频率（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序结束（怎么用）
