# Contributing to XiaoBao-Pygame / 参与项目贡献

We are thrilled that you want to contribute to the Pygame Educational Curriculum! This project aims to make programming accessible, highly visual, and logically sound for beginners. 

我们非常高兴您有兴趣为本项目贡献力量！本项目的目标是为编程初学及教学提供极简、易懂且充满趣味性的游戏教案。

---

## Code of Style / 代码规范指南

Because this is a teaching repository, consistency is our highest priority. **All code submissions MUST follow our five core laws**:

由于本项目属于教学课程仓库，代码一致性是重中之重。**所有提交的代码必须严格遵守以下五大法则**：

### 1. Pinyin Variable Naming / 变量命名全拼音化
- **Rule / 规则**: All variables, functions, and parameters must be written in Chinese Pinyin.
- **Reason / 原因**: Lowering English anxiety for young learners.
- **Example / 示例**:
  ```python
  shuzu = []             # Array / 数组
  feichuan_sudu = 5      # Spaceship speed / 飞船移动速度
  ```

### 2. "Three-in-One" Comments / “三位一体”逐行注释
- **Rule / 规则**: Every non-blank line of code must be commented. The comment must include:
  `What it is (Function) + Why it is there (Principle) + How to use it (Arguments/Usage)`.
- **Reason / 原因**: Maximizing micro-comprehension for self-learners.
- **Example / 示例**:
  ```python
  pygame.draw.circle(chuangkou, (0, 150, 255), qp, 20, 2)  # 绘图（是什么），蓝色空心圆（为什么），参数含位置半径及边框宽度（怎么用）
  ```

### 3. File & Lesson Constraints / 严格的行数与课时数
- **Rule / 规则**:
  - Each lesson's source code should not exceed **30-40 lines** of logical code (excluding comments and whitespace).
  - Each game must contain **3 to 5 lessons** demonstrating incremental feature evolution.
- **Reason / 原因**: Ensuring small, digestible milestones that fit in a standard 45-minute lesson.

### 4. Zero External Assets / 零外部素材原则
- **Rule / 规则**: Only draw vector shapes (`pygame.draw.circle`, `pygame.draw.rect`, etc.). Do not load `.png`, `.wav`, or other external assets.
- **Reason / 原因**: Eliminating local path error reports when teachers or students open scripts across various operating systems.

### 5. Incremental Progression / 增量标注
- **Rule / 规则**: Mark code modifications relative to the previous lesson with distinct comments:
  - `# 新增变量：` (New variable)
  - `# 新增函数：` (New function)
  - `# 新增代码：` (New code)

---

## Workflow / 贡献流程

1. **Fork the Repository** to your own GitHub account.
   将项目 **Fork** 到您的 GitHub 账户。
2. **Create a Feature Branch** from the `main` branch.
   从 `main` 分支创建您的 **开发分支** (e.g. `git checkout -b feature/new-game-flappy-bird`)。
3. **Commit your changes** ensuring that the code compiles perfectly.
   **提交您的更改**，并确保所有新增代码均符合编写法则。
4. **Test execution**: Make sure the game works and can be scanned by running `python run_launcher.py`.
   **运行测试**：通过执行 `python run_launcher.py` 验证游戏可以正常加载并流畅执行。
5. **Open a Pull Request** with a detailed explanation of your game curriculum design.
   **新建 Pull Request (PR)** 并详细描述您所设计的游戏教学要点。

Thank you for helping teachers and students make their coding journey fun!
感谢您对编程教育事业做出的宝贵贡献！
