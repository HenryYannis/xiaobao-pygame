import pygame, random, math

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Click Pop - Lesson 3")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 36)                     # 新增变量：纯内置默认字体(是什么)，避免跨平台系统字体报错(为什么)，字号36(怎么用)

得分 = 0                                              # 新增变量：当前消除成绩
倒计时秒数 = 15                                       # 新增变量：游戏限制时间
开始时间 = pygame.time.get_ticks()                    # 新增变量：本局开始的毫秒时间戳，重开时刷新它，倒计时才会重新开始
剩余时间 = 倒计时秒数
气泡列表 = []
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.MOUSEBUTTONDOWN and 事件.button == 1 and 剩余时间 > 0:  # 新增代码：时间未结束时才响应鼠标左键
            鼠标x, 鼠标y = 事件.pos                   # 取事件自带的点击坐标
            for 索引 in range(len(气泡列表) - 1, -1, -1):  # 倒序遍历索引，防止pop删除元素时漏检跳位
                气泡x, 气泡y = 气泡列表[索引]
                if math.hypot(鼠标x - 气泡x, 鼠标y - 气泡y) <= 20:  # 勾股定理算距离(是什么)，判断是否在圆内(为什么)，半径20(怎么用)
                    气泡列表.pop(索引)                # 命中消除(是什么)，从列表中移除(为什么)，传入索引删除(怎么用)
                    得分 += 1                         # 新增代码：加分奖励(是什么)，累加成绩(为什么)，递增1分(怎么用)
                    break                             # 跳出循环(是什么)，单次点击只消一个(为什么)，break中断(怎么用)
        if 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE and 剩余时间 <= 0:  # 新增代码：时间到后按空格重开
            得分 = 0                                  # 新增代码：分数清零
            开始时间 = pygame.time.get_ticks()        # 新增代码：重新记录开始时间，倒计时从15秒重新开始
            剩余时间 = 倒计时秒数                     # 新增代码：剩余时间恢复满格

    已运行秒数 = (pygame.time.get_ticks() - 开始时间) // 1000  # 新增代码：本局已运行整秒数(是什么)，当前毫秒减开始毫秒再整除1000(为什么)，作为扣减依据(怎么用)
    剩余时间 = max(0, 倒计时秒数 - 已运行秒数)         # 新增代码：计算剩余时间(是什么)，限制最小为0(为什么)，max函数防负数(怎么用)

    if 剩余时间 > 0:
        if random.random() < 0.05 and len(气泡列表) < 8:  # 随机生成：每帧5%概率冒出新气泡，最多同时8个
            气泡列表.append([random.randint(20, 380), random.randint(20, 380)])
    else:
        气泡列表.clear()                               # 新增代码：时间耗尽清屏(是什么)，定格终局(为什么)，清空列表(怎么用)

    窗口.fill((255, 255, 255))                         # 清空画布：擦除上一帧残留画面，白色RGB(255,255,255)全屏覆盖
    for 气泡 in 气泡列表:
        pygame.draw.circle(窗口, (0, 150, 255), 气泡, 20, 2)  # 绘制图形：天蓝色空心圆呈现气泡(圆心坐标, 半径20, 线宽2)

    得分画面 = 字体.render(f"SCORE: {得分}", True, (0, 0, 0))       # 新增代码：默认字体渲染英文SCORE成绩图像(黑色)
    窗口.blit(得分画面, (10, 10))                                   # 新增代码：贴到左上角UI位置(10, 10)
    时间画面 = 字体.render(f"TIME: {剩余时间}s", True, (255, 0, 0)) # 新增代码：红色英文字符串渲染剩余时间
    窗口.blit(时间画面, (270, 10))                                  # 新增代码：贴到右上角UI位置(270, 10)

    if 剩余时间 <= 0:
        提示画面 = 字体.render("TIME UP! - Press SPACE", True, (255, 0, 0))  # 新增代码：终局大字提示(是什么)，红字醒目(为什么)，提示按空格重开(怎么用)
        窗口.blit(提示画面, 提示画面.get_rect(center=(200, 200)))  # 新增代码：get_rect(center=...)让文字正好居中在窗口中央

    pygame.display.flip()                              # 双缓冲刷新：将后台绘制好的画面一次性呈现在屏幕上，防闪烁
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
