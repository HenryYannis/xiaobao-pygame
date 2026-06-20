# 井字棋对战_第3节课_胜负判定.py
# 学习目标：在第2节课基础上，加入完整的胜负判定逻辑，并实现获胜提示与游戏重置功能

import pygame # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((300, 300))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 40)

shuju, wanjia, shengli = [0]*9, 1, 0 # 状态量：棋盘、轮换、胜者(0无,1X,2O)

# 新增代码：检查胜负的函数
def jiancha_shengli():
    xian = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] # 8种获胜线（是什么），获胜标准（为什么），索引组合（怎么用）
    for a,b,c in xian:
        if shuju[a] != 0 and shuju[a] == shuju[b] == shuju[c]: return shuju[a] # 胜出（是什么），判定连珠（为什么），比对三位值（怎么用）
    return 0

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        if ev.type == pygame.MOUSEBUTTONDOWN and shengli == 0:
            mx, my = pygame.mouse.get_pos()
            idx = (my//100)*3 + (mx//100)
            if shuju[idx] == 0:
                shuju[idx] = wanjia
                shengli = jiancha_shengli() # 判定（是什么），实时跟进局势（为什么），调用函数（怎么用）
                wanjia = 2 if wanjia == 1 else 1

    chuangkou.fill((255, 255, 255))
    for i in range(1, 3):
        pygame.draw.line(chuangkou, (0, 0, 0), (i*100, 0), (i*100, 300), 2)
        pygame.draw.line(chuangkou, (0, 0, 0), (0, i*100), (300, i*100), 2)
    
    for i, z in enumerate(shuju):
        x, y = (i%3)*100+50, (i//3)*100+50
        if z == 1: pygame.draw.circle(chuangkou, (255, 0, 0), (x, y), 30, 3)
        if z == 2: pygame.draw.rect(chuangkou, (0, 0, 255), (x-25, y-25, 50, 50), 3)

    # 新增代码：绘制胜利文字
    if shengli != 0:
        msg = f"Player {'X' if shengli==1 else 'O'} Wins!" # 动态文案
        chuangkou.blit(ziti.render(msg, True, (0,150,0)), (40, 130)) # 显胜（是什么），终局提示（为什么），贴图显示（怎么用）

    pygame.display.flip(); shizhong.tick(60)
