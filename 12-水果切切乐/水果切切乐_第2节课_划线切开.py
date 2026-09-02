import pygame, random, math                            # 新增代码：导入math库用于计算轨迹点与水果圆心的距离

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Fruit Slice - Lesson 2")
时钟 = pygame.time.Clock()

水果列表 = []                                          # 存储所有抛出的水果数据[x, y, 水平速度, 垂直速度]
轨迹列表 = []                                          # 新增变量：记录鼠标滑动划过的轨迹点坐标[(x, y), ...]
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False

    鼠标按下 = pygame.mouse.get_pressed()[0]           # 新增代码：获取鼠标左键按下状态
    if 鼠标按下:
        鼠标x, 鼠标y = pygame.mouse.get_pos()          # 新增代码：获取当前鼠标移动坐标
        轨迹列表.append((鼠标x, 鼠标y))                 # 新增代码：追加轨迹点
        if len(轨迹列表) > 10:                         # 新增代码：只保留最近10个点形成拖尾刀光
            轨迹列表.pop(0)
    else:
        轨迹列表.clear()                               # 新增代码：松开鼠标后清空刀光轨迹

    if random.random() < 0.03:                         # 随机生成：每帧3%概率从底部向上抛出新水果
        水果列表.append([random.randint(50, 350), 410, random.uniform(-2, 2), -9.0])

    for 索引 in range(len(水果列表) - 1, -1, -1):      # 倒序遍历水果列表，防止pop删除元素时索引越界
        水果 = 水果列表[索引]
        水果[0] += 水果[2]                             # 坐标更新：累加水平移动速度
        水果[1] += 水果[3]                             # 坐标更新：累加垂直移动速度
        水果[3] += 0.25                                # 重力模拟：垂直速度每帧增加，形成下落抛物线

        已切中 = False                                 # 新增代码：标记当前水果是否被切中
        for 点x, 点y in 轨迹列表:                      # 新增代码：遍历刀光轨迹点
            if math.hypot(点x - 水果[0], 点y - 水果[1]) <= 20:  # 新增代码：欧几里得距离小于半径20判定切开
                水果列表.pop(索引)                     # 新增代码：命中切开移除水果
                已切中 = True
                break

        if not 已切中 and 水果[1] > 420:               # 掉落销毁：水果未被切中且掉出屏幕底部时移除
            水果列表.pop(索引)

    窗口.fill((20, 20, 20))                           # 暗色背景：RGB深灰黑(20, 20, 20)全屏填充
    for 水果 in 水果列表:
        pygame.draw.circle(窗口, (255, 140, 0), (int(水果[0]), int(水果[1])), 20)  # 绘制橙色水果(半径20)

    if len(轨迹列表) > 1:
        pygame.draw.lines(窗口, (255, 255, 255), False, 轨迹列表, 3)  # 新增代码：绘制白色连续刀光轨迹线(线宽3)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
