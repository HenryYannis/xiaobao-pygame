# 颜色匹配_第2节课_匹配判定.py
# 学习目标：在第1节课基础上，学习捕捉选项点击事件，并实现逻辑比对与题目自动刷新

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 300))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 40)

yanses = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255)]
def xin_timu():
    s1, s2 = random.sample(range(len(yanses)), 2)
    return s1, s2, random.choice([s1, s2])

opt1, opt2, daan = xin_timu()

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        
        # 新增代码：处理点击判定
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            # 新增逻辑：点击区域换算
            # 左方块: x(50-170), y(180-260)；右方块: x(230-350), y(180-260)
            xuanze = -1 # 初始未选
            if 180 <= my <= 260:
                if 50 <= mx <= 170: xuanze = opt1 # 点了左（是什么），记录选色索引（为什么），判断坐标（怎么用）
                elif 230 <= mx <= 350: xuanze = opt2 # 点了右（是什么），记录选色索引（为什么），判断坐标（怎么用）
            
            # 新增逻辑：比对正确性
            if xuanze == daan: # 答对了（是什么），刷新下一题（为什么），逻辑比对相等（怎么用）
                opt1, opt2, daan = xin_timu() # 换题（是什么），让游戏继续（为什么），再次调用生成函数（怎么用）

    chuangkou.fill((255, 255, 255))
    chuangkou.blit(ziti.render("Match this color:", True, (0,0,0)), (80, 20))
    pygame.draw.rect(chuangkou, yanses[daan], (150, 70, 100, 50))
    pygame.draw.rect(chuangkou, yanses[opt1], (50, 180, 120, 80))
    pygame.draw.rect(chuangkou, yanses[opt2], (230, 180, 120, 80))

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
