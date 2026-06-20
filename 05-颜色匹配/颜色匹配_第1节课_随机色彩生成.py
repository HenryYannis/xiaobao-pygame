# 颜色匹配_第1节课_随机色彩生成.py
# 学习目标：掌握如何从颜色列表中随机选取不重复元素，并搭建基础的选项界面

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((400, 300))  # 创建400宽300高窗口
pygame.display.set_caption("Color Match - Lesson 1")
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 40)

# 颜色库：存储可用的颜色元组
yanses = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255)] # 红绿蓝黄紫

# 逻辑函数：生成一轮新的题目
def xin_timu():
    # 随机选两个不同的颜色索引
    s1, s2 = random.sample(range(len(yanses)), 2)  # 抽样（是什么），选出不重复的色号（为什么），sample(范围, 数量)（怎么用）
    target = random.choice([s1, s2]) # 目标色（是什么），设定本轮的正确答案（为什么），从两个选项中随机定一个（怎么用）
    return s1, s2, target # 返回数据（是什么），传递给变量（为什么），函数返回值（怎么用）

opt1, opt2, daan = xin_timu() # 初始化第一题

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False

    chuangkou.fill((255, 255, 255)) # 刷白背景
    
    # 绘制题目：上方显示目标颜色
    chuangkou.blit(ziti.render("Match this color:", True, (0,0,0)), (80, 20)) # 文字提示
    pygame.draw.rect(chuangkou, yanses[daan], (150, 70, 100, 50)) # 目标色块（是什么），视觉指引（为什么），使用daan索引（怎么用）
    
    # 绘制选项：下方两个方块
    pygame.draw.rect(chuangkou, yanses[opt1], (50, 180, 120, 80)) # 选项1（是什么），供玩家选择（为什么），位置偏左（怎么用）
    pygame.draw.rect(chuangkou, yanses[opt2], (230, 180, 120, 80)) # 选项2（是什么），供玩家选择（为什么），位置偏右（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
