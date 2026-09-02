# Contributing to XiaoBao-Pygame / 参与项目贡献

We are thrilled that you want to contribute to the Pygame Educational Curriculum! This project aims to make programming accessible, highly visual, and logically sound for beginners and educators.

我们非常高兴您有兴趣为本项目贡献力量！本项目的目标是为编程初学者及少儿教师提供极简、易懂且充满趣味性的游戏教案。

---

## Code of Style / 代码规范指南

Because this is a teaching repository, consistency is our highest priority. **All code submissions MUST follow our five core laws**:

由于本项目属于教学课程仓库，代码一致性是重中之重。**所有提交的代码必须严格遵守以下五大核心法则**：

### 1. Pure Chinese Variable Naming / 函数与变量名全中文化
- **Rule / 规则**: All custom variables and function names must be written in Chinese characters (Python 3 UTF-8 native support).
- **Reason / 原因**: Completely removes English vocabulary anxiety for young learners and beginners, making code read as naturally as a sentence.
- **Example / 示例**:
  ```python
  得分 = 0
  飞船速度 = 5
  def 重置游戏():
  ```

### 2. Column-Aligned Inline Comments / 精准列对齐行尾注释
- **Rule / 规则**:
  - Comments must be inline `#` placed at the end of the line and column-aligned vertically around column 50–55 using spaces.
  - Omit redundant comments on obvious lines (imports, `pygame.init()`, trivial 0-assignments). Reserve comments for math, coordinates, collision logic, and Pygame mechanics.
- **Reason / 原因**: Keeps clean code on the left and orderly explanation on the right, eliminating screen clutter.

### 3. Lesson Controls & Progressive Structure / 课时控制与渐进结构
- **Rule / 规则**:
  - No rigid line-count limits. Priority is placed on clean, self-explanatory logic rather than artificially compressing multiple statements.
  - Each game must contain **3 to 5 lessons** demonstrating incremental feature evolution.
- **Reason / 原因**: Guarantees manageable scope while keeping students engaged and excited to finish a full game.

### 4. Zero External Assets & Default Fonts / 零外部素材与默认字体
- **Rule / 规则**:
  - Only draw vector shapes (`pygame.draw.circle`, `pygame.draw.rect`, etc.). Do not load `.png`, `.wav`, or other external assets to prevent file-path errors.
  - Strictly use built-in default font `pygame.font.Font(None, 36)`. Never use `SysFont` or load `.ttf` files. All rendered on-screen text must use standard English (e.g. `SCORE`, `GAME OVER`, `YOU WIN!`).
- **Reason / 原因**: Complete cross-platform reliability without missing font or asset path crashes.

### 5. Incremental Progression / 增量行尾标注
- **Rule / 规则**: Mark code modifications relative to the previous lesson at the end of the line:
  - `# 新增变量：` (New variable)
  - `# 新增函数：` (New function)
  - `# 新增代码：` (New code)

---

## Workflow / 贡献流程

1. **Fork the Repository** to your own GitHub account.
   将项目 **Fork** 到您的 GitHub 账户。
2. **Create a Feature Branch** from the `main` branch.
   从 `main` 分支创建您的 **开发分支** (e.g. `git checkout -b feature/new-game-flappy-bird`)。
3. **Commit your changes** ensuring that the code compiles perfectly (`python -m py_compile ...`).
   **提交您的更改**，并确保所有新增代码均符合编写法则并通过编译验证。
4. **Test execution**: Make sure the game works and can be scanned by running `python run_launcher.py`.
   **运行测试**：通过执行 `python run_launcher.py` 验证游戏可以正常加载并流畅执行。
5. **Open a Pull Request** with a detailed explanation of your game curriculum design.
   **新建 Pull Request (PR)** 并详细描述您所设计的游戏教学要点。

Thank you for helping teachers and students make their coding journey fun!
感谢您对编程教育事业做出的宝贵贡献！
