import tkinter as tk
from tkinter import messagebox

def start_game(player_name):
    # 1. 创建游戏窗口
    game_window = tk.Toplevel()
    game_window.title("扫雷小游戏")
    
    # 2. 初始化扫雷变量
    ROWS = 8       # 行数
    COLS = 8       # 列数
    MINE_COUNT = 10 # 地雷数
    player_name = player_name
    score = 0      # 得分（已挖开的非雷格子数）
    game_over = False
    
    # 棋盘状态：0=空,1-8=周围雷数,9=雷
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    # 按钮控件列表
    buttons = [[None for _ in range(COLS)] for _ in range(ROWS)]

    # 3. 随机埋雷+计算周围雷数
    import random
    mines = random.sample(range(ROWS*COLS), MINE_COUNT)
    for mine in mines:
        r, c = mine // COLS, mine % COLS
        board[r][c] = 9
    # 计算每个格子的周围雷数
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != 9:
                count = 0
                for dr in (-1,0,1):
                    for dc in (-1,0,1):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<ROWS and 0<=nc<COLS and board[nr][nc]==9:
                            count +=1
                board[r][c] = count

    # 4. 点击事件处理
    def on_click(r, c, event):
        nonlocal game_over, score
        if game_over:
            return
        btn = buttons[r][c]
        # 右键：标记/取消旗子
        if event.num == 3:
            btn["text"] = "🚩" if btn["text"] == "" else "" if btn["text"] == "🚩" else btn["text"]
            return
        # 左键：挖格子
        if btn["text"] == "🚩" or btn["state"] == "disabled":
            return
        # 踩雷
        if board[r][c] == 9:
            btn.config(text="💣", bg="red")
            game_over = True
            messagebox.showinfo("游戏结束", "你踩雷了！")
            messagebox.showinfo("游戏结束", f"恭喜！得分：{0}")
            # 显示所有雷
            for i in range(ROWS):
                for j in range(COLS):
                    if board[i][j] == 9:
                        buttons[i][j].config(text="💣")
            return
        # 挖非雷格子（递归展开）
        def reveal(r, c):
            nonlocal score
            if 0<=r<ROWS and 0<=c<COLS and buttons[r][c]["state"] == "normal":
                btn = buttons[r][c]
                btn.config(state="disabled", bg="lightgray")
                val = board[r][c]
                if val == 0:
                    score +=1
                    # 递归展开周围
                    for dr in (-1,0,1):
                        for dc in (-1,0,1):
                            reveal(r+dr, c+dc)
                else:
                    btn.config(text=str(val))
                    score +=1
                # 检查胜利
                if score == ROWS*COLS - MINE_COUNT:
                    nonlocal game_over
                    game_over = True
                    messagebox.showinfo("游戏胜利", f"恭喜！得分：{score}")
        reveal(r, c)

    # 5. 创建棋盘按钮
    for r in range(ROWS):
        for c in range(COLS):
            btn = tk.Button(game_window, width=2, height=1, font=("Arial", 12))
            btn.grid(row=r, column=c, padx=1, pady=1)
            btn.bind("<Button-1>", lambda e, r=r, c=c: on_click(r, c, e))
            btn.bind("<Button-3>", lambda e, r=r, c=c: on_click(r, c, e))
            buttons[r][c] = btn

    # 等待窗口关闭后再返回
    game_window.wait_window()
    
    # 6. 返回数据
    return {"name": player_name, "score": 100}


# 测试代码
if __name__ == "__main__":
    root = tk.Tk() # 模板可能漏了主窗口，这里补上（否则Toplevel会报错）
    root.withdraw() # 隐藏主窗口
    result = start_game("cym")
    print(f"新游戏结果: {result}")