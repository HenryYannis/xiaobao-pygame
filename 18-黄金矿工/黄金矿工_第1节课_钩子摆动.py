import pygame, math

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Gold Miner - Lesson 1")
时钟 = pygame.time.Clock()

锚点x, 锚点y = 200, 50                                 # 矿工绳索顶部悬挂中心固定锚点坐标
绳长 = 50.0                                           # 绳索当前伸缩长度(初始收拢为50)
角度 = 0.0                                            # 钩子摆动角度(-75度至75度)
摆动时间 = 0                                          # 钩子已经摆动了多少帧(只在摆动状态下累加)
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    摆动时间 += 1                                     # 摆动计时器：每帧加1
    角度 = math.sin(摆动时间 / 30.0) * 75.0           # 正弦函数驱动单摆左右周期性晃动(摆动时间每过30帧约走1弧度)

    弧度 = math.radians(角度 + 90.0)                  # 极坐标换算：根据锚点、绳长和摆角，计算钩子末端在笛卡尔坐标系中的(x, y)
    钩尖x = 锚点x + 绳长 * math.cos(弧度)
    钩尖y = 锚点y + 绳长 * math.sin(弧度)

    窗口.fill((245, 235, 195))                         # 暖沙黄色地下矿洞背景全屏填充

    pygame.draw.line(窗口, (70, 50, 30), (锚点x, 锚点y), (钩尖x, 钩尖y), 3)  # 绘制棕褐色矿工绳索
    pygame.draw.circle(窗口, (120, 120, 120), (int(钩尖x), int(钩尖y)), 6)   # 绘制绳头金属挂钩

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
