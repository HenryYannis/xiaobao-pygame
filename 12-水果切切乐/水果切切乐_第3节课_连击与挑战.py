import pygame, random, math

pygame.init()
窗口 = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Fruit Slice - Lesson 3")
时钟 = pygame.time.Clock()
字体 = pygame.font.Font(None, 36)                     # 新增变量：纯内置默认字体(是什么)，避免跨平台字体报错(为什么)，字号36(怎么用)

水果列表 = []                                          # 存储所有抛出的水果数据[x, y, 水平速度, 垂直速度]
轨迹列表 = []                                          # 记录鼠标滑动划过的轨迹点坐标[(x, y), ...]
得分 = 0                                              # 新增变量：切中水果的累计得分
生命值 = 3                                            # 新增变量：玩家初始生命值(漏切扣血)
游戏结束 = False                                      # 新增变量：标记当前是否已耗尽生命值失败
运行中 = True

while 运行中:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            运行中 = False
        if 游戏结束 and 事件.type == pygame.KEYDOWN and 事件.key == pygame.K_SPACE:  # 新增代码：游戏结束后按空格键重开
            水果列表.clear()                          # 新增代码：清空当前残留水果
            轨迹列表.clear()                          # 新增代码：清空刀光轨迹
            得分 = 0                                  # 新增代码：重置分数为0
            生命值 = 3                                # 新增代码：恢复满血状态
            游戏结束 = False                          # 新增代码：重置为进行中状态

    if not 游戏结束:                                   # 新增代码：仅在游戏未结束时更新刀光轨迹与水果运动
        鼠标按下 = pygame.mouse.get_pressed()[0]
        if 鼠标按下:
            鼠标x, 鼠标y = pygame.mouse.get_pos()
            轨迹列表.append((鼠标x, 鼠标y))
            if len(轨迹列表) > 10:                     # 保持刀光长度：只保留最近10个坐标点
                轨迹列表.pop(0)
        else:
            轨迹列表.clear()                           # 松开鼠标后立即清空刀光轨迹

        if random.random() < 0.03:                     # 随机生成：每帧3%概率从底部向上抛出新水果
            水果列表.append([random.randint(50, 350), 410, random.uniform(-2, 2), -9.0])

        for 索引 in range(len(水果列表) - 1, -1, -1):  # 倒序遍历水果列表，防止pop删除元素时索引越界
            水果 = 水果列表[索引]
            水果[0] += 水果[2]                         # 坐标更新：累加水平移动速度
            水果[1] += 水果[3]                         # 坐标更新：累加垂直移动速度
            水果[3] += 0.25                            # 重力模拟：垂直速度每帧增加，形成下落抛物线

            已切中 = False
            for 点x, 点y in 轨迹列表:                  # 碰撞检测：比对刀光轨迹点与水果圆心的距离
                if math.hypot(点x - 水果[0], 点y - 水果[1]) <= 20:
                    水果列表.pop(索引)                 # 切开效果：命中后移除该水果
                    得分 += 10                        # 新增代码：切中水果奖励累加10分
                    已切中 = True
                    break

            if not 已切中 and 水果[1] > 420:           # 掉落销毁：水果掉出屏幕底部边界
                水果列表.pop(索引)
                生命值 -= 1                           # 新增代码：漏接水果扣除1点生命值
                if 生命值 <= 0:                       # 新增代码：生命值耗尽触发游戏结束
                    游戏结束 = True

    窗口.fill((20, 20, 20))                           # 暗色背景：RGB深灰黑(20, 20, 20)全屏填充
    for 水果 in 水果列表:
        pygame.draw.circle(窗口, (255, 140, 0), (int(水果[0]), int(水果[1])), 20)  # 绘制橙色水果(半径20)

    if len(轨迹列表) > 1:
        pygame.draw.lines(窗口, (255, 255, 255), False, 轨迹列表, 3)  # 绘制白色连续刀光轨迹线(线宽3)

    得分画面 = 字体.render(f"SCORE: {得分}  HP: {生命值}", True, (255, 255, 255)) # 新增代码：默认字体纯英文渲染得分与血量
    窗口.blit(得分画面, (10, 10))                                              # 新增代码：贴在左上角UI位置(10, 10)

    if 游戏结束:
        提示画面 = 字体.render("GAME OVER - Press SPACE", True, (255, 0, 0))      # 新增代码：红色英文大字提示失败与按空格重开
        窗口.blit(提示画面, (40, 180))                                           # 新增代码：居中贴在屏幕中央(40, 180)

    pygame.display.flip()                              # 双缓冲刷新：将新绘制的画面一次性呈现到屏幕
    时钟.tick(60)                                      # 锁定帧率：稳定每秒60帧流畅运行

pygame.quit()
