# 打砖块_第5节课_完整游戏与结局.py
# 学习目标：掌握多行变色逻辑、设计完整的胜利与失败结算画面，完成整款游戏的开发流程

import pygame, random  # 导入库（是什么），驱动核心与随机（为什么），必备（怎么用）

pygame.init()  # 初始化（是什么），引擎预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），400像素舞台（为什么），元组参数（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)  # 初始化组件（是什么），时钟与字体（为什么），一次性定义（怎么用）

# 变量初始化
qiu, sudu, defen, shengli = [200, 200], [random.choice([-3, 3]), random.choice([-3, 3])], 0, False # 属性汇总（是什么），初态定义（为什么），多重赋值（怎么用）
# 新增变量：颜色列表，用于区分不同行砖块
yanse_list = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0)]  # 颜色库（是什么），红橙黄绿（为什么），存入RGB元组（怎么用）
zhuan_list = []  # 容器（是什么），空列表（为什么），列表初始化（怎么用）
for h in range(4):  # 生成砖块
    for l in range(5): zhuan_list.append([l*70+30, h*30+40, 60, 20, h])  # 存入列表（是什么），最后位存行号（为什么），追加五个属性项（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），处理逻辑（为什么），不断重复执行（怎么用）
    for ev in pygame.event.get():  # 监听事件
        if ev.type == pygame.QUIT: pygame.quit(); exit() # 强力退出（是什么），彻底关闭（为什么），退出系统（怎么用）

    dangban_x = max(50, min(350, pygame.mouse.get_pos()[0]))  # 挡板（是什么），鼠标跟随（为什么），限位处理（怎么用）
    qiu[0]+=sudu[0]; qiu[1]+=sudu[1]  # 移动球（是什么），更新位移（为什么），累加坐标（怎么用）

    if qiu[0]<=10 or qiu[0]>=390: sudu[0]*=-1  # 墙壁（是什么），反弹动作（为什么），取反速度（怎么用）
    if qiu[1]<=10: sudu[1]*=-1  # 顶（是什么），反弹动作（为什么），取反速度（怎么用）
    if qiu[1]>=360 and dangban_x-50<=qiu[0]<=dangban_x+50: qiu[1], sudu[1] = 359, sudu[1]*-1 # 板（是什么），接球（为什么），修正并反弹（怎么用）

    for i, z in enumerate(zhuan_list):  # 砖块检测
        if z[0]<=qiu[0]<=z[0]+z[2] and z[1]<=qiu[1]<=z[1]+z[3]: # 击中判断（是什么），判定碰撞（为什么），范围判断（怎么用）
            zhuan_list.pop(i); sudu[1]*=-1; defen+=10; break  # 击碎处理（是什么），删除加分（为什么），中断当前循环（怎么用）

    if len(zhuan_list)==0: shengli, yunxing = True, False  # 赢了（是什么），通关判定（为什么），状态位置True（怎么用）
    if qiu[1]>=390: shengli, yunxing = False, False  # 输了（是什么），触底判定（为什么），状态位置False（怎么用）

    chuangkou.fill((0, 0, 0))  # 刷黑（是什么），清屏（为什么），填充（怎么用）
    pygame.draw.circle(chuangkou, (255, 255, 255), qiu, 10)  # 画球（是什么），白色圆（为什么），绘制（怎么用）
    pygame.draw.rect(chuangkou, (0, 255, 0), (dangban_x-50, 370, 100, 10))  # 画板（是什么），绿板（为什么），绘制（怎么用）
    for z in zhuan_list: pygame.draw.rect(chuangkou, yanse_list[z[4]], z[:4]) # 变色画砖（是什么），依行号取色（为什么），绘制切片范围项（怎么用）
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (255, 255, 255)), (10, 10)) # 显分（是什么），成果看板（为什么），文字贴图（怎么用）
    pygame.display.flip(); shizhong.tick(60)  # 刷新定帧

# 新增代码：游戏结局结算画面
chuangkou.fill((0, 0, 0))  # 再次刷黑（是什么），显示最终画面（为什么），清空背景（怎么用）
wenzi, yanse = ("YOU WIN!", (0, 255, 0)) if shengli else ("GAME OVER", (255, 0, 0)) # 选择结局（是什么），根据结果切换文案颜色（为什么），三元运算（怎么用）
chuangkou.blit(ziti.render(wenzi, True, yanse), (130, 180)) # 写结局（是什么），渲染显示（为什么），调用blit（怎么用）
chuangkou.blit(ziti.render(f"Final Score: {defen}", True, (255, 255, 255)), (120, 220)) # 写分（是什么），展示成绩（为什么），位置偏移（怎么用）
pygame.display.flip(); pygame.time.wait(3000); pygame.quit() # 停顿并退出（是什么），留时间观看（为什么），组合调用（怎么用）
