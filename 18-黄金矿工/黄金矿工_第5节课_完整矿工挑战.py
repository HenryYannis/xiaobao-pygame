import pygame, math, random

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Gold Miner - Lesson 5")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 32)                     # 创建纯内置默认字体(是什么)，避免跨平台字体报错(为什么)，字号32(怎么用)

锚点x, 锚点y = 200, 50                                 # 矿工绳索顶部悬挂中心固定锚点坐标
绳长 = 50.0                                           # 绳索当前伸缩长度(初始收拢为50)
角度 = 0.0                                            # 钩子摆动角度(-75度至75度)
钩子状态 = "摆动"                                     # 钩子运行模式("摆动", "出钩", "收钩")
抓到金块 = None                                       # 记录当前钩住的金块对象[x, y, 半径]

def 生成金块():                                       # 新增函数：在地下随机生成5个不同大小金块
    return [[random.randint(60, 340), random.randint(160, 350), random.randint(12, 28)] for _ in range(5)]

金块列表 = 生成金块()
得分 = 0                                              # 新增变量：抓取金块累计得分
开始时间 = pygame.time.get_ticks()                     # 新增变量：记录开局毫秒时间戳
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()
    剩余秒数 = max(0, 30 - (当前时间 - 开始时间) // 1000)  # 新增代码：30秒限时倒计时计算

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 剩余秒数 <= 0 and 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 新增代码：超时按空格重开
            金块列表 = 生成金块()                     # 新增代码：重置地下金块
            得分 = 0                                  # 新增代码：重置分数
            开始时间 = pygame.time.get_ticks()         # 新增代码：重置倒计时
            绳长 = 50.0
            钩子状态 = "摆动"
            抓到金块 = None

        elif 剩余秒数 > 0 and 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:
            if 钩子状态 == "摆动":
                钩子状态 = "出钩"                     # 按空格键释放钩子笔直射出

    if 剩余秒数 > 0:                                   # 仅在限时未耗尽时执行物理计算
        if 钩子状态 == "摆动":
            角度 = math.sin(当前时间 / 500.0) * 75.0   # 正弦函数驱动单摆左右周期性晃动
        elif 钩子状态 == "出钩":
            绳长 += 6.0                               # 钩子沿当前朝向快速向外伸展
        elif 钩子状态 == "收钩":
            # 载重物理模拟：抓到的金块体积半径越大，负重越沉，收卷拉力速度越慢
            收绳速度 = max(1.5, 6.0 - (抓到金块[2] / 6.0 if 抓到金块 else 0))
            绳长 -= 收绳速度
            if 绳长 <= 50.0:                           # 钩子完全收回矿车
                if 抓到金块:
                    得分 += 抓到金块[2] * 2            # 新增代码：成功拉上金块，按尺寸翻倍计入得分
                    抓到金块 = None
                绳长 = 50.0
                钩子状态 = "摆动"                     # 恢复摆动准备下一次发射

        # 极坐标换算：根据锚点、绳长和摆角，计算钩子末端在笛卡尔坐标系中的(x, y)
        弧度 = math.radians(角度 + 90.0)
        钩尖x = 锚点x + 绳长 * math.cos(弧度)
        钩尖y = 锚点y + 绳长 * math.sin(弧度)

        if 钩子状态 == "出钩":
            # 边缘触界折返判定
            if 钩尖x < 10 or 钩尖x > 390 or 钩尖y > 390:
                钩子状态 = "收钩"

            # 抓取金块碰撞检测：检测钩尖与各个地下金块圆心的欧式距离
            for 索引 in range(len(金块列表) - 1, -1, -1):
                金块 = 金块列表[索引]
                if math.hypot(钩尖x - 金块[0], 钩尖y - 金块[1]) < 金块[2]:
                    抓到金块 = 金块列表.pop(索引)       # 将金块从地下矿层中拔出
                    钩子状态 = "收钩"                 # 命中目标立即进入收钩状态
                    break
    else:
        弧度 = math.radians(角度 + 90.0)
        钩尖x = 锚点x + 绳长 * math.cos(弧度)
        钩尖y = 锚点y + 绳长 * math.sin(弧度)

    窗口.fill((245, 235, 195))                         # 暖沙黄色地下矿洞背景全屏填充

    for 金块 in 金块列表:                              # 循环绘制地下闪闪发光的黄金矿石
        pygame.draw.circle(窗口, (255, 200, 0), (金块[0], 金块[1]), 金块[2])

    if 抓到金块:                                       # 绘制钩尖上紧紧锁定的金块
        pygame.draw.circle(窗口, (255, 200, 0), (int(钩尖x), int(钩尖y)), 抓到金块[2])

    pygame.draw.line(窗口, (70, 50, 30), (锚点x, 锚点y), (钩尖x, 钩尖y), 3)  # 绘制棕褐色矿工绳索
    pygame.draw.circle(窗口, (120, 120, 120), (int(钩尖x), int(钩尖y)), 6)   # 绘制绳头金属挂钩

    得分画面 = 字体.render(f"SCORE: {得分}", True, (50, 40, 20))       # 默认字体纯英文渲染得分看板
    窗口.blit(得分画面, (10, 10))

    时间画面 = 字体.render(f"TIME: {剩余秒数}s", True, (220, 40, 40))   # 新增代码：右上角红色英文倒计时
    窗口.blit(时间画面, (280, 10))

    if 剩余秒数 <= 0:                                  # 新增代码：倒计时归零居中展示超时挑战结束
        提示画面 = 字体.render("TIME UP! - Press SPACE", True, (220, 40, 40))
        窗口.blit(提示画面, (50, 180))

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
