# 小恐龙跳一跳_第2节课_重力跳跃.py
# 学习目标：在第1节课基础上，学习模拟重力加速度，并实现空格键触发的跳跃逻辑

import pygame  # 导入库

pygame.init()
chuangkou = pygame.display.set_mode((600, 300))
shizhong = pygame.time.Clock()

dimian_y = 250
konglong_x, konglong_y = 100, 200

# 新增变量：跳跃速度与重力
# 跳跃通过负速度向上（y轴减小），重力通过正加速度向下（y轴增加）
sudu_y = 0  # 垂直速度（是什么），控制上下位移快慢（为什么），变量初始化（怎么用）
zhongli = 0.8  # 重力常数（是什么），模拟自然下坠（为什么），每帧累加到速度上（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False
        # 新增代码：按下空格键且在地面上时跳起
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:  # 跳跃指令（是什么），触发动作（为什么），判断按键与高度（怎么用）
            if konglong_y >= dimian_y - 50: # 只有落地时才能跳（是什么），防止二段跳（为什么），判断y轴阈值（怎么用）
                sudu_y = -15  # 给予向上初速（是什么），实现瞬间腾空（为什么），负值代表向上（怎么用）

    # 新增代码：物理模拟逻辑
    sudu_y += zhongli  # 速度受重力影响（是什么），实现变速运动（为什么），速度累加加速度（怎么用）
    konglong_y += sudu_y  # 更新位置（是什么），执行位移（为什么），坐标累加速度（怎么用）
    
    # 落地碰撞检测：防止恐龙掉进地心
    if konglong_y > dimian_y - 50:  # 触地判定（是什么），限制下限（为什么），判断y坐标（怎么用）
        konglong_y = dimian_y - 50  # 修正位置（是什么），踩在地面上（为什么），强制赋值（怎么用）
        sudu_y = 0  # 垂直静止（是什么），落地后不再下坠（为什么），速度清零（怎么用）

    chuangkou.fill((255, 255, 255))
    pygame.draw.rect(chuangkou, (200, 200, 200), (0, dimian_y, 600, 50))
    pygame.draw.rect(chuangkou, (67, 160, 72), (konglong_x, konglong_y, 40, 50))

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
