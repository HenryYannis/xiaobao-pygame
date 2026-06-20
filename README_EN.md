# XiaoBao-Pygame | Python Game Series Curriculum (Teacher & Educator Edition)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![Library Dependency](https://img.shields.io/badge/dependency-Pygame-green.svg)](https://www.pygame.org/)
[![Curriculum Complexity](https://img.shields.io/badge/Curriculum-18%20Games%20%2F%2069%20Lessons-orange.svg)](#curriculum-syllabus-difficulty-ladder)

This repository is designed specifically for **programming beginners** and **K-12 educators**. It contains an educational curriculum based on the **Pygame** engine. The curriculum includes **18 classic games** of varying difficulty levels, split across **69 step-by-step, progressive lessons**. It is designed to teach students logical thinking and coordinate-based math concepts through interactive, playful examples.

---

## 🎨 Pedagogical Coding Rules (The 5 Core Laws)

To ensure that the code is completely beginner-friendly and readable, all files in this repository strictly adhere to the following **five core laws**:

1. **Pinyin Variable Naming**: All variable and function names are written in Chinese Pinyin (e.g., `feichuan_sudu = 5` for "spaceship speed"). This eliminates English vocabulary barriers for native Chinese-speaking children and allows them to focus purely on coding logic.
2. **"Three-in-One" Inline Comments**: **Every single line** of code features a comprehensive comment detailing: **What** the line is (Function) + **Why** it is there (Principle) + **How** to use it (Key parameters).
3. **Strict Constraints (40 lines / 3-5 lessons)**: Each lesson is restricted to **30-40 lines** of logical code (excluding comments and blank lines). Each game is built within **3 to 5 lessons** so that students complete games quickly, preventing learning fatigue and keeping motivation high.
4. **Zero External Assets**: All visual rendering is done using Pygame's vector drawing methods (`pygame.draw.circle`, `pygame.draw.rect`, etc.). No external image or audio files are loaded. This prevents common path/directory errors, allowing students to focus 100% on the core algorithms.
5. **Incremental Diff Marking**: Whenever code is added to a new lesson compared to the previous one, it is preceded by specific markers: `# 新增变量：` (new variables), `# 新增函数：` (new functions), or `# 新增代码：` (new code).

---

## 🧭 Curriculum Syllabus (Difficulty Ladder)

The syllabus scales gradually from single click event checks to complex multi-body collision detection, finite state machines (FSM), and polar coordinate mechanics:

| Difficulty | Index | Game Title | Lessons | Core Pedagogical Concepts |
| :--- | :---: | :--- | :---: | :--- |
| **Beginner** | 01 | [Click & Pop](./01-点击消除/) | 3 Lessons | Click coordinate checks, random object positioning, basic list management |
| **Beginner** | 02 | [Whack-A-Mole](./02-打地鼠/) | 3 Lessons | Mouse coordinates, time controls, randomized state machines |
| **Beginner** | 03 | [Paddle Ball](./03-弹跳球接球/) | 3 Lessons | Elastic physical rebounds, keyboard movement, bounding box intersection |
| 🟩 **Elementary** | 04 | [Fruit Slasher](./04-水果切切乐/) | 3 Lessons | Slide-trace vector calculations, fruit gravity launch mechanics |
| 🟩 **Elementary** | 05 | [Color Matcher](./05-颜色匹配/) | 3 Lessons | Random color generation, logic matching checks, combo timer systems |
| 🟩 **Elementary** | 06 | [Pixel Painter](./06-像素画家/) | 3 Lessons | 2D coordinate grid creation, mouse brush canvas drawing, color palettes |
| 🟩 **Elementary** | 07 | [Tic-Tac-Toe](./07-井字棋对战/) | 3 Lessons | 2D list state matrix, grid-to-coordinate mapping, win-scan algorithms |
| 🟦 **Intermediate**| 08 | [Brick Breaker](./08-打砖块/) | 5 Lessons | 2D brick array grid, angle deflection reflection, multi-object collision |
| 🟦 **Intermediate**| 09 | [Catch the Fruits](./09-接水果/) | 5 Lessons | Keyboard bounds check, multi-object speed, scoring systems |
| 🟦 **Intermediate**| 10 | [Dino Runner](./10-小恐龙跳一跳/) | 3 Lessons | Basic gravity jumps, floor boundary checks, dynamic cactus generation |
| 🟦 **Intermediate**| 11 | [Snake](./11-贪吃蛇/) | 5 Lessons | Head-insertion & tail-deletion queue, turning buffers, growth logic |
| 🟪 **Advanced** | 12 | [Beat Block](./12-节奏方块/) | 4 Lessons | Scrolling tracks, rhythmic hit window checks, combo scoring systems |
| 🟪 **Advanced** | 13 | [Maze Runner](./13-迷宫逃脱/) | 5 Lessons | 2D grid map coordinates, wall bounding-box blocking, countdown timers |
| 🟪 **Advanced** | 14 | [Simon Memory](./14-颜色记忆大师/) | 5 Lessons | Automated sequence playback, click state queueing, list matches |
| 🟥 **Master** | 15 | [Flappy Bird](./15-横版飞行避障/) | 3 Lessons | Flappy jump velocity, horizontal obstacles scrolling, screen pass checks |
| 🟥 **Master** | 16 | [Space Invaders](./16-太空射击/) | 5 Lessons | Laser spawning & garbage collection, group collision checks, stars scrolling |
| 🟥 **Master** | 17 | [Slider Puzzle](./17-数字拼图/) | 3 Lessons | Inversion numbers checking for solvable states, grid array swap logic |
| 🟥 **Master** | 18 | [Gold Miner](./18-黄金矿工/) | 5 Lessons | Trigonometric rotation (sin/cos), claw animation vectors, weight-based pull |

---

## 🚀 Quick Start

### 1. Prerequisites & Environment Setup
Make sure you have **Python 3.12 or higher** installed on your system.
Open your terminal and run the following command to install **Pygame**:

```bash
pip install -r requirements.txt
```

### 2. Interactive Graphical Launcher (Highly Recommended)
To run lessons easily and visually browse the games, we have developed a beautiful **GUI Launcher** using **Pygame**. Run the following command in the project root to launch:

```bash
python run_launcher.py
```

Key features of the GUI Launcher:
* **Sleek Dark Theme**: Supports smooth mouse hover transitions, glowing button borders, and selected state coloring.
* **Two-Column Layout**: Left side lists the 18 games. Right side displays responsive lesson cards with clean formatted titles (e.g., `Lesson 1 - 气泡浮现`) and the corresponding source file name.
* **Instant Website Redirect**: Click the author credits and link in the bottom-left corner to automatically load the website in your browser.


---

## 🛠️ Contributing

We welcome contributions from educators, students, and game developers!

1. **Review Guidelines**: Before submitting a Pull Request (PR), please read [CONTRIBUTING.md](./CONTRIBUTING.md) to ensure your code follows the naming conventions and comment structures (Pinyin naming, three-in-one inline comments).
2. **Behavioral Code**: Please review and adhere to [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

---

## 📄 License

This repository is licensed under the **[MIT License](./LICENSE)**. You are free to use it for personal learning, teacher training, school lessons, or commercial bootcamps.

---

## 👨‍💻 About the Author

* **Author**: Cheng Xiaobao (程小宝)
* **Official Website**: [xbkjz.cn](http://xbkjz.cn)
* **GitHub Profile**: [@HenryYannis](https://github.com/HenryYannis)

