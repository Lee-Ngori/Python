import tkinter as tk
from tkinter import messagebox
from typing import Dict, Any

# ==============================================================================
# 全局常量
# ==============================================================================

BOARD_SIZE = 3
EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

# 定义个性化玩家名称
PLAYER_X_NAME = "勒布朗詹姆斯" # 玩家 (X)
PLAYER_O_NAME = "科比"         # 对手 (O)

# 定义尺寸 (放大后的尺寸)
BASE_FONT_SIZE = 20

class TicTacToe:
    
    def __init__(self, master: tk.Toplevel, player_name: str, on_game_end):
        self.master = master
        self.master.title("井字棋 (勒布朗 vs 科比)")
        
        self.player_name_for_return = player_name
        self.on_game_end = on_game_end
        
        self.board = [EMPTY] * (BOARD_SIZE * BOARD_SIZE)
        self.current_player = PLAYER_X 
        self.game_over = False
        self.score = 0 
        
        self.buttons: Dict[int, tk.Button] = {}
        
        # 1. 游戏界面居中逻辑 (修复：窗口尺寸增大到 650x750)
        window_width = 850
        window_height = 950  # 再次增大高度和宽度，确保完整显示
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.master.lift()
        
        # GUI 元素 (文字放大)
        self.status_label = tk.Label(master, text=f"{PLAYER_X_NAME} (X) 的回合", font=('Arial', BASE_FONT_SIZE))
        self.status_label.pack(pady=40) # 增大 pady 确保标签和棋盘有足够间距
        
        self.create_board_ui()
        
    def create_board_ui(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        
        # 按钮尺寸适配文字 (使用放大后的尺寸)
        btn_width = 7 # 增大按钮宽度
        btn_height = 4 # 增大按钮高度
        
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                index = i * BOARD_SIZE + j
                button = tk.Button(
                    self.frame, 
                    text=EMPTY, 
                    font=('Arial', BASE_FONT_SIZE + 10, 'bold'), # 棋盘文字更大
                    width=btn_width, 
                    height=btn_height,
                    command=lambda idx=index: self.handle_click(idx),
                    compound=tk.NONE
                )
                # 增大 padx/pady 确保格子间距
                button.grid(row=i, column=j, padx=15, pady=15) # 进一步增大间距
                self.buttons[index] = button

    def handle_click(self, index: int):
        if self.game_over or self.board[index] != EMPTY:
            return 
        
        self.board[index] = self.current_player
        
        self.buttons[index].config(text=self.current_player, disabledforeground='black')
        
        self.buttons[index].config(state=tk.DISABLED) 
        
        winner = self.check_winner()
        if winner:
            self.end_game(winner)
        elif EMPTY not in self.board:
            self.end_game(None) 
        else:
            self.switch_player()

    def switch_player(self):
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
        player_turn_name = PLAYER_X_NAME if self.current_player == PLAYER_X else PLAYER_O_NAME
        self.status_label.config(text=f"{player_turn_name} ({self.current_player}) 的回合")

    def check_winner(self) -> str | None:
        
        for i in range(BOARD_SIZE):
            row_start = i * BOARD_SIZE
            if self.board[row_start] == self.board[row_start+1] == self.board[row_start+2] != EMPTY:
                return self.board[row_start]
        
        for j in range(BOARD_SIZE):
            if self.board[j] == self.board[j+BOARD_SIZE] == self.board[j+2*BOARD_SIZE] != EMPTY:
                return self.board[j]
        
        if self.board[0] == self.board[4] == self.board[8] != EMPTY: 
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != EMPTY: 
            return self.board[2]
            
        return None

    def end_game(self, winner: str | None):
        self.game_over = True
        
        if winner == PLAYER_X:
            custom_message = "你赢了，詹姆斯历史第一"
            messagebox.showinfo("游戏结束", f"恭喜！{PLAYER_X_NAME} 获胜！\n\n{custom_message}")
            self.score = 100 
            self.status_label.config(text=f"游戏结束: {PLAYER_X_NAME} 获胜！")
        elif winner == PLAYER_O:
            custom_message = "你输了，但詹姆斯依然历史第一"
            messagebox.showinfo("游戏结束", f"很遗憾！{PLAYER_O_NAME} 获胜！\n\n{custom_message}")
            self.score = 20 
            self.status_label.config(text=f"游戏结束: {PLAYER_O_NAME} 获胜！")
        else:
            messagebox.showinfo("游戏结束", "平局！")
            self.score = 50 
            self.status_label.config(text="游戏结束: 平局！")
            
        for button in self.buttons.values():
            button.config(state=tk.DISABLED)
            
        self.master.protocol("WM_DELETE_WINDOW", lambda: self.close_window_and_return())
        
        self.end_button = tk.Button(self.master, text="确定/返回主页", command=self.close_window_and_return, font=('Arial', BASE_FONT_SIZE - 4))
        self.end_button.pack(pady=40) # 增大 pady 确保按钮不紧贴底部

    def close_window_and_return(self):
        self.master.destroy() 
        self.on_game_end({"name": self.player_name_for_return, "score": self.score})

# ==============================================================================
# 接口函数
# ==============================================================================

def start_game(player_name: str = "玩家1") -> Dict[str, Any]:
    
    game_window = tk.Toplevel()
    
    game_result: Dict[str, Any] = {}
    
    def set_result_and_quit(result: Dict[str, Any]):
        nonlocal game_result
        game_result = result

    game = TicTacToe(game_window, player_name, set_result_and_quit)

    try:
        root = tk.Tk()
        root.withdraw() 
        game_window.mainloop() 
    except tk.TclError:
        pass

    if game_result:
        return {
            "name": game_result["name"], 
            "score": int(game_result["score"]) 
        }
    else:
        return {"name": player_name, "score": 0}

# ==============================================================================
# 测试代码
# ==============================================================================

if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("主程序/测试窗口")
    
    # 主测试窗口居中逻辑
    window_width = 850
    window_height = 450
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    player_name = PLAYER_X_NAME 
    
    def run_game():
        result = start_game(player_name)
        
        print("--- 游戏接口返回结果 ---")
        print(f"玩家名字: {result['name']}")
        print(f"游戏得分: {result['score']}")
        print("------------------------")
        messagebox.showinfo("接口结果", f"游戏已结束，返回结果：\nName: {result['name']}\nScore: {result['score']}")

    # 提示语文字放大
    tk.Label(root, text="点击下方按钮打开詹姆斯大战科比（井字棋版）", font=('Arial', BASE_FONT_SIZE + 4)).pack(pady=40)
    
    tk.Button(root, text="启动井字棋游戏", command=run_game, font=('Arial', BASE_FONT_SIZE)).pack(pady=10)
    
    root.mainloop()