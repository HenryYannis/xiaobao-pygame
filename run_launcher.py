# 项目名称：XiaoBao-Pygame 游戏系列课程 (教师教学版)
# 项目作者：程小宝 (xbkjz.cn)
# 授权协议：MIT License

import os  # 导入系统库（是什么），进行路径和文件操作（为什么），系统模块直接调用（怎么用）
import sys  # 导入解释器库（是什么），获取当前Python执行路径（为什么），系统模块直接调用（怎么用）
import subprocess  # 导入子进程库（是什么），用于启动并运行游戏脚本（为什么），系统模块直接调用（怎么用）
import pygame  # 导入Pygame引擎（是什么），用于创建窗口渲染界面和捕获键鼠事件（为什么），标准库导入后直接调用（怎么用）

# 全局变量：锁定当前脚本文件所在的绝对目录路径
gongzuo_mulu = os.path.dirname(os.path.abspath(__file__))  # 根目录（是什么），确保工作路径不随执行目录偏移（为什么），__file__获取绝对路径（怎么用）

def huo_qu_you_xi_mulu():  # 获取游戏目录函数（是什么），收集所有以数字开头的游戏文件夹（为什么），无参数返回排序列表（怎么用）
    mulu_liebiao = []  # 目录列表（是什么），存储符合条件的游戏目录名称（为什么），初始化为空列表（怎么用）
    for mingzi in os.listdir(gongzuo_mulu):  # 遍历当前目录（是什么），扫描根文件夹下的项目（为什么），os.listdir扫描gongzuo_mulu（怎么用）
        juedui_lujing = os.path.join(gongzuo_mulu, mingzi)  # 绝对路径（是什么），检查是否是文件夹（为什么），join组合路径（怎么用）
        if os.path.isdir(juedui_lujing) and mingzi[0:2].isdigit():  # 条件判断（是什么），过滤出前两位是数字的文件夹（为什么），isdigit与isdir组合（怎么用）
            mulu_liebiao.append(mingzi)  # 添加目录（是什么），将符合的放入列表（为什么），append追加到末尾（怎么用）
    mulu_liebiao.sort()  # 排序目录（是什么），确保游戏按01-18的数字顺序排列（为什么），sort就地排序（怎么用）
    return mulu_liebiao  # 返回结果（是什么），供主逻辑渲染菜单使用（为什么），return关键字返回列表（怎么用）

def huo_qu_ke_cheng_wenjian(mulu_mingzi):  # 获取课程文件函数（是什么），检索该游戏目录下的所有第X课的py文件（为什么），接收目录名称并返回排序列表（怎么用）
    wenjian_liebiao = []  # 文件列表（是什么），存储匹配的python游戏脚本路径（为什么），初始化为空列表（怎么用）
    mulu_lujing = os.path.join(gongzuo_mulu, mulu_mingzi)  # 拼接路径（是什么），获取游戏目录的绝对路径（为什么），os.path.join安全拼接（怎么用）
    for mingzi in os.listdir(mulu_lujing):  # 遍历该目录（是什么），查找里面的脚本文件（为什么），os.listdir列出子文件（怎么用）
        if mingzi.endswith(".py") and "第" in mingzi and "课" in mingzi:  # 条件过滤（是什么），只找教学用.py代码（为什么），endswith与成员运算符组合（怎么用）
            wenjian_liebiao.append(mingzi)  # 添加文件（是什么），把脚本名存入列表（为什么），append追加到末尾（怎么用）
    wenjian_liebiao.sort()  # 排序文件（是什么），确保按课时先后顺序展示（为什么），sort就地排序（怎么用）
    return wenjian_liebiao  # 返回结果（是什么），供子菜单选择使用（为什么），return关键字返回列表（怎么用）

