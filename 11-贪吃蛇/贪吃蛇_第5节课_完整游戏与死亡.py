# 贪吃蛇_第5节课_完整游戏与死亡.py
# 学习目标：在第4节课基础上，加入死亡判定逻辑与实时计分，完成一个具备挑战性的完整游戏

import pygame, random  # 导入库（是什么），驱动逻辑（为什么），必备组件（怎么用）

pygame.init()  # 初始化（是什么），引擎预备（为什么），开头调用（怎么用）
chuangkou = pygame.display.set_mode((400, 400))  # 窗口（是什么），400像素舞台（为什么），元组定义（怎么用）
pygame.display.set_caption("Snake - Final Lesson")  # 标题（是什么），最终课标识（为什么），传入文本（怎么用）
shizhong, ziti = pygame.time.Clock(), pygame.font.SysFont(None, 30)  # 初始化（是什么），时钟与字体（为什么），一次性定义（怎么用）

gedian, sudu = 20, [0, 0]  # 基础参数（是什么），格点和初始速度（为什么），多变量定义（怎么用）
shetou_x, shetou_y, fenshu = 200, 200, 0  # 状态量（是什么），坐标与分数（为什么），变量初始化（怎么用）
she_shen = [[200, 200]]  # 蛇身容器（是什么），存储坐标列表（为什么），列表初始化（怎么用）
shiwu_x, shiwu_y = random.randint(0, 19) * gedian, random.randint(0, 19) * gedian  # 食物（是什么），对齐格点（为什么），随机计算（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑判断（怎么用）
while yunxing:  # 主循环（是什么），逻辑中枢（为什么），不断重复执行（怎么用）
    for shijian in pygame.event.get():  # 监听事件（是什么），捕捉动作（为什么），轮询获取（怎么用）
        if shijian.type == pygame.QUIT: yunxing = False  # 退出（是什么），点击关闭（为什么），改状态位（怎么用）
        if shijian.type == pygame.KEYDOWN:  # 方向控制（是什么），改变轨迹（为什么），增加转向逻辑（怎么用）
            if shijian.key == pygame.K_UP and sudu != [0, gedian]: sudu = [0, -gedian]  # 向上且防倒车（是什么），防反向自撞（为什么），加判断条件（怎么用）
            if shijian.key == pygame.K_DOWN and sudu != [0, -gedian]: sudu = [0, gedian]  # 向下且防倒车（是什么），防反向自撞（为什么），加判断条件（怎么用）
            if shijian.key == pygame.K_LEFT and sudu != [gedian, 0]: sudu = [-gedian, 0]  # 向左且防倒车（是什么），防反向自撞（为什么），加判断条件（怎么用）
            if shijian.key == pygame.K_RIGHT and sudu != [-gedian, 0]: sudu = [gedian, 0]  # 向右且防倒车（是什么），防反向自撞（为什么），加判断条件（怎么用）

    shetou_x += sudu[0]; shetou_y += sudu[1]  # 更新位置（是什么），持续位移（为什么），原坐标累加（怎么用）
    
    # 新增代码：死亡判定（撞墙或撞到自己）
    # she_shen[1:]表示除了头以外的身体部分，使用 in 检查新头部是否在身体里
    if shetou_x < 0 or shetou_x >= 400 or shetou_y < 0 or shetou_y >= 400 or [shetou_x, shetou_y] in she_shen[1:]:  # 死亡判断（是什么），判定输赢（为什么），逻辑组合判定（怎么用）
        yunxing = False  # 停止运行（是什么），游戏结束（为什么），直接退出循环（怎么用）

    she_shen.insert(0, [shetou_x, shetou_y])  # 加头（是什么），移动模型（为什么），列表插入（怎么用）
    if shetou_x == shiwu_x and shetou_y == shiwu_y:  # 进食（是什么），加分增长（为什么），坐标相等判定（怎么用）
        fenshu += 1  # 增加得分（是什么），反馈进度（为什么），变量累加（怎么用）
        shiwu_x, shiwu_y = random.randint(0, 19) * gedian, random.randint(0, 19) * gedian  # 重生食物（是什么），继续游戏（为什么），重随机（怎么用）
    else: she_shen.pop()  # 去尾（是什么），保持长度（为什么），pop操作（怎么用）

    chuangkou.fill((0, 0, 0))  # 刷黑（是什么），清除旧像（为什么），黑屏（怎么用）
    pygame.draw.rect(chuangkou, (255, 0, 0), (shiwu_x, shiwu_y, gedian, gedian))  # 画食物（是什么），红色（为什么），矩形（怎么用）
    for guanjie in she_shen: pygame.draw.rect(chuangkou, (0, 255, 0), (guanjie[0], guanjie[1], gedian, gedian))  # 画蛇（是什么），绿色（为什么），循环（怎么用）
    
    # 新增代码：实时显示分数
    chuangkou.blit(ziti.render(f"Score: {fenshu}", True, (255, 255, 255)), (10, 10))  # 显分（是什么），UI反馈（为什么），一步完成渲染与贴图（怎么用）

    pygame.display.flip(); shizhong.tick(10)  # 刷新并定帧（是什么），完成这一帧（为什么），低FPS（怎么用）

pygame.quit()  # 退出（是什么），清理内存（为什么），整个代码最后一行（怎么用）
