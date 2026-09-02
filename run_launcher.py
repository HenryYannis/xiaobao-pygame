# 项目名称：XiaoBao-Pygame 游戏系列课程 (教师教学版)
# 项目作者：程小宝 (xbkjz.cn)
# 授权协议：MIT License

import os
import sys
import subprocess
import pygame

工作目录 = os.path.dirname(os.path.abspath(__file__))  # 锁定根目录绝对路径，确保工作路径不随执行目录偏移

def 获取游戏目录():                                   # 扫描根文件夹下所有以两位数字编号开头的游戏目录
    目录列表 = []
    for 名称 in os.listdir(工作目录):
        绝对路径 = os.path.join(工作目录, 名称)
        if os.path.isdir(绝对路径) and 名称[0:2].isdigit():
            目录列表.append(名称)
    目录列表.sort()                                    # 确保游戏按 01-18 的数字顺序排列展示
    return 目录列表

def 获取课程文件(目录名):                             # 检索对应游戏目录下的所有第X节课 Python 教学脚本
    文件列表 = []
    目录路径 = os.path.join(工作目录, 目录名)
    for 名称 in os.listdir(目录路径):
        if 名称.endswith(".py") and "第" in 名称 and "课" in 名称:
            文件列表.append(名称)
    文件列表.sort()                                    # 确保按课时先后顺序正序排列
    return 文件列表

def 解析课程标题(文件名):                             # 解析中文课时名生成精简易懂的卡片标题
    try:
        去后缀 = 文件名.replace(".py", "")
        拆分 = 去后缀.split("_")
        if len(拆分) >= 3:
            课时 = 拆分[1].replace("第", "").replace("节课", "").replace("课", "")
            功能 = 拆分[2]
            return f"Lesson {课时} - {功能}"
    except Exception:
        pass
    return 文件名

def 主菜单():                                         # 交互式图形启动器主界面与事件循环
    pygame.init()
    窗口 = pygame.display.set_mode((900, 650))
    pygame.display.set_caption("XiaoBao-Pygame Interactive Launcher")
    时钟 = pygame.time.Clock()

    字体小 = pygame.font.SysFont("microsoftyahei,simhei,simsun,arial", 15)
    字体中 = pygame.font.SysFont("microsoftyahei,simhei,simsun,arial", 18)
    字体标题 = pygame.font.SysFont("microsoftyahei,simhei,simsun,arial", 22, bold=True)

    游戏目录列表 = 获取游戏目录()
    当前选中游戏索引 = 0
    运行中 = True

    while 运行中:
        光标x, 光标y = pygame.mouse.get_pos()
        发生点击 = False

        for 事件 in pygame.event.get():
            if 事件.type == pygame.QUIT:
                运行中 = False
            elif 事件.type == pygame.MOUSEBUTTONUP and 事件.button == 1:
                发生点击 = True

        窗口.fill((30, 35, 45))                        # 主界面深暗底色

        if not 游戏目录列表:
            pygame.draw.rect(窗口, (20, 24, 33), (0, 0, 900, 650))
            错误提示1 = 字体标题.render("Error: No game folders found!", True, (255, 100, 100))
            错误提示2 = 字体中.render("Please place run_launcher.py in the project root folder.", True, (200, 200, 200))
            错误提示3 = 字体小.render(f"Current Path: {工作目录}", True, (150, 150, 150))
            窗口.blit(错误提示1, (100, 200))
            窗口.blit(错误提示2, (100, 245))
            窗口.blit(错误提示3, (100, 290))
        else:
            # 绘制左侧侧边栏
            pygame.draw.rect(窗口, (20, 24, 33), (0, 0, 320, 650))
            侧边标题 = 字体标题.render("XiaoBao Pygame", True, (0, 180, 255))
            窗口.blit(侧边标题, (20, 25))
            pygame.draw.line(窗口, (45, 52, 71), (0, 70), (320, 70), 2)

            for 序号, 目录 in enumerate(游戏目录列表):
                按钮y = 80 + 序号 * 28
                悬停中 = 10 <= 光标x <= 310 and 按钮y <= 光标y <= 按钮y + 26

                if 序号 == 当前选中游戏索引:
                    pygame.draw.rect(窗口, (0, 120, 215), (10, 按钮y, 300, 26), border_radius=4)
                elif 悬停中:
                    pygame.draw.rect(窗口, (45, 52, 71), (10, 按钮y, 300, 26), border_radius=4)

                if 悬停中 and 发生点击:
                    当前选中游戏索引 = 序号

                文字色 = (255, 255, 255) if (序号 == 当前选中游戏索引 or 悬停中) else (180, 190, 200)
                文字画面 = 字体小.render(目录, True, 文字色)
                窗口.blit(文字画面, (20, 按钮y + 4))

            # 左下角作者署名与链接
            pygame.draw.line(窗口, (45, 52, 71), (0, 600), (320, 600), 2)
            作者悬停 = 20 <= 光标x <= 250 and 610 <= 光标y <= 635
            作者色 = (0, 180, 255) if 作者悬停 else (150, 160, 180)
            作者画面 = 字体小.render("作者：程小宝 (xbkjz.cn)", True, 作者色)
            窗口.blit(作者画面, (20, 615))

            if 作者悬停 and 发生点击:
                import webbrowser
                webbrowser.open("http://xbkjz.cn")

            # 绘制右侧当前游戏课时详情区
            当前目录名 = 游戏目录列表[当前选中游戏索引]
            游戏标题画面 = 字体中.render(f"当前游戏: {当前目录名}", True, (255, 255, 255))
            窗口.blit(游戏标题画面, (350, 25))
            pygame.draw.line(窗口, (45, 52, 71), (320, 70), (900, 70), 2)

            课程列表 = 获取课程文件(当前目录名)
            for 下标, 文件名 in enumerate(课程列表):
                卡片y = 90 + 下标 * 75
                卡片矩形 = (350, 卡片y, 510, 62)
                卡片悬停 = 350 <= 光标x <= 860 and 卡片y <= 光标y <= 卡片y + 62

                if 卡片悬停:
                    pygame.draw.rect(窗口, (45, 55, 75), 卡片矩形, border_radius=6)
                    pygame.draw.rect(窗口, (0, 180, 255), 卡片矩形, width=1, border_radius=6)
                else:
                    pygame.draw.rect(窗口, (35, 42, 57), 卡片矩形, border_radius=6)

                标题文本 = 解析课程标题(文件名)
                标题画面 = 字体中.render(标题文本, True, (255, 255, 255))
                窗口.blit(标题画面, (370, 卡片y + 12))

                副标题画面 = 字体小.render(文件名, True, (150, 160, 180))
                窗口.blit(副标题画面, (370, 卡片y + 36))

                运行色 = (0, 200, 255) if 卡片悬停 else (180, 190, 200)
                运行文字 = 字体小.render("Run >", True, 运行色)
                窗口.blit(运行文字, (800, 卡片y + 22))

                if 卡片悬停 and 发生点击:
                    脚本路径 = os.path.join(工作目录, 当前目录名, 文件名)
                    try:
                        subprocess.run([sys.executable, 脚本路径])
                    except Exception as 错误:
                        print(f"Failed to launch: {错误}")

        pygame.display.flip()
        时钟.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    主菜单()
