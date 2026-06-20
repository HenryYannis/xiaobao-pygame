# 黄金矿工_第2节课_出钩与收钩.py
# 学习目标：在第1节课基础上，学习使用“状态机”管理钩子的不同行为（摆动、伸长、收回）

import pygame, math  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 400))
shizhong = pygame.time.Clock()

zhongxin = [200, 50]
changdu, jiaodu = 50, 0
# 新增变量：管理钩子状态。0:摆动, 1:下放, 2:收回
zhuangtai = 0  # 钩子状态（是什么），记录当前工作模式（为什么），整数0/1/2切换（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        # 新增代码：按下空格键尝试出钩
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE and zhuangtai == 0:  # 发射判定（是什么），触发动作（为什么），仅在摆动时有效（怎么用）
            zhuangtai = 1  # 切换到下放模式（是什么），开始伸长（为什么），变量修改为1（怎么用）

    # 逻辑更新：根据不同状态执行动作
    if zhuangtai == 0:  # 摆动模式
        jiaodu = math.sin(pygame.time.get_ticks() / 500) * 80
    elif zhuangtai == 1:  # 下放模式
        changdu += 5  # 伸长（是什么），向下探测（为什么），变量自增（怎么用）
        if changdu > 350: zhuangtai = 2  # 触底自动收回（是什么），边界保护（为什么），判断长度是否超限（怎么用）
    elif zhuangtai == 2:  # 收回模式
        changdu -= 5  # 缩短（是什么），拉回钩子（为什么），变量自减（怎么用）
        if changdu <= 50: zhuangtai = 0; changdu = 50  # 恢复摆动（是什么），重置循环（为什么），回到模式0（怎么用）

    hudu = math.radians(jiaodu + 90)
    m_x, m_y = zhongxin[0] + changdu * math.cos(hudu), zhongxin[1] + changdu * math.sin(hudu)

    chuangkou.fill((255, 255, 200))
    pygame.draw.line(chuangkou, (0, 0, 0), zhongxin, (m_x, m_y), 3)
    pygame.draw.circle(chuangkou, (100, 50, 0), zhongxin, 10)

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
