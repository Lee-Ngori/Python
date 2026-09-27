import tkinter as tk
import random


def start_game(player_name):
    # 确保有根窗口
    if not tk._default_root:
        root = tk.Tk()
        root.withdraw()  # 隐藏根窗口

    window = tk.Toplevel()
    window.title("极限挑战")
    window.geometry("250x150")

    score = 0
    time_visible = 1500
    target = None
    started = False
    timer_id = None

    def create_target():
        nonlocal target, timer_id
        if target: target.destroy()
        if timer_id: window.after_cancel(timer_id)
        target = tk.Button(window, text="颗秒", command=click, bg="red", fg="white")
        target.place(x=random.randint(20, 150), y=random.randint(20, 80))
        if started:
            timer_id = window.after(time_visible, lambda: target.destroy() or game_over())

    def click():
        nonlocal score, time_visible, started
        if not started: started = True
        score += 1
        if score >= 66:
            tk.Label(window, text="棒棒棒棒棒", fg="gold").place(relx=0.5, rely=0.5, anchor="center")
            window.after(1000, window.destroy)
            return
        time_visible = max(100, time_visible - 20)
        create_target()

    def game_over():
        tk.Label(window, text="难道他真的是赋能哥", fg="red").place(relx=0.5, rely=0.5, anchor="center")
        window.after(1000, window.destroy)

    create_target()
    window.wait_window()
    return {"name": player_name, "score": min(score, 66)}


if __name__ == "__main__":
    result = start_game("cym")
    print(f"游戏结束！结果: {result}")