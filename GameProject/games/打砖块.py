import tkinter as tk
import random


class BreakoutGame:
    def __init__(self, root):
        self.root = root
        self.root.title("打砖块小游戏")
        self.root.resizable(False, False)

        # 游戏画布
        self.canvas = tk.Canvas(root, width=500, height=400, bg="black")
        self.canvas.pack()

        # 挡板
        self.paddle = self.canvas.create_rectangle(200, 370, 300, 385, fill="white")

        # 小球
        self.ball = self.canvas.create_oval(240, 350, 260, 370, fill="red")

        # 小球移动速度
        self.ball_dx = 3
        self.ball_dy = -3

        # 创建砖块
        self.bricks = []
        self.create_bricks()

        # 挡板移动绑定
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # 游戏循环
        self.update_ball()

    def create_bricks(self):
        """创建砖块"""
        colors = ["#ff4d4d", "#ff944d", "#ffe14d", "#6bff4d", "#4dffe3",
                  "#4da6ff", "#b84dff"]

        for row in range(5):
            for col in range(10):
                x1 = col * 50 + 5
                y1 = row * 25 + 5
                x2 = x1 + 40
                y2 = y1 + 20
                brick = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=colors[row % len(colors)], width=0
                )
                self.bricks.append(brick)

    def move_left(self, event):
        """挡板左移"""
        self.canvas.move(self.paddle, -20, 0)

    def move_right(self, event):
        """挡板右移"""
        self.canvas.move(self.paddle, 20, 0)

    def update_ball(self):
        """更新小球运动"""
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)

        # 撞到左右边界
        if bx1 <= 0 or bx2 >= 500:
            self.ball_dx = -self.ball_dx

        # 撞到顶部
        if by1 <= 0:
            self.ball_dy = -self.ball_dy

        # 撞到挡板
        px1, py1, px2, py2 = self.canvas.coords(self.paddle)
        if by2 >= py1 and bx2 >= px1 and bx1 <= px2:
            self.ball_dy = -abs(self.ball_dy)  # 向上弹

        # 碰到砖块
        hit_list = self.canvas.find_overlapping(bx1, by1, bx2, by2)
        for obj in hit_list:
            if obj in self.bricks:
                self.bricks.remove(obj)
                self.canvas.delete(obj)
                self.ball_dy = -self.ball_dy
                break

        # 掉落到底部（游戏结束）
        if by2 >= 400:
            self.canvas.create_text(
                250, 200,
                text="游戏结束！",
                fill="white",
                font=("Microsoft YaHei", 20)
            )
            return  # 停止游戏循环

        # 下一帧
        self.root.after(16, self.update_ball)  # 约 60 FPS


def start_game():
    root = tk.Tk()
    BreakoutGame(root)
    root.mainloop()


if __name__ == "__main__":
    start_game()
