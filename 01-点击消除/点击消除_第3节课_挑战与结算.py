# 点击消除_第3节课_挑战与结算.py
# 学习目标：在第2节课基础上，加入分数系统与倒计时机制，完成一款具备完整游戏流程的作品

import pygame, random, math  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)

# 新增变量：得分与限制时间
defen = 0  # 分数（是什么），记录成绩（为什么），初始为0（怎么用）
daojishi = 10  # 时间限制（是什么），增加挑战紧迫感（为什么），设定为10秒（怎么用）

qipao_list = []
yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        if ev.type == pygame.MOUSEBUTTONDOWN and daojishi > 0:  # 点击判定：增加时间检查
            mx, my = pygame.mouse.get_pos()
            for i in range(len(qipao_list)-1, -1, -1):
                qx, qy = qipao_list[i]
                if math.hypot(mx - qx, my - qy) < 20:
                    qipao_list.pop(i)
                    # 新增代码：击中后加分
                    defen += 1  # 成绩累加（是什么），分数反馈（为什么），变量递增（怎么用）
                    break

    # 新增代码：计算剩余时间。get_ticks返回总毫秒数
    # 为了简化教学，此处暂不考虑复杂的重启逻辑。
    sheng_shijian = daojishi - pygame.time.get_ticks() // 1000  # 倒计时（是什么），计算当前剩余（为什么），上限减去运行秒数（怎么用）

    if sheng_shijian > 0:  # 只有时间未到才生成气泡
        if random.random() < 0.05: qipao_list.append([random.randint(20, 380), random.randint(20, 380)])
    else: qipao_list.clear(); sheng_shijian = 0  # 结束后清屏（是什么），定格画面（为什么），清空列表（怎么用）

    chuangkou.fill((255, 255, 255))
    for qp in qipao_list: pygame.draw.circle(chuangkou, (0, 150, 255), qp, 20, 2)

    # 新增代码：绘制分数与倒计时文字
    chuangkou.blit(ziti.render(f"Score: {defen}", True, (0, 0, 0)), (10, 10))  # 显分（是什么），成果反馈（为什么），贴图（怎么用）
    chuangkou.blit(ziti.render(f"Time: {sheng_shijian}s", True, (255, 0, 0)), (280, 10))  # 显秒（是什么），倒计时警告（为什么），红字显示（怎么用）

    if sheng_shijian <= 0:  # 结束后提示
        chuangkou.blit(ziti.render("TIME UP!", True, (255, 0, 0)), (140, 180)) # 结局（是什么），标识结束（为什么），贴图（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
