import pygame, random, math                            # 新增代码：导入math数学库用于计算点击距离

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Click Pop - Lesson 2")
时钟 = pygame.time.Clock()

气泡列表 = []                                          # 坐标容器：存储屏幕上所有活动气泡坐标[x, y]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.MOUSEBUTTONDOWN and 事件.button == 1:  # 新增代码：响应鼠标左键按下(button 1是左键，滚轮和右键不算)
            鼠标x, 鼠标y = 事件.pos                   # 新增代码：直接取事件自带的点击坐标，就是按下那一刻的位置
            for 索引 in range(len(气泡列表) - 1, -1, -1):  # 新增代码：倒序遍历索引，防止pop删除元素时漏检跳位
                气泡x, 气泡y = 气泡列表[索引]
                if math.hypot(鼠标x - 气泡x, 鼠标y - 气泡y) <= 20: # 新增代码：勾股定理算距离(是什么)，判断是否在圆内(为什么)，半径20(怎么用)
                    气泡列表.pop(索引)                 # 新增代码：命中消除(是什么)，从列表中移除(为什么)，传入索引删除(怎么用)
                    break                              # 新增代码：跳出循环(是什么)，单次点击只消一个(为什么)，break中断(怎么用)

    if random.random() < 0.03 and len(气泡列表) < 8:  # 随机生成：每帧3%概率产生新气泡，最多同时8个，不会铺满屏幕
        气泡列表.append([random.randint(20, 380), random.randint(20, 380)])

    窗口.fill((255, 255, 255))                         # 清空画布：擦除上一帧残留画面，白色RGB(255,255,255)全屏覆盖
    for 气泡 in 气泡列表:
        pygame.draw.circle(窗口, (0, 150, 255), 气泡, 20, 2)  # 绘制图形：天蓝色空心圆呈现气泡(圆心坐标, 半径20, 线宽2)

    pygame.display.flip()                              # 双缓冲刷新：将后台绘制好的画面一次性呈现在屏幕上，防闪烁
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
