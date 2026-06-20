# 黄金矿工_第1节课_钩子摆动.py
# 学习目标：掌握极坐标转换，利用正弦函数(math.sin)实现矿工钩子的自动左右摆动

import pygame, math  # 导入库（是什么），增加数学库处理三角函数（为什么），必备环境（怎么用）

pygame.init()  # 初始化
chuangkou = pygame.display.set_mode((400, 400))  # 窗口
pygame.display.set_caption("Gold Miner - Lesson 1")  # 标题
shizhong = pygame.time.Clock()  # 时钟

# 钩子基础参数：旋转中心、长度、角度、摆动速度
zhongxin = [200, 50]  # 旋转中心（是什么），钩子挂载点（为什么），设在屏幕顶部中央（怎么用）
changdu = 50  # 钩子长度（是什么），视觉线段长（为什么），固定为50（怎么用）
jiaodu = 0  # 当前角度（是什么），控制摆动位置（为什么），随时间变化（怎么用）

yunxing = True
while yunxing:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: yunxing = False

    # 逻辑更新：利用 sin 函数让角度在 -80 到 80 度之间往复摆动
    # pygame.time.get_ticks() 随时间递增，除以系数控制摆速
    jiaodu = math.sin(pygame.time.get_ticks() / 500) * 80  # 计算角度（是什么），周期性往复（为什么），将毫秒转为弧度比例（怎么用）
    
    # 极坐标转直角坐标：计算钩子末端的 (x, y)
    # math.radians 将度数转为 Python 需要的弧度
    hudu = math.radians(jiaodu + 90)  # 换算弧度（是什么），数学库要求（为什么），加上90度让0度垂直向下（怎么用）
    moudan_x = zhongxin[0] + changdu * math.cos(hudu)  # 终点x（是什么），钩子末端横坐标（为什么），x=r*cos(a)（怎么用）
    moudan_y = zhongxin[1] + changdu * math.sin(hudu)  # 终点y（是什么），钩子末端纵坐标（为什么），y=r*sin(a)（怎么用）

    chuangkou.fill((255, 255, 200))  # 刷浅黄色背景（是什么），代表沙地颜色（为什么），填充RGB（怎么用）
    
    # 绘制钩子：从中心点到末端画一条黑线
    pygame.draw.line(chuangkou, (0, 0, 0), zhongxin, (moudan_x, moudan_y), 3)  # 画线（是什么），视觉钩子（为什么），传入中心和末端（怎么用）
    pygame.draw.circle(chuangkou, (100, 50, 0), zhongxin, 10)  # 画转轴（是什么），美化界面（为什么），画小圆点（怎么用）

    pygame.display.flip(); shizhong.tick(60)

pygame.quit()
