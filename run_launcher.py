# 项目名称：XiaoBao-Pygame 游戏系列课程 (教师教学版)
# 项目作者：程小宝 (xbkjz.cn)
# 授权协议：MIT License

import os
import re
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
    文件列表.sort(key=课时序号)                        # 按“第X节”里的数字排序，第10节课不会排到第2节课前面
    return 文件列表

def 课时序号(文件名):                                 # 从文件名“第X节课”里取出数字X
    结果 = re.search(r"第(\d+)节", 文件名)
    return int(结果.group(1)) if 结果 else 0

def 查找中文字体():                                   # 依次尝试 Windows/macOS/Linux 常见中文字体，找到就返回字体文件路径
    候选字体 = ["microsoftyahei", "simhei", "pingfangsc", "hiraginosansgb", "stheitimedium",
            "notosanscjksc", "notosanscjk", "sourcehansanssc", "wenquanyimicrohei", "wqyzenhei", "droidsansfallback"]
    for 字体名 in 候选字体:
        路径 = pygame.font.match_font(字体名)
        if 路径:
            return 路径
    return None                                        # 一个都没找到：界面改用英文显示，避免汉字变成方块

英文游戏名 = {"01": "Pixel Painter", "02": "Bubble Pop", "03": "Rhythm Blocks", "04": "Catch Fruit",
         "05": "Whack-a-Mole", "06": "Bounce Ball", "07": "Dino Jump", "08": "Tic-Tac-Toe",
         "09": "Number Puzzle", "10": "Snake", "11": "Flappy Flight", "12": "Fruit Slice",
         "13": "Color Match", "14": "Maze Escape", "15": "Breakout", "16": "Space Shooter",
         "17": "Color Memory", "18": "Gold Miner"}  # 没有中文字体时界面显示的英文名

