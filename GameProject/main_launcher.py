import customtkinter as ctk
import os
import subprocess
import threading
import sys

# ================= 设计规范 =================
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

COLOR_BG_MAIN = "#FFFFFF"
COLOR_BG_SIDEBAR = "#F2F2F7"
COLOR_TEXT_MAIN = "#1D1D1F"
COLOR_TEXT_SUB = "#86868B"
COLOR_ACCENT = "#007AFF"
COLOR_ACCENT_HOVER = "#0051a8"
COLOR_DESC_BG = "#F5F5F7"


# ================= 侧边栏按钮 =================
class SidebarButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.configure(fg_color="#E5E5EA", cursor="hand2")

    def on_leave(self, event):
        self.configure(fg_color="transparent", cursor="arrow")


# ================= 主程序 =================

class GameLauncherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Goat游戏开发小组")
        self.geometry("900x600")
        self.configure(fg_color=COLOR_BG_MAIN)
        self.resizable(True, True)

        self.selected_game_info = None

        self.grid_columnconfigure(0, weight=0, minsize=240)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # === 左侧 Sidebar ===
        self.sidebar = ctk.CTkFrame(self, fg_color=COLOR_BG_SIDEBAR, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(self.sidebar, text="游戏", font=("Helvetica", 22, "bold"),
                     text_color=COLOR_TEXT_MAIN, anchor="w").grid(row=0, column=0, padx=25, pady=(35, 15), sticky="ew")

        self.scroll_frame = ctk.CTkScrollableFrame(self.sidebar, fg_color="transparent")
        self.scroll_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # === 右侧 Main Area ===
        self.main_area = ctk.CTkFrame(self, fg_color=COLOR_BG_MAIN, corner_radius=0)
        self.main_area.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)

        self.main_area.grid_columnconfigure(0, weight=1)
        self.main_area.grid_rowconfigure(1, weight=1)

        self.label_title = ctk.CTkLabel(self.main_area, text="快快选一个游戏吧(◍•ᴗ•◍)❤",
                                        font=("Microsoft YaHei UI", 32, "bold"), text_color=COLOR_TEXT_MAIN, anchor="w")
        self.label_title.grid(row=0, column=0, sticky="w", pady=(0, 20))

        self.desc_frame = ctk.CTkFrame(self.main_area, fg_color=COLOR_DESC_BG, corner_radius=12)
        self.desc_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 30))

        self.desc_text = ctk.CTkTextbox(
            self.desc_frame,
            font=("Microsoft YaHei UI", 16),
            text_color=COLOR_TEXT_MAIN,
            fg_color="transparent",
            wrap="word",
            activate_scrollbars=True
        )
        self.desc_text.pack(padx=20, pady=20, fill="both", expand=True)
        self.desc_text.insert("0.0", "(๑>ᴗ<๑)\n小组成员:\n               陈奕铭 潘禹越 肖胜杰 宋楚龙 曹育贤\n               庄皓扬 曾钰茵 马天宇 李俊浩 薛煜")
        self.desc_text.configure(state="disabled")

        self.btn_start = ctk.CTkButton(
            self.main_area,
            text="Start Game",
            font=("Microsoft YaHei UI", 16, "bold"),
            height=55,
            corner_radius=27,
            fg_color=COLOR_ACCENT,
            hover_color=COLOR_ACCENT_HOVER,
            state="disabled",
            command=self.on_start_game
        )
        self.btn_start.grid(row=2, column=0, sticky="ew")

        self.scan_games()

    def scan_games(self):
        if not os.path.exists("games"):
            self.set_desc("Error: 'games' folder not found!")
            return

        items = os.listdir("games")
        valid_games = []

        for item in items:
            full_path = os.path.join("games", item)

            # 情况 A: 单文件
            if os.path.isfile(full_path) and item.endswith(".py") and item != "__init__.py":
                game_name = item.replace(".py", "").replace("_", " ").title()
                valid_games.append({
                    "name": game_name,
                    "path": full_path,  # 例如: games/snake.py
                    "filename": item,  # 例如: snake.py (新增这个字段，很有用)
                    "is_folder": False
                })

            # 情况 B: 文件夹
            elif os.path.isdir(full_path):
                entry_point = os.path.join(full_path, "main.py")
                if os.path.exists(entry_point):
                    game_name = item.replace("_", " ").title()
                    valid_games.append({
                        "name": game_name,
                        "path": entry_point,  # 例如: games/PvZ/main.py
                        "filename": "main.py",  # 固定是 main.py
                        "is_folder": True,
                        "folder_path": full_path  # 例如: games/PvZ
                    })

        for game in valid_games:
            btn = SidebarButton(
                self.scroll_frame,
                text=game["name"],
                font=("Microsoft YaHei UI", 14),
                fg_color="transparent",
                text_color=COLOR_TEXT_MAIN,
                anchor="w",
                height=45,
                corner_radius=8,
                command=lambda g=game: self.select_game(g)
            )
            btn.pack(fill="x", pady=2)

    def select_game(self, game_info):
        self.selected_game_info = game_info
        self.label_title.configure(text=game_info["name"])
        self.btn_start.configure(state="normal", text="Start Game")

        txt_path = ""
        if game_info["is_folder"]:
            txt_path = os.path.join(game_info["folder_path"], "main.txt")
        else:
            txt_path = game_info["path"].replace(".py", ".txt")

        description = "暂无玩法介绍。\n(No description provided)"
        if os.path.exists(txt_path):
            try:
                with open(txt_path, "r", encoding="utf-8") as f:
                    description = f.read()
            except Exception as e:
                description = f"读取错误: {e}"

        self.set_desc(description)

    def set_desc(self, text):
        self.desc_text.configure(state="normal")
        self.desc_text.delete("0.0", "end")
        self.desc_text.insert("0.0", text)
        self.desc_text.configure(state="disabled")

    def on_start_game(self):
        if not self.selected_game_info:
            return

        self.btn_start.configure(state="disabled", text="Running...")
        threading.Thread(target=self.run_game_thread).start()

    def run_game_thread(self):
        """【最终修正版】完全使用相对路径"""

        # 1. 确定我们要进入哪个文件夹 (cwd)
        # 2. 确定我们在这个文件夹里要运行哪个文件 (script_name)

        target_work_dir = ""
        script_to_run = ""

        if self.selected_game_info["is_folder"]:
            # 如果是文件夹模式
            # 工作目录设为: games/PvZ
            # 运行脚本名为: main.py (只给文件名，不带路径！)
            target_work_dir = self.selected_game_info["folder_path"]
            script_to_run = "main.py"
        else:
            # 如果是单文件模式
            # 工作目录设为: games
            # 运行脚本名为: snake.py
            target_work_dir = "games"
            script_to_run = self.selected_game_info["filename"]

        try:
            # 这里的逻辑是：
            # 1. 告诉 Python: "请进入 target_work_dir 这个房间"
            # 2. 告诉 Python: "运行这个房间桌子上叫 script_to_run 的文件"
            # 这样就不会出现路径重复，而且全程相对路径，老师电脑上也能跑！
            subprocess.run([sys.executable, script_to_run], cwd=target_work_dir, check=False)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.after(0, self.reset_button)

    def reset_button(self):
        self.btn_start.configure(state="normal", text="Start Game")


if __name__ == "__main__":
    app = GameLauncherApp()
    app.mainloop()