def jie_xi_wenjian(wenjian_mingzi):  # 解析文件名函数（是什么），把中文课时名转换成精简版展示（为什么），接收文件名返回格式化后的文本（怎么用）
    try:  # 捕获异常（是什么），防止非标准文件命名导致报错（为什么），try...except保障（怎么用）
        mingzi_wu_houzhui = wenjian_mingzi.replace(".py", "")  # 去后缀（是什么），去掉扩展名.py（为什么），replace方法替换（怎么用）
        bufen = mingzi_wu_houzhui.split("_")  # 切割字符串（是什么），以底划线切分文件名（为什么），split方法拆分（怎么用）
        if len(bufen) >= 3:  # 格式检查（是什么），验证切分部分是否符合预期（为什么），判断长度是否大于等于3（怎么用）
            keshi = bufen[1].replace("第", "").replace("节课", "")  # 提取课时（是什么），拿到数字（为什么），replace连续清洗（怎么用）
            gongneng = bufen[2]  # 提取功能（是什么），获取课程内容说明（为什么），索引访问第三项（怎么用）
            return f"Lesson {keshi} - {gongneng}"  # 返回组合（是什么），生成干净的课程名（为什么），f-string格式化（怎么用）
    except Exception:  # 异常分支（是什么），捕捉任何处理失败（为什么），不报错降级显示（怎么用）
        pass  # 忽略错误（是什么），继续往下执行（为什么），pass空操作（怎么用）
    return wenjian_mingzi  # 降级返回（是什么），直接返回原文件名（为什么），return原值（怎么用）

