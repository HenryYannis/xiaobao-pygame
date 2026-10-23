# 冒烟测试：在没有显示器的环境(如 GitHub Actions)里，把每一节课自动运行若干帧，
# 同时随机模拟鼠标点击、拖动和按键，只要有任何一节课抛出异常就判定失败。
# 用法：python tools/smoke_test.py            测试全部课程(每课默认 300 帧)
#       python tools/smoke_test.py 某课.py 600  只测试一节课，跑 600 帧
# 项目作者：程小宝 (xbkjz.cn)

import os
import sys
import glob
import random
import runpy
import subprocess

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")              # 虚拟显示驱动：不弹出真实窗口
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")              # 虚拟声卡驱动：没有声卡也能初始化

根目录 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class 跑够帧数(Exception):
    pass


class 不等待的时钟:
    def tick(self, 帧率=0):
        return 16

    def get_fps(self):
        return 60.0

    def get_time(self):
        return 16


def 测试单节课(脚本路径, 帧数):
    import pygame

    random.seed(1)
    已画帧数 = [0]
    原始取事件 = pygame.event.get
    测试按键 = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE,
            pygame.K_RETURN, pygame.K_r, pygame.K_a, pygame.K_d, pygame.K_f, pygame.K_j]

    def 随机坐标():
        窗口 = pygame.display.get_surface()
        宽, 高 = 窗口.get_size() if 窗口 else (400, 400)
        return (random.randint(0, 宽 - 1), random.randint(0, 高 - 1))

    def 模拟取事件(*参数, **关键字):
        事件列表 = 原始取事件(*参数, **关键字)
        r = random.random()
        if r < 0.15:
            事件列表.append(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=随机坐标(), button=1))
        elif r < 0.25:
            事件列表.append(pygame.event.Event(pygame.MOUSEBUTTONUP, pos=随机坐标(), button=1))
        elif r < 0.35:
            事件列表.append(pygame.event.Event(pygame.MOUSEMOTION, pos=随机坐标(), rel=(5, 5), buttons=(1, 0, 0)))
        elif r < 0.55:
            事件列表.append(pygame.event.Event(pygame.KEYDOWN, key=random.choice(测试按键), mod=0, unicode="", scancode=0))
        elif r < 0.6:
            事件列表.append(pygame.event.Event(pygame.KEYUP, key=random.choice(测试按键), mod=0, unicode="", scancode=0))
        return 事件列表

    def 计数():
        已画帧数[0] += 1
        if 已画帧数[0] >= 帧数:
            raise 跑够帧数()

    原始flip = pygame.display.flip
    原始update = pygame.display.update
    pygame.display.flip = lambda *a: (原始flip(), 计数())
    pygame.display.update = lambda *a: (原始update(*a), 计数())
    pygame.event.get = 模拟取事件
    pygame.time.get_ticks = lambda: 已画帧数[0] * 16                 # 虚拟时钟：每帧算 16 毫秒，计时器照样会走
    pygame.time.Clock = 不等待的时钟                                # 不真的等待，测试跑得飞快
    pygame.mouse.get_pos = 随机坐标
    pygame.mouse.get_pressed = lambda *a, **k: (random.random() < 0.3, False, False)

    try:
        runpy.run_path(脚本路径, run_name="__main__")
    except (跑够帧数, SystemExit):
        pass
    print(f"OK {已画帧数[0]} 帧")


def 测试全部(帧数):
    课程列表 = sorted(glob.glob(os.path.join(根目录, "[0-9][0-9]-*", "*第*课*.py")))
    失败列表 = []
    for 脚本 in 课程列表:
        名称 = os.path.relpath(脚本, 根目录)
        try:
            结果 = subprocess.run([sys.executable, os.path.abspath(__file__), 脚本, str(帧数)],
                                cwd=os.path.dirname(脚本), capture_output=True, text=True,
                                encoding="utf-8", errors="replace", timeout=120)
            通过 = 结果.returncode == 0
            输出 = 结果.stdout + 结果.stderr
        except subprocess.TimeoutExpired:
            通过, 输出 = False, "超时"
        print(("通过  " if 通过 else "失败  ") + 名称, flush=True)
        if not 通过:
            失败列表.append(名称)
            print(输出)
    print(f"\n共 {len(课程列表)} 节课，失败 {len(失败列表)} 节")
    if not 课程列表 or 失败列表:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].endswith(".py"):
        测试单节课(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 300)
    else:
        测试全部(int(sys.argv[1]) if len(sys.argv) > 1 else 300)
