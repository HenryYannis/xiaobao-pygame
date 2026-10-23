# 增量标注检查：逐课和上一课比对"去掉注释后的代码行"，找出标注不准的地方。
#   误标：行尾写了"新增"，但上一课已经有一模一样的代码
#   漏标：上一课没有这行代码，行尾却没写"新增"或"修改代码"
#         (和上一课某行很像的，提示为"可能是修改"，建议标 # 修改代码：)
# 用法：python tools/check_increment.py            检查全部游戏，只打印报告
#       python tools/check_increment.py --strict   有问题时返回失败(可用于 CI)
# 说明：这是辅助工具，结果需要人工复核(例如 break、else: 这类很短的行一般不用标)。
# 项目作者：程小宝 (xbkjz.cn)

import os
import re
import sys
import glob
import difflib

根目录 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
无需标注 = {"else:", "break", "continue", "pass", "return", "try:", "]", ")", "}", "运行中 = False", "return True", "return False"}


def 拆分代码与注释(行):
    代码, 注释 = 行, ""
    if " #" in 行:
        位置 = 行.index(" #")
        if 行[:位置].count('"') % 2 == 0 and 行[:位置].count("'") % 2 == 0:
            代码, 注释 = 行[:位置], 行[位置 + 2:]
    return 代码.strip(), 注释.strip()


def 课时序号(路径):
    结果 = re.search(r"第(\d+)节", 路径)
    return int(结果.group(1)) if 结果 else 0


def 检查游戏(目录):
    课程 = sorted(glob.glob(os.path.join(目录, "*第*课*.py")), key=课时序号)
    问题数 = 0
    for 上一课, 本课 in zip(课程, 课程[1:]):
        旧代码 = []
        for 行 in open(上一课, encoding="utf-8"):
            代码, _ = 拆分代码与注释(行)
            if 代码 and not 代码.startswith("#"):
                旧代码.append(代码)
        剩余旧代码 = list(旧代码)
        报告 = []
        for 行号, 行 in enumerate(open(本课, encoding="utf-8"), 1):
            代码, 注释 = 拆分代码与注释(行)
            if not 代码 or 代码.startswith("#"):
                continue
            已标新增 = "新增" in 注释
            已标修改 = "修改代码" in 注释
            if 代码 in 剩余旧代码:
                剩余旧代码.remove(代码)
                if 已标新增:
                    报告.append(f"  第{行号}行 误标：上一课已有这行，不应标“新增” -> {代码}")
            elif 代码 in 无需标注 or 代码.startswith(("(", "[", '"', "pygame.display.set_caption")):
                continue                                        # 很短的行、多行列表里的数据行、窗口标题，不要求标注
            elif not (已标新增 or 已标修改):
                相似 = difflib.get_close_matches(代码, 旧代码, n=1, cutoff=0.75)
                类型 = "可能是修改(建议标 # 修改代码：)" if 相似 else "漏标新增"
                报告.append(f"  第{行号}行 {类型} -> {代码}")
        if 报告:
            问题数 += len(报告)
            print(os.path.relpath(本课, 根目录))
            print("\n".join(报告))
    return 问题数


if __name__ == "__main__":
    总数 = 0
    for 目录 in sorted(glob.glob(os.path.join(根目录, "[0-9][0-9]-*"))):
        总数 += 检查游戏(目录)
    print(f"\n共发现 {总数} 处需要人工复核的增量标注")
    if "--strict" in sys.argv and 总数:
        sys.exit(1)
