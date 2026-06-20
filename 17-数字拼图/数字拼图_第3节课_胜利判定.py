# 数字拼图_第3节课_胜利判定.py
# 学习目标：在第2节课基础上，加入拼图还原判定逻辑，完成一个完整的智力挑战游戏

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((300, 300))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 40)

# 初始数据：打乱的列表
shuzi_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]
random.shuffle(shuzi_list)
# 新增变量：胜利的目标状态
mubiao = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # 目标序列（是什么），正确的顺序（为什么），用于核对结果（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            idx, kong_idx = (my//100)*3 + (mx//100), shuzi_list.index(0)
            if abs(idx - kong_idx) in [1, 3]:
                shuzi_list[idx], shuzi_list[kong_idx] = shuzi_list[kong_idx], shuzi_list[idx]

    chuangkou.fill((255, 255, 255))
    for i in range(9):
        x, y = (i % 3) * 100, (i // 3) * 100
        if shuzi_list[i] != 0:
            pygame.draw.rect(chuangkou, (100, 255, 100) if shuzi_list == mubiao else (200, 200, 200), (x+5, y+5, 90, 90)) # 变色反馈
            chuangkou.blit(pygame.font.SysFont(None, 60).render(str(shuzi_list[i]), True, (0, 0, 0)), (x+35, y+25))

    # 新增代码：检查是否获胜
    if shuzi_list == mubiao:  # 成功判定（是什么），核对拼图是否还原（为什么），直接比对两个列表（怎么用）
        chuangkou.blit(ziti.render("YOU WIN!", True, (255, 0, 0)), (80, 130))  # 胜利提示（是什么），文字居中（为什么），渲染贴图（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
