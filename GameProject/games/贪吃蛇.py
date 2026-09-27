import tkinter as tk
import random
from tkinter import messagebox

def start_game(player_name):
    """
    游戏接口函数 - 必须用这个函数名！
    返回格式: {"name": "玩家名字", "score": 整数分数}
    """
    # 1. 创建游戏窗口（必须用TopLevel）
    game_window = tk.Toplevel()
    game_window.title("贪吃蛇游戏")
    game_window.resizable(False, False)

    # 游戏参数配置
    CELL_SIZE = 20
    GRID_WIDTH = 25
    GRID_HEIGHT = 20
    SPEED = 150

    # 颜色配置
    BG_COLOR = "#1a1a1a"
    SNAKE_COLOR = "#00ff00"
    FOOD_COLOR = "#ff0000"
    TEXT_COLOR = "#ffffff"

    # 创建画布
    canvas = tk.Canvas(
        game_window,
        width=CELL_SIZE * GRID_WIDTH,
        height=CELL_SIZE * GRID_HEIGHT,
        bg=BG_COLOR,
        highlightthickness=0
    )
    canvas.pack()

    # 初始化游戏状态
    score = 0
    player_name = player_name
    direction = "Right"
    next_direction = direction
    snake = []
    food = None

    # 创建初始蛇身
    def create_snake():
        start_x = GRID_WIDTH // 4
        start_y = GRID_HEIGHT // 2
        for i in range(3):
            x = start_x - i
            y = start_y
            snake.append((x, y))
            canvas.create_rectangle(
                x * CELL_SIZE,
                y * CELL_SIZE,
                (x + 1) * CELL_SIZE - 1,
                (y + 1) * CELL_SIZE - 1,
                fill=SNAKE_COLOR,
                tag="snake"
            )

    # 生成食物
    def spawn_food():
        nonlocal food
        if food:
            canvas.delete("food")
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake:
                food = (x, y)
                break
        canvas.create_oval(
            x * CELL_SIZE + 2,
            y * CELL_SIZE + 2,
            (x + 1) * CELL_SIZE - 3,
            (y + 1) * CELL_SIZE - 3,
            fill=FOOD_COLOR,
            tag="food"
        )

    # 绘制分数
    def draw_score():
        canvas.delete("score")
        canvas.create_text(
            10, 10,
            text=f"分数: {score}",
            fill=TEXT_COLOR,
            anchor="nw",
            tag="score",
            font=("Arial", 12)
        )

    # 处理键盘事件
    def on_key_press(event):
        nonlocal next_direction
        key = event.keysym
        if key == "Up" and direction != "Down":
            next_direction = "Up"
        elif key == "Down" and direction != "Up":
            next_direction = "Down"
        elif key == "Left" and direction != "Right":
            next_direction = "Left"
        elif key == "Right" and direction != "Left":
            next_direction = "Right"

    # 移动蛇
    def move_snake():
        nonlocal score, direction
        direction = next_direction
        head_x, head_y = snake[0]
        if direction == "Up":
            new_head = (head_x, head_y - 1)
        elif direction == "Down":
            new_head = (head_x, head_y + 1)
        elif direction == "Left":
            new_head = (head_x - 1, head_y)
        else:
            new_head = (head_x + 1, head_y)
        snake.insert(0, new_head)
        canvas.create_rectangle(
            new_head[0] * CELL_SIZE,
            new_head[1] * CELL_SIZE,
            (new_head[0] + 1) * CELL_SIZE - 1,
            (new_head[1] + 1) * CELL_SIZE - 1,
            fill=SNAKE_COLOR,
            tag="snake"
        )
        if new_head == food:
            score += 10
            draw_score()
            spawn_food()
        else:
            tail = snake.pop()
            canvas.delete(canvas.find_closest(
                tail[0] * CELL_SIZE + CELL_SIZE//2,
                tail[1] * CELL_SIZE + CELL_SIZE//2
            ))

    # 检查碰撞
    def check_collision():
        head_x, head_y = snake[0]
        if (head_x < 0 or head_x >= GRID_WIDTH or
            head_y < 0 or head_y >= GRID_HEIGHT or
            (head_x, head_y) in snake[1:]):
            return True
        return False

    # 游戏结束
    def game_over():
        canvas.delete("all")
        canvas.create_text(
            CELL_SIZE * GRID_WIDTH // 2,
            CELL_SIZE * GRID_HEIGHT // 2 - 30,
            text="游戏结束!",
            fill=TEXT_COLOR,
            font=("Arial", 24, "bold"),
            tag="game_over"
        )
        canvas.create_text(
            CELL_SIZE * GRID_WIDTH // 2,
            CELL_SIZE * GRID_HEIGHT // 2 + 10,
            text=f"最终分数: {score}",
            fill=TEXT_COLOR,
            font=("Arial", 18),
            tag="game_over"
        )
        game_window.unbind("<KeyPress>")
        game_window.after(1000, lambda: game_window.destroy())

    # 游戏主循环
    def game_loop():
        if not check_collision():
            move_snake()
            game_window.after(SPEED, game_loop)
        else:
            game_over()

    # 初始化游戏
    create_snake()
    spawn_food()
    draw_score()
    game_window.bind("<KeyPress>", on_key_press)
    game_loop()

    # 等待游戏窗口关闭后返回结果
    game_window.wait_window()
    return {"name": player_name, "score": score}

# 测试代码
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    result = start_game("cym")
    print(f"游戏结果: {result}")
    root.destroy()