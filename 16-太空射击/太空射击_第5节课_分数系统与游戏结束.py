# 太空射击_第5节课_分数系统与游戏结束.py
# 学习目标：掌握分数系统的设计、失败判定及游戏结算画面的展示，完成完整的游戏闭环

import pygame, random, math  # 导入库（是什么），驱动核心（为什么），必备（怎么用）

pygame.init()  # 初始化（是什么），引擎预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 600))  # 窗口（是什么），舞台（为什么），元组参数（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 30)  # 初始化组件（是什么），时钟与字体（为什么），一次性定义（怎么用）

# 新增变量：分数与游戏结束状态
feichuan, diren_list, zidan_list, defen, jieshu = [200, 500], [], [], 0, False  # 状态变量（是什么），包含分数与标志（为什么），多重初始化（怎么用）

yunxing = True  # 运行开关（是什么），管理循环（为什么），布尔变量（怎么用）
while yunxing:  # 主循环（是什么），中枢（为什么），不断重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），轮询读取（怎么用）
        if ev.type == pygame.QUIT: yunxing = False  # 退出判定（是什么），关窗口（为什么），改状态位（怎么用）
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE and not jieshu: zidan_list.append([feichuan[0], feichuan[1]-20])  # 发射（是什么），生成子弹（为什么），复合判断（怎么用）

    if not jieshu:  # 运行中逻辑
        jp = pygame.key.get_pressed()  # 读键盘（是什么），控制位移（为什么），更新x（怎么用）
        if jp[pygame.K_LEFT] and feichuan[0]>20: feichuan[0]-=5; 
        if jp[pygame.K_RIGHT] and feichuan[0]<380: feichuan[0]+=5; 

        if random.random() < 0.02: diren_list.append([random.randint(20, 380), -20])  # 产生敌人（是什么），随机出现（为什么），追加列表（怎么用）

        for i in range(len(diren_list)-1, -1, -1):  # 遍历敌人（是什么），处理碰撞（为什么），倒序循环（怎么用）
            diren_list[i][1] += 3; 
            # 新增逻辑：撞机检测
            if math.sqrt((feichuan[0]-diren_list[i][0])**2 + (feichuan[1]-diren_list[i][1])**2) < 35: jieshu = True  # 失败判定（是什么），撞机逻辑（为什么），标志位置True（怎么用）
            if diren_list[i][1] > 600: diren_list.pop(i)  # 出界清理（是什么），释放资源（为什么），超限即pop（怎么用）

        for i in range(len(zidan_list)-1, -1, -1):  # 遍历子弹（是什么），判定击中（为什么），倒序循环（怎么用）
            zidan_list[i][1] -= 8; 
            for j in range(len(diren_list)-1, -1, -1):  # 嵌套循环（是什么），检测击中（为什么），再次倒序（怎么用）
                if math.sqrt((zidan_list[i][0]-diren_list[j][0])**2 + (zidan_list[i][1]-diren_list[j][1])**2) < 25: 
                    zidan_list.pop(i); diren_list.pop(j); defen += 10; break  # 击中销毁并加分（是什么），记录成绩（为什么），执行复合动作（怎么用）

    chuangkou.fill((10, 10, 30))  # 刷深蓝（是什么），清屏（为什么），RGB填充（怎么用）
    pygame.draw.polygon(chuangkou, (0, 200, 255), [(feichuan[0], feichuan[1]-20), (feichuan[0]-15, feichuan[1]+15), (feichuan[0]+15, feichuan[1]+15)])  # 画船（是什么），三角形（为什么），polygon绘图（怎么用）
    for dr in diren_list: pygame.draw.circle(chuangkou, (255, 50, 50), dr, 20)  # 画敌群（是什么），红球（为什么），循环（怎么用）
    for zd in zidan_list: pygame.draw.circle(chuangkou, (255, 255, 0), zd, 5)  # 画弹幕（是什么），黄点（为什么），循环（怎么用）
    # 新增代码：显示分数看板
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10))  # 显分（是什么），反馈成果（为什么），文字贴图（怎么用）

    if jieshu:  # 结算画面（是什么），游戏结束提示（为什么），判断标志位（怎么用）
        chuangkou.fill((0, 0, 0)); chuangkou.blit(ziti.render(f"GAME OVER - Score: {defen}", True, (255, 0, 0)), (80, 280))  # 写结局（是什么），居中显示（为什么），显示红字（怎么用）

    pygame.display.flip(); shizhong.tick(60)  # 刷新与定帧（是什么），完成一帧（为什么），同步频率（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序结束（怎么用）
