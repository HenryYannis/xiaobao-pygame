import pygame, random, math                            # 新增代码：导入math库用于计算鼠标与地鼠的距离

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Whac-A-Mole - Lesson 2")
时钟 = pygame.time.Clock()

地洞列表 = []
for 行 in range(3):
    for 列 in range(3):
        地洞列表.append([列 * 120 + 80, 行 * 120 + 80])     # 九宫格网格：计算9个地洞的圆心坐标(x, y)

地鼠索引 = -1                                         # 地鼠状态：当前冒头的洞口编号，-1表示潜伏隐藏
下次冒头时间 = 0                                      # 刷新时刻：下一次更换洞口冒头的毫秒时间戳
运行中 = True

while 运行中:
    当前时间 = pygame.time.get_ticks()                 # 获取毫秒：获取游戏自启动以来的时间戳

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 事件.type == pygame.MOUSEBUTTONDOWN and 地鼠索引 != -1:  # 新增代码：有地鼠冒头时响应鼠标点击打击
            鼠标x, 鼠标y = pygame.mouse.get_pos()                 # 新增代码：获取点击时的鼠标坐标
            地鼠x, 地鼠y = 地洞列表[地鼠索引]                     # 新增代码：获取当前冒头地鼠的圆心坐标
            if math.hypot(鼠标x - 地鼠x, 鼠标y - 地鼠y) <= 30:     # 新增代码：勾股定理算距离，小于半径30判定击中
                地鼠索引 = -1                                     # 新增代码：击中后地鼠缩回潜伏隐藏
                下次冒头时间 = 当前时间 + 500                     # 新增代码：缩短等待时间，500毫秒后加速冒头

    if 当前时间 > 下次冒头时间:                       # 定时切换：当前时间超过预定时刻，地鼠随机换洞冒头
        地鼠索引 = random.randint(0, 8)               # 随机选洞：从9个地洞(0-8)中随机抽取一个
        下次冒头时间 = 当前时间 + 1000                # 预设间隔：设定1000毫秒(1秒)后再次切换

    窗口.fill((34, 139, 34))                           # 草地背景：RGB绿色(34, 139, 34)全屏填充
    for 编号, 坐标 in enumerate(地洞列表):             # 遍历地洞：依次获取每个地洞的编号索引与坐标
        pygame.draw.circle(窗口, (50, 25, 0), 坐标, 40)       # 绘制地洞：深褐色实心圆(半径40)
        if 编号 == 地鼠索引:
            pygame.draw.circle(窗口, (200, 150, 100), 坐标, 30) # 绘制地鼠：浅褐色实心圆(半径30)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
