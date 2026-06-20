# 水果切切乐_第3节课_连击与挑战.py
# 学习目标：掌握分数累加与生命损失逻辑，完成具有失败结局的完整切割挑战游戏

import pygame, random, math  # 导入库
pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 30)

# 新增变量：分数与生命值
sg_list, guiji, defen, shengming = [], [], 0, 3  # 状态变量组（是什么），包含成绩与血量（为什么），变量初始化（怎么用）

while shengming > 0:  # 只要活着就循环（是什么），游戏主进程（为什么），控制运行范围（怎么用）
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()

    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]: guiji.append((mx, my))
    if len(guiji) > 10: guiji.pop(0)
    if not pygame.mouse.get_pressed()[0]: guiji.clear()

    if random.random() < 0.03: sg_list.append([random.randint(50, 350), 410, random.uniform(-2, 2), -9])

    for i in range(len(sg_list)-1, -1, -1):
        s = sg_list[i]; s[0]+=s[2]; s[1]+=s[3]; s[3]+=0.25
        for p in guiji:
            if math.hypot(p[0]-s[0], p[1]-s[1]) < 20: 
                sg_list.pop(i); defen+=10; break # 切中加分（是什么），成果回馈（为什么），变量累加（怎么用）
        if i < len(sg_list) and s[1] > 420: 
            sg_list.pop(i); shengming-=1 # 漏切扣血（是什么），增加惩罚（为什么），变量递减（怎么用）

    chuangkou.fill((20, 20, 20))
    for s in sg_list: pygame.draw.circle(chuangkou, (255, 150, 0), (int(s[0]), int(s[1])), 20)
    if len(guiji)>1: pygame.draw.lines(chuangkou, (255, 255, 255), False, guiji, 2)
    # 新增代码：显示 UI
    chuangkou.blit(ziti.render(f"Score: {defen}  HP: {shengming}", True, (255, 255, 255)), (10, 10)) # 显状态（是什么），展示成绩（为什么），文字贴图（怎么用）

    pygame.display.flip(); shizhong.tick(60)

# 新增代码：游戏结束结算
chuangkou.fill((0, 0, 0)); chuangkou.blit(ziti.render(f"GAME OVER - Score: {defen}", True, (255, 0, 0)), (80, 180))
pygame.display.flip(); pygame.time.wait(2000); pygame.quit() # 定格退出（是什么），留时间看分（为什么），组合调用（怎么用）