def zhu_caidan():  # 启动器主界面与事件循环（是什么），处理图形界面的渲染和游戏运行触发（为什么），直接调用启动UI（怎么用）
    pygame.init()  # 初始化引擎（是什么），准备好字体和窗口模块（为什么），开局首先调用（怎么用）
    chuangkou = pygame.display.set_mode((900, 650))  # 创建主窗口（是什么），设置900x650的分辨率（为什么），传入尺寸元组（怎么用）
    pygame.display.set_caption("XiaoBao-Pygame Interactive Launcher")  # 窗口标题（是什么），指示当前是启动器程序（为什么），传入文本参数（怎么用）
    shizhong = pygame.time.Clock()  # 锁定帧率时钟（是什么），确保GUI平滑刷新不占满CPU（为什么），创建Clock实例（怎么用）
    
    ziti_xiao = pygame.font.SysFont("microsoftyahei,simhei,simsun,arial", 15)  # 小号字体（是什么），用于列表和署名（为什么），SysFont安全加载（怎么用）
    ziti_zhong = pygame.font.SysFont("microsoftyahei,simhei,simsun,arial", 18)  # 中号字体（是什么），用于课时卡片和右侧标题（为什么），SysFont安全加载（怎么用）
    ziti_biaoti = pygame.font.SysFont("microsoftyahei,simhei,simsun,arial", 22, bold=True)  # 粗体大字（是什么），用于侧边栏大标题（为什么），SysFont设置粗体参数（怎么用）
    
    you_xi_mulu = huo_qu_you_xi_mulu()  # 获取目录（是什么），得到排序好的18个游戏文件夹列表（为什么），无参调用（怎么用）
    xuanze_you_xi_index = 0  # 选中索引（是什么），记录当前左侧点击的游戏项（为什么），初始为0指向第一项（怎么用）
    
    yunxing = True  # 循环标志（是什么），控制退出流程（为什么），布尔变量（怎么用）
    while yunxing:  # 主循环（是什么），不断更新和绘制界面（为什么），while判断标志位（怎么用）
        shibiao_x, shibiao_y = pygame.mouse.get_pos()  # 鼠标位置（是什么），获取当前光标坐标（为什么），get_pos获取元组（怎么用）
        dianji = False  # 点击标志（是什么），捕获当前帧是否有左键松开（为什么），每帧初始化为False（怎么用）
        
        for shijian in pygame.event.get():  # 遍历事件（是什么），从事件队列中轮询（为什么），get方法获取（怎么用）
            if shijian.type == pygame.QUIT:  # 退出判定（是什么），捕获右上角红叉（为什么），判断type属性（怎么用）
                yunxing = False  # 结束标志（是什么），跳出循环关闭软件（为什么），赋值为False（怎么用）
            elif shijian.type == pygame.MOUSEBUTTONUP:  # 鼠标抬起（是什么），判断按键交互（为什么），判断type属性（怎么用）
                if shijian.button == 1:  # 左键松开（是什么），确认是左键点击（为什么），判断button值（怎么用）
                    dianji = True  # 点击生效（是什么），设为真触发点击逻辑（为什么），赋值为True（怎么用）
        
        chuangkou.fill((30, 35, 45))  # 清空画布（是什么），填充灰色背景作为底层（为什么），fill传入RGB颜色（怎么用）
        
        # 保护机制：如果未找到任何游戏目录，渲染专门的提示界面
        if not you_xi_mulu:  # 目录检查（是什么），如果没有发现任何以数字开头的游戏文件夹（为什么），判断空值（怎么用）
            pygame.draw.rect(chuangkou, (20, 24, 33), (0, 0, 900, 650))  # 全屏背景（是什么），绘制背景（为什么），draw.rect画大矩形（怎么用）
            error_tu1 = ziti_biaoti.render("Error: No game folders found!", True, (255, 100, 100))  # 渲染错误标题（是什么），提示寻找失败（为什么），render绘制（怎么用）
            error_tu2 = ziti_zhong.render("Please place run_launcher.py in the project root folder.", True, (200, 200, 200))  # 渲染引导语（是什么），告知解决办法（为什么），render绘制（怎么用）
            error_tu3 = ziti_xiao.render(f"Current Path: {gongzuo_mulu}", True, (150, 150, 150))  # 渲染当前路径（是什么），辅助排查定位（为什么），render绘制（怎么用）
            chuangkou.blit(error_tu1, (100, 200))  # 显示错误标题（是什么），定位到窗口中央（为什么），blit贴图（怎么用）
            chuangkou.blit(error_tu2, (100, 245))  # 显示引导语（是什么），定位到标题下方（为什么），blit贴图（怎么用）
            chuangkou.blit(error_tu3, (100, 290))  # 显示当前路径（是什么），定位在下方（为什么），blit贴图（怎么用）
            
            # 渲染作者与网址（底部）
            zuozhe_tu = ziti_xiao.render("作者：程小宝 (xbkjz.cn)", True, (150, 160, 180))  # 渲染作者名（是什么），生成版权文字（为什么），render绘制（怎么用）
            chuangkou.blit(zuozhe_tu, (100, 500))  # 贴图显示（是什么），展示在错误提示下方（为什么），blit贴图（怎么用）
        else:
            pygame.draw.rect(chuangkou, (20, 24, 33), (0, 0, 320, 650))  # 侧边栏（是什么），划分出左侧的深蓝色区域（为什么），draw.rect绘制（怎么用）
            
            biaoti_tu = ziti_biaoti.render("XiaoBao Pygame", True, (0, 180, 255))  # 渲染侧边栏标题（是什么），显示LOGO（为什么），render生成贴图（怎么用）
            chuangkou.blit(biaoti_tu, (20, 25))  # 绘制标题（是什么），将文字画在画布左上角（为什么），blit指定坐标（怎么用）
            pygame.draw.line(chuangkou, (45, 52, 71), (0, 70), (320, 70), 2)  # 分隔线（是什么），区分头部标题与菜单区域（为什么），draw.line绘制（怎么用）
            
            for i, mulu in enumerate(you_xi_mulu):  # 遍历列表（是什么），绘制左侧游戏选项（为什么），enumerate解包索引和文件夹（怎么用）
                item_y = 80 + i * 28  # 计算纵坐标（是什么），根据索引安排每个项目的位置（为什么），基本算术乘法（怎么用）
                xuanting = 10 <= shibiao_x <= 310 and item_y <= shibiao_y <= item_y + 26  # 悬停判断（是什么），判断鼠标是否在此按钮区域内（为什么），与逻辑运算（怎么用）
                
                if i == xuanze_you_xi_index:  # 选中高亮（是什么），若当前索引为已选中（为什么），if条件判断（怎么用）
                    pygame.draw.rect(chuangkou, (0, 120, 215), (10, item_y, 300, 26), border_radius=4)  # 蓝色背景（是什么），视觉凸显选中项（为什么），draw.rect画圆角矩形（怎么用）
                elif xuanting:  # 悬停高亮（是什么），若鼠标划过非选中项（为什么），elif条件判断（怎么用）
                    pygame.draw.rect(chuangkou, (45, 52, 71), (10, item_y, 300, 26), border_radius=4)  # 灰色背景（是什么），提供过渡视觉反馈（为什么），draw.rect画圆角矩形（怎么用）
                    
                if xuanting and dianji:  # 触发点击（是什么），点击该游戏项目（为什么），双重与逻辑校验（怎么用）
                    xuanze_you_xi_index = i  # 更新选中（是什么），切换显示的游戏课时列表（为什么），重新赋值（怎么用）
                    
                wenzi_se = (255, 255, 255) if (i == xuanze_you_xi_index or xuanting) else (180, 190, 200)  # 文字色彩（是什么），选中或悬停时白色，否则淡灰（为什么），三元表达式（怎么用）
                wenzi_tu = ziti_xiao.render(mulu, True, wenzi_se)  # 渲染文字（是什么），生成表面贴图（为什么），render生成（怎么用）
                chuangkou.blit(wenzi_tu, (20, item_y + 4))  # 绘制文字（是什么），画到对应侧边栏纵坐标（为什么），blit绘制（怎么用）
                
            pygame.draw.line(chuangkou, (45, 52, 71), (0, 600), (320, 600), 2)  # 署名分隔线（是什么），区分菜单区和底部署名区（为什么），draw.line绘制（怎么用）
            
            zuozhe_xuanting = 20 <= shibiao_x <= 250 and 610 <= shibiao_y <= 635  # 署名悬停（是什么），判断鼠标是否在作者链接上（为什么），逻辑范围比较（怎么用）
            zuozhe_se = (0, 180, 255) if zuozhe_xuanting else (150, 160, 180)  # 颜色切换（是什么），悬停时变亮蓝色（为什么），三元表达式（怎么用）
            zuozhe_tu = ziti_xiao.render("作者：程小宝 (xbkjz.cn)", True, zuozhe_se)  # 渲染文本（是什么），应用最终颜色（为什么），render绘制（怎么用）
            chuangkou.blit(zuozhe_tu, (20, 615))  # 贴图显示（是什么），展示到左下角（为什么），blit贴图（怎么用）
            
            if zuozhe_xuanting and dianji:  # 网页跳转（是什么），点击作者链接（为什么），与逻辑触发（怎么用）
                import webbrowser  # 导入浏览器模块（是什么），用于打开外部分支链接（为什么），局部导入（怎么用）
                webbrowser.open("http://xbkjz.cn")  # 打开主页（是什么），在默认浏览器加载作者网站（为什么），webbrowser.open跳转（怎么用）
                
            xuanze_mulu = you_xi_mulu[xuanze_you_xi_index]  # 选中目录（是什么），取出当前的文件夹名称（为什么），索引访问（怎么用）
            you_biaoti_tu = ziti_zhong.render(f"当前游戏: {xuanze_mulu}", True, (255, 255, 255))  # 游戏标题（是什么），显示选中的游戏（为什么），render渲染（怎么用）
            chuangkou.blit(you_biaoti_tu, (350, 25))  # 绘制游戏标题（是什么），贴图到右上部（为什么），blit绘制（怎么用）
            pygame.draw.line(chuangkou, (45, 52, 71), (320, 70), (900, 70), 2)  # 分隔线（是什么），区分标题和课时内容（为什么），draw.line绘制（怎么用）
            
            ke_cheng = huo_qu_ke_cheng_wenjian(xuanze_mulu)  # 获取课程（是什么），读取选中文件夹内的所有课时py脚本（为什么），函数调用（怎么用）
            for j, wenjian in enumerate(ke_cheng):  # 遍历课时（是什么），渲染课程按钮列表（为什么），enumerate遍历（怎么用）
                card_y = 90 + j * 75  # 计算卡片Y坐标（是什么），垂直排列每课按钮（为什么），纵向坐标递增（怎么用）
                card_rect = (350, card_y, 510, 62)  # 卡片范围（是什么），宽510高62的矩形参数（为什么），四元组元组定义（怎么用）
                card_xuanting = 350 <= shibiao_x <= 860 and card_y <= shibiao_y <= card_y + 62  # 卡片悬停（是什么），判断鼠标横纵坐标是否在卡片内（为什么），逻辑与运算（怎么用）
                
                if card_xuanting:  # 悬停颜色（是什么），鼠标滑过时（为什么），if分支控制（怎么用）
                    pygame.draw.rect(chuangkou, (45, 55, 75), card_rect, border_radius=6)  # 浅高亮（是什么），提供动感交互（为什么），draw.rect画圆角矩形（怎么用）
                    pygame.draw.rect(chuangkou, (0, 180, 255), card_rect, width=1, border_radius=6)  # 发光边框（是什么），增强立体感（为什么），width=1画线框（怎么用）
                else:  # 默认状态（是什么），鼠标未滑过（为什么），else分支（怎么用）
                    pygame.draw.rect(chuangkou, (35, 42, 57), card_rect, border_radius=6)  # 默认底色（是什么），低调配色（为什么），draw.rect画圆角矩形（怎么用）
                    
                ke_cheng_ming = jie_xi_wenjian(wenjian)  # 解析课程名（是什么），获得友好的显示名称（为什么），传入文件名解析（怎么用）
                card_wenzi = ziti_zhong.render(ke_cheng_ming, True, (255, 255, 255))  # 渲染课名（是什么），白色亮字展示（为什么），render生成Surface（怎么用）
                chuangkou.blit(card_wenzi, (370, card_y + 12))  # 绘制课名（是什么），贴在卡片左侧（为什么），blit放置（怎么用）
                
                card_fubiaoti = ziti_xiao.render(wenjian, True, (150, 160, 180))  # 渲染副标题（是什么），显示真实文件名称（为什么），render小字生成（怎么用）
                chuangkou.blit(card_fubiaoti, (370, card_y + 36))  # 绘制副标题（是什么），贴在卡片左下侧（为什么），blit放置（怎么用）
                
                anniu_yanse = (0, 200, 255) if card_xuanting else (180, 190, 200)  # 运行颜色（是什么），悬停时变亮青色（为什么），三元条件（怎么用）
                anniu_wenzi = ziti_xiao.render("Run >", True, anniu_yanse)  # 渲染按钮（是什么），指示可以启动游戏（为什么），render生成（怎么用）
                chuangkou.blit(anniu_wenzi, (800, card_y + 22))  # 绘制运行（是什么），贴在卡片右侧（为什么），blit贴图（怎么用）
                
                if card_xuanting and dianji:  # 点击启动（是什么），鼠标左键点击卡片（为什么），双重逻辑与（怎么用）
                    wenjian_lujing = os.path.join(gongzuo_mulu, xuanze_mulu, wenjian)  # 获取路径（是什么），拼装该课时脚本的绝对路径（为什么），join拼接（怎么用）
                    try:  # 保护机制（是什么），防止子游戏报错崩溃带垮启动器（为什么），try结构保护（怎么用）
                        subprocess.run([sys.executable, wenjian_lujing])  # 运行游戏（是什么），以当前Python解释器进程启动（为什么），subprocess.run（怎么用）
                    except Exception as cuowu:  # 捕获异常（是什么），接收可能发生的所有错误（为什么），except捕获（怎么用）
                        print(f"Failed to launch: {cuowu}")  # 报错日志（是什么），反馈错误详情（为什么），print打印异常（怎么用）
                    
        pygame.display.flip()  # 刷新画布（是什么），把所有绘制输出到显示屏上（为什么），flip方法调用（怎么用）
        shizhong.tick(60)  # 锁定帧率（是什么），限制游戏运行在60FPS（为什么），tick函数限制（怎么用）
        
    pygame.quit()  # 退出引擎（是什么），清理Pygame占用的系统资源（为什么），程序结束时执行（怎么用）
    sys.exit()  # 退出系统（是什么），完全终止主进程（为什么），sys.exit（怎么用）

if __name__ == "__main__":  # 入口判定（是什么），保证是脚本被直接运行时才执行主逻辑（为什么），__name__标准判断（怎么用）
    zhu_caidan()  # 启动主函数（是什么），进入交互菜单（为什么），无参数直接调用（怎么用）