def 显示名称(中文名, 序号, 有中文字体):               # 没有中文字体时，用英文名称代替中文名称
    if 有中文字体:
        return 中文名
    if 序号 is not None:
        return f"Lesson {序号}"
    编号 = 中文名[0:2]
    return f"{编号} {英文游戏名.get(编号, 'Game')}"

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

    中文字体路径 = 查找中文字体()
    有中文字体 = 中文字体路径 is not None
    字体小 = pygame.font.Font(中文字体路径, 15 if 有中文字体 else 20)  # 路径为 None 时使用 pygame 内置默认字体
    字体中 = pygame.font.Font(中文字体路径, 18 if 有中文字体 else 24)
    字体标题 = pygame.font.Font(中文字体路径, 22 if 有中文字体 else 30)
    字体标题.set_bold(True)

    游戏目录列表 = 获取游戏目录()
    课程缓存 = {目录: 获取课程文件(目录) for 目录 in 游戏目录列表}  # 启动时只扫描一次文件夹，不再每帧读硬盘
    当前选中游戏索引 = 0
    列表滚动 = 0                                       # 左侧游戏列表向下滚动了几行(游戏超过 18 个时用鼠标滚轮翻看)
    最多显示行数 = 18
    错误信息 = ""
    运行中 = True

    while 运行中:
        光标x, 光标y = pygame.mouse.get_pos()
        发生点击 = False

        for 事件 in pygame.event.get():
            if 事件.type == pygame.QUIT:
                运行中 = False
            elif 事件.type == pygame.MOUSEBUTTONUP and 事件.button == 1:
                发生点击 = True
            elif 事件.type == pygame.MOUSEWHEEL and 光标x < 320:
                最大滚动 = max(0, len(游戏目录列表) - 最多显示行数)
                列表滚动 = max(0, min(最大滚动, 列表滚动 - 事件.y))  # 滚轮向上 y 为正，列表往回滚

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
            pygame.draw.rect(窗口, (20, 24, 33), (0, 0, 320, 650))  # 绘制左侧侧边栏
            侧边标题 = 字体标题.render("XiaoBao Pygame", True, (0, 180, 255))
            窗口.blit(侧边标题, (20, 25))
            pygame.draw.line(窗口, (45, 52, 71), (0, 70), (320, 70), 2)

            for 序号, 目录 in enumerate(游戏目录列表):
                if not 列表滚动 <= 序号 < 列表滚动 + 最多显示行数:
                    continue                           # 超出可见区域的游戏先不画，避免压住底部署名
                按钮y = 80 + (序号 - 列表滚动) * 28
                悬停中 = 10 <= 光标x <= 310 and 按钮y <= 光标y <= 按钮y + 26

                if 序号 == 当前选中游戏索引:
                    pygame.draw.rect(窗口, (0, 120, 215), (10, 按钮y, 300, 26), border_radius=4)
                elif 悬停中:
                    pygame.draw.rect(窗口, (45, 52, 71), (10, 按钮y, 300, 26), border_radius=4)

                if 悬停中 and 发生点击:
                    当前选中游戏索引 = 序号
                    错误信息 = ""

                文字色 = (255, 255, 255) if (序号 == 当前选中游戏索引 or 悬停中) else (180, 190, 200)
                文字画面 = 字体小.render(显示名称(目录, None, 有中文字体), True, 文字色)
                窗口.blit(文字画面, (20, 按钮y + 4))

            pygame.draw.line(窗口, (45, 52, 71), (0, 600), (320, 600), 2)  # 左下角作者署名与链接
            作者悬停 = 20 <= 光标x <= 250 and 610 <= 光标y <= 635
            作者色 = (0, 180, 255) if 作者悬停 else (150, 160, 180)
            作者文字 = "作者：程小宝 (xbkjz.cn)" if 有中文字体 else "Author: Cheng Xiaobao (xbkjz.cn)"
            作者画面 = 字体小.render(作者文字, True, 作者色)
            窗口.blit(作者画面, (20, 615))

            if 作者悬停 and 发生点击:
                import webbrowser
                webbrowser.open("http://xbkjz.cn")

            当前目录名 = 游戏目录列表[当前选中游戏索引]          # 绘制右侧当前游戏课时详情区
            游戏标题文字 = f"当前游戏: {当前目录名}" if 有中文字体 else f"Current: {显示名称(当前目录名, None, False)}"
            游戏标题画面 = 字体中.render(游戏标题文字, True, (255, 255, 255))
            窗口.blit(游戏标题画面, (350, 25))
            pygame.draw.line(窗口, (45, 52, 71), (320, 70), (900, 70), 2)

            课程列表 = 课程缓存[当前目录名]
            for 下标, 文件名 in enumerate(课程列表):
                卡片y = 90 + 下标 * 75
                卡片矩形 = (350, 卡片y, 510, 62)
                卡片悬停 = 350 <= 光标x <= 860 and 卡片y <= 光标y <= 卡片y + 62

                if 卡片悬停:
                    pygame.draw.rect(窗口, (45, 55, 75), 卡片矩形, border_radius=6)
                    pygame.draw.rect(窗口, (0, 180, 255), 卡片矩形, width=1, border_radius=6)
                else:
                    pygame.draw.rect(窗口, (35, 42, 57), 卡片矩形, border_radius=6)

                标题文本 = 解析课程标题(文件名) if 有中文字体 else 显示名称(文件名, 课时序号(文件名), False)
                标题画面 = 字体中.render(标题文本, True, (255, 255, 255))
                窗口.blit(标题画面, (370, 卡片y + 12))

                if 有中文字体:
                    副标题画面 = 字体小.render(文件名, True, (150, 160, 180))
                    窗口.blit(副标题画面, (370, 卡片y + 36))

                运行色 = (0, 200, 255) if 卡片悬停 else (180, 190, 200)
                运行文字 = 字体小.render("Run >", True, 运行色)
                窗口.blit(运行文字, (800, 卡片y + 22))

                if 卡片悬停 and 发生点击:
                    脚本路径 = os.path.join(工作目录, 当前目录名, 文件名)
                    try:
                        subprocess.Popen([sys.executable, 脚本路径], cwd=os.path.dirname(脚本路径))  # Popen 不等课程结束，启动器继续刷新画面
                        错误信息 = ""
                    except Exception as 错误:
                        错误信息 = f"Failed to launch: {错误}"
                        print(错误信息)
                    pygame.event.clear()               # 清掉启动瞬间多余的点击，避免误启动别的课

            if 错误信息:
                错误画面 = 字体小.render(错误信息[:70], True, (255, 100, 100))  # 双击运行看不到控制台，所以把错误画在界面上
                窗口.blit(错误画面, (350, 615))

        pygame.display.flip()
        时钟.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    主菜单()
