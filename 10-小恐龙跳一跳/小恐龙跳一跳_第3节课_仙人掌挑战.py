# 小恐龙跳一跳_第3节课_仙人掌挑战.py
# 学习目标：在第2节课基础上，加入滚动的仙人掌障碍与碰撞判定，完成一个完整的动作小游戏

import pygame, random  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((600, 300))
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 36)

# 状态变量：恐龙位置、速度、障碍物矩形、得分
ky, sy, defen = 200, 0, 0 # 缩写变量名以节省行数
# 新增变量：障碍物，使用 Rect 对象方便判定碰撞
zhang_rect = pygame.Rect(600, 210, 30, 40) # 仙人掌（是什么），移动的障碍（为什么），x设在屏外(600)（怎么用）

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); exit()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE and ky >= 200: sy = -14

    # 物理更新
    sy += 0.8; ky += sy
    if ky > 200: ky, sy = 200, 0

    # 新增代码：障碍物滚动逻辑
    zhang_rect.x -= 8 # 向左平移（是什么），模拟奔跑感（为什么），坐标自减（怎么用）
    if zhang_rect.right < 0: # 出界重置（是什么），循环挑战（为什么），判断右边缘小于0（怎么用）
        zhang_rect.x, defen = 600, defen + 1 # 重生并加分（是什么），下一关（为什么），重设x并累加变量（怎么用）

    # 新增代码：碰撞判定。使用 colliderect 检测两个矩形是否重叠
    long_rect = pygame.Rect(100, ky, 40, 50) # 实时恐龙包围盒
    if long_rect.colliderect(zhang_rect): # 撞到了（是什么），判定失败（为什么），调用Rect内置方法（怎么用）
        defen = 0; zhang_rect.x = 600 # 惩罚重置（是什么），游戏重启（为什么），变量复原（怎么用）

    chuangkou.fill((255, 255, 255))
    pygame.draw.rect(chuangkou, (200, 200, 200), (0, 250, 600, 50)) # 地面
    pygame.draw.rect(chuangkou, (67, 160, 72), long_rect) # 画龙
    pygame.draw.rect(chuangkou, (255, 50, 50), zhang_rect) # 画刺

    chuangkou.blit(ziti.render(f"Score: {defen}", True, (0,0,0)), (10, 10))
    pygame.display.flip(); shizhong.tick(60)
