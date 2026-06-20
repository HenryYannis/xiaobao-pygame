# 太空射击_第1节课_星空与飞船.py
# 学习目标：掌握Pygame窗口初始化，学习绘制多边形(Polygon)作为游戏主角，并设置深邃的星空背景

import pygame  # 导入库（是什么），2D游戏开发心脏（为什么），必选组件（怎么用）

pygame.init()  # 初始化（是什么），激活全部硬件接口（为什么），开头第一行运行（怎么用）

pingmu_kuan, pingmu_gao = 400, 600  # 定义尺寸（是什么），设定竖屏规格（为什么），变量名使用拼音（怎么用）
chuangkou = pygame.display.set_mode((pingmu_kuan, pingmu_gao))  # 创建窗口（是什么），定义显示区域（为什么），传入宽高元组（怎么用）
pygame.display.set_caption("Space Shooter - Lesson 1")  # 窗口标题（是什么），标识当前项目（为什么），传入文本（怎么用）

shizhong = pygame.time.Clock()  # 创建时钟（是什么），控制更新速率（为什么），锁定60FPS（怎么用）

# 飞船坐标：[x, y]
feichuan_weizhi = [200, 500]  # 定义飞船位置（是什么），存储在屏幕下方中央（为什么），用列表方便修改坐标（怎么用）

yunxing = True  # 开关（是什么），循环条件（为什么），逻辑开关（怎么用）
while yunxing:  # 主循环（是什么），逻辑中心（为什么），不断重复执行（怎么用）
    for shijian in pygame.event.get():  # 事件监听（是什么），捕捉动作（为什么），轮询读取（怎么用）
        if shijian.type == pygame.QUIT:  # 退出判定（是什么），点击关闭按钮（为什么），判断事件类型（怎么用）
            yunxing = False  # 停止循环（是什么），准备关闭（为什么），改标志位为False（怎么用）

    chuangkou.fill((10, 10, 30))  # 刷深蓝色背景（是什么），代表深邃的太空（为什么），传入RGB值(10,10,30)（怎么用）
    
    # 绘制飞船：使用多边形画出一个三角形飞船
    # 参数：(窗口, 颜色, 点坐标列表)
    dian_ji = [
        (feichuan_weizhi[0], feichuan_weizhi[1] - 20),      # 顶点：上方尖端
        (feichuan_weizhi[0] - 15, feichuan_weizhi[1] + 15),  # 左侧点
        (feichuan_weizhi[0] + 15, feichuan_weizhi[1] + 15)   # 右侧点
    ]  # 坐标计算（是什么），基于中心点偏移（为什么），定义三角形的三个角（怎么用）
    
    pygame.draw.polygon(chuangkou, (0, 200, 255), dian_ji)  # 画多边形（是什么），代表飞船（为什么），传入三个顶点的列表（怎么用）

    pygame.display.flip()  # 刷新显示（是什么），可见更新（为什么），flip方法（怎么用）
    shizhong.tick(60)  # 定帧60（是什么），稳定平滑（为什么），锁定60FPS（怎么用）

pygame.quit()  # 退出（是什么），清理资源（为什么），程序末尾（怎么用）
