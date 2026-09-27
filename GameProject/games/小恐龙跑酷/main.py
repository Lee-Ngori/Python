import tkinter as tk
import random


class DinoGame:
    def __init__(self, root,on_game_over_callback=None):
        self.root = root
        self.root.title("Chrome Dino Game")
        self.root.geometry("800x400")
        self.root.resizable(False, False)
        self.on_game_over_callback = on_game_over_callback

        # 游戏变量
        self.game_speed =12
        self.score = 0
        self.is_jumping = False
        self.jump_velocity = 0
        self.gravity = 1.2
        self.jump_strength = -15
        self.dino_y = 300
        self.dino_height = 50  # 恐龙的正常高度
        self.is_game_over = False
        self.game_started = False
        self.is_fast_falling = False
        self.fast_fall_gravity = 4.5
        self.is_ducking = False  # 下蹲状态
        self.duck_height = 25  # 下蹲时的高度
        self.auto_duck_on_landing = False  # 标记是否需要在落地时自动下蹲

        # 动画相关变量
        self.animation_counter = 0
        self.animation_speed = 3  # 数值越小动画越快
        self.current_run_frame = 0
        self.current_duck_frame = 0

        # 失败动画相关变量
        self.dead_animation_started = False
        self.dead_animation_counter = 0
        self.dino_dead_img = None

        # 障碍物相关变量
        self.obstacles = []
        self.obstacle_types = []  # 记录障碍物类型
        self.obstacle_speed = self.game_speed
        self.pterodactyl_chance = 0.1  # 翼龙出现的概率

        # 仙人掌图片
        self.cactus_imgs = []
        self.cactus_widths = []  # 存储每种仙人掌的宽度
        self.cactus_heights = []  # 存储每种仙人掌的高度

        # 翼龙图片和动画变量
        self.ptera_imgs = []
        self.ptera_widths = []  # 存储翼龙的宽度
        self.ptera_heights = []  # 存储翼龙的高度
        self.ptera_animation_counter = 0
        self.ptera_animation_speed = 5  # 翼龙动画速度

        # 创建画布
        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack()

        # 加载恐龙图片
        self.use_images = False
        self.dino_run_imgs = []
        self.dino_duck_imgs = []

        try:
            # 尝试加载跑步动画图片
            self.dino_run_imgs.append(tk.PhotoImage(file=r'跑步1_小.png'))
            self.dino_run_imgs.append(tk.PhotoImage(file=r'跑步2_副本.png'))

            # 尝试加载下蹲动画图片
            self.dino_duck_imgs.append(tk.PhotoImage(file=r"趴下1_副本确定1.png"))
            self.dino_duck_imgs.append(tk.PhotoImage(file=r"趴下2_副本1.png"))

            # 尝试加载失败图片
            self.dino_dead_img = tk.PhotoImage(file=r"失败的小恐龙_副本.png")

            # 尝试加载仙人掌图片
            self.cactus_imgs.append(tk.PhotoImage(file=r"仙人掌1_副本.png"))
            self.cactus_imgs.append(tk.PhotoImage(file=r"仙人掌2_副本.png"))
            self.cactus_imgs.append(tk.PhotoImage(file=r"仙人掌3_副本.png"))

            # 尝试加载翼龙图片
            self.ptera_imgs.append(tk.PhotoImage(file=r"翼龙上飞_副本.png"))
            self.ptera_imgs.append(tk.PhotoImage(file=r"翼龙下飞_副本.png"))

            # 记录每种仙人掌的宽度和高度（用于碰撞检测）
            for img in self.cactus_imgs:
                self.cactus_widths.append(img.width())
                self.cactus_heights.append(img.height())

            # 记录翼龙的宽度和高度
            for img in self.ptera_imgs:
                self.ptera_widths.append(img.width())
                self.ptera_heights.append(img.height())

            self.use_images = True
            print("成功加载恐龙、仙人掌和翼龙图片")
        except Exception as e:
            # 如果图片加载失败，使用矩形代替
            print(f"无法加载图片: {e}，使用矩形代替")
            self.use_images = False

        # 创建恐龙
        if self.use_images:
            # 使用图片创建恐龙
            self.dino = self.canvas.create_image(65, self.dino_y + self.dino_height // 2,
                                                 image=self.dino_run_imgs[0], anchor=tk.CENTER)
        else:
            # 使用矩形创建恐龙
            self.dino = self.canvas.create_rectangle(50, self.dino_y, 80, self.dino_y + self.dino_height, fill="gray")

        # 创建地面
        self.ground = self.canvas.create_line(0, 350, 800, 350, fill="black", width=2)

        # 分数显示
        self.score_text = self.canvas.create_text(700, 20, text=f"Score: {self.score}", font=("Arial", 16))

        # 游戏开始提示
        self.start_text = self.canvas.create_text(400, 200,
                                                  text="点击鼠标开始游戏\n按向下键下蹲或快速下落",
                                                  font=("Arial", 16))

        # 绑定按键事件
        self.root.bind("<space>", self.start_game)
        self.root.bind("<KeyPress>", self.key_press)
        self.root.bind("<KeyRelease>", self.key_release)
        self.root.focus_set()

        # 绑定鼠标点击事件
        self.canvas.bind("<Button-1>", self.mouse_click)

        # 游戏循环
        self.update_game()

    def start_game(self, event=None):
        if not self.game_started:
            self.canvas.delete(self.start_text)
            self.game_started = True
            # 游戏开始时生成第一个障碍物
            self.generate_obstacle()
        elif self.is_game_over:
            self.reset_game()

    def mouse_click(self, event):
        if not self.game_started:
            self.start_game()
        elif self.game_started and not self.is_game_over and not self.is_ducking:
            self.initiate_jump()
        elif self.is_game_over:
            self.reset_game()

    def reset_game(self):
        self.canvas.delete("game_over")
        self.score = 0
        self.game_speed = 8
        self.is_game_over = False
        self.is_jumping = False
        self.jump_velocity = 0
        self.dino_y = 300
        self.is_fast_falling = False
        self.is_ducking = False
        self.auto_duck_on_landing = False
        self.pterodactyl_chance = 0.3
        self.animation_counter = 0
        self.current_run_frame = 0
        self.current_duck_frame = 0
        self.dead_animation_started = False
        self.dead_animation_counter = 0
        self.ptera_animation_counter = 0

        # 重置恐龙位置和大小
        if self.use_images:
            self.canvas.coords(self.dino, 65, self.dino_y + self.dino_height // 2)
            self.canvas.itemconfig(self.dino, image=self.dino_run_imgs[0])
        else:
            self.canvas.coords(self.dino, 50, self.dino_y, 80, self.dino_y + self.dino_height)

        # 清除所有障碍物
        for obstacle in self.obstacles:
            self.canvas.delete(obstacle)
        self.obstacles = []
        self.obstacle_types = []

        # 更新分数显示
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

        # 游戏重置后生成第一个障碍物
        self.generate_obstacle()

    def key_press(self, event):
        # 空格键或上键都可以使恐龙跳跃
        if (
                event.keysym == "space" or event.keysym == "Up") and not self.is_jumping and not self.is_game_over and self.game_started and not self.is_ducking:
            self.initiate_jump()
        elif event.keysym == "Down" and not self.is_game_over and self.game_started:
            if self.is_jumping:
                # 如果在空中，开启快速下落并标记落地后自动下蹲
                self.is_fast_falling = True
                self.auto_duck_on_landing = True
            else:
                # 如果在地面，直接下蹲
                self.duck()

    def key_release(self, event):
        if event.keysym == "Down":
            self.is_fast_falling = False
            self.auto_duck_on_landing = False  # 取消自动下蹲标记

            # 如果当前是下蹲状态，则站立
            if self.is_ducking:
                self.stand_up()

    def initiate_jump(self):
        if not self.is_jumping and not self.is_game_over and self.game_started and not self.is_ducking:
            self.is_jumping = True
            self.jump_velocity = self.jump_strength

    def duck(self):
        if not self.is_jumping and not self.is_ducking:
            self.is_ducking = True
            # 更新恐龙高度为下蹲高度
            if self.use_images:
                self.canvas.coords(self.dino, 65, self.dino_y + self.dino_height - self.duck_height // 2)
                self.canvas.itemconfig(self.dino, image=self.dino_duck_imgs[0])
            else:
                self.canvas.coords(self.dino, 50, self.dino_y + (self.dino_height - self.duck_height),
                                   80, self.dino_y + self.dino_height)

    def stand_up(self):
        if self.is_ducking:
            self.is_ducking = False
            # 恢复恐龙正常高度
            if self.use_images:
                self.canvas.coords(self.dino, 65, self.dino_y + self.dino_height // 2)
                self.canvas.itemconfig(self.dino, image=self.dino_run_imgs[0])
            else:
                self.canvas.coords(self.dino, 50, self.dino_y, 80, self.dino_y + self.dino_height)

    def update_animation(self):
        # 如果游戏结束，不更新正常动画
        if self.is_game_over:
            return

        # 更新动画计数器
        self.animation_counter += 1

        # 如果计数器达到动画速度阈值，更新动画帧
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0

            if self.use_images:
                if not self.is_jumping and not self.is_ducking:
                    # 跑步动画
                    self.current_run_frame = (self.current_run_frame + 1) % len(self.dino_run_imgs)
                    self.canvas.itemconfig(self.dino, image=self.dino_run_imgs[self.current_run_frame])
                elif self.is_ducking:
                    # 下蹲动画
                    self.current_duck_frame = (self.current_duck_frame + 1) % len(self.dino_duck_imgs)
                    self.canvas.itemconfig(self.dino, image=self.dino_duck_imgs[self.current_duck_frame])
                # 跳跃时保持第一帧跑步图片
                elif self.is_jumping:
                    self.canvas.itemconfig(self.dino, image=self.dino_run_imgs[0])

    def update_ptera_animation(self):
        # 更新翼龙动画计数器
        self.ptera_animation_counter += 1

        # 如果计数器达到动画速度阈值，更新所有翼龙的动画帧
        if self.ptera_animation_counter >= self.ptera_animation_speed:
            self.ptera_animation_counter = 0

            # 遍历所有障碍物，更新翼龙的动画
            for i, obstacle_info in enumerate(self.obstacle_types):
                if isinstance(obstacle_info, dict) and obstacle_info["type"] == "pterodactyl":
                    # 切换翼龙动画帧
                    obstacle_info["current_frame"] = (obstacle_info["current_frame"] + 1) % len(self.ptera_imgs)
                    self.canvas.itemconfig(self.obstacles[i], image=self.ptera_imgs[obstacle_info["current_frame"]])

    def update_dead_animation(self):
        # 更新死亡动画计数器
        self.dead_animation_counter += 1

        # 当计数器达到一定值时，显示游戏结束文字
        if self.dead_animation_counter >= 10:  # 延迟一点显示文字，让玩家有时间反应
            self.show_game_over_text()

    def jump(self):
        if self.is_jumping:
            current_gravity = self.fast_fall_gravity if self.is_fast_falling else self.gravity

            self.dino_y += self.jump_velocity
            self.jump_velocity += current_gravity

            if self.dino_y >= 300:
                self.dino_y = 300
                self.is_jumping = False
                self.jump_velocity = 0
                self.is_fast_falling = False

                # 检查是否需要自动下蹲
                if self.auto_duck_on_landing:
                    self.duck()

            # 更新恐龙的画布位置
            if self.use_images:
                if self.is_ducking:
                    self.canvas.coords(self.dino, 65, self.dino_y + self.dino_height - self.duck_height // 2)
                else:
                    self.canvas.coords(self.dino, 65, self.dino_y + self.dino_height // 2)
            else:
                if self.is_ducking:
                    self.canvas.coords(self.dino, 50, self.dino_y + (self.dino_height - self.duck_height),
                                       80, self.dino_y + self.dino_height)
                else:
                    self.canvas.coords(self.dino, 50, self.dino_y, 80, self.dino_y + self.dino_height)

    def generate_obstacle(self):
        # 随机决定生成普通障碍物还是翼龙
        if random.random() < self.pterodactyl_chance:
            # 生成翼龙
            if self.use_images and self.ptera_imgs:
                # 随机选择翼龙飞行高度
                height = random.randint(250, 300)  # 翼龙在空中飞行

                # 随机选择初始动画帧
                initial_frame = random.randint(0, len(self.ptera_imgs) - 1)
                ptera_img = self.ptera_imgs[initial_frame]

                # 使用翼龙的原始大小
                ptera_width = self.ptera_widths[initial_frame]
                ptera_height = self.ptera_heights[initial_frame]

                # 创建翼龙障碍物
                obstacle = self.canvas.create_image(
                    800, height,
                    image=ptera_img, anchor=tk.CENTER
                )

                # 存储障碍物的额外信息用于碰撞检测和动画
                obstacle_info = {
                    "type": "pterodactyl",
                    "width": ptera_width,
                    "height": ptera_height,
                    "image": ptera_img,  # 保持引用，防止被垃圾回收
                    "current_frame": initial_frame
                }

                self.obstacles.append(obstacle)
                self.obstacle_types.append(obstacle_info)
            else:
                # 如果没有图片，使用矩形
                height = random.randint(250, 300)
                width = 40
                obstacle = self.canvas.create_rectangle(
                    800, height,
                    800 + width, height + 20,
                    fill="darkgray"
                )
                self.obstacles.append(obstacle)
                self.obstacle_types.append("pterodactyl")
        else:
            # 生成仙人掌
            if self.use_images and self.cactus_imgs:
                # 随机选择一种仙人掌
                cactus_type = random.randint(0, len(self.cactus_imgs) - 1)
                cactus_img = self.cactus_imgs[cactus_type]

                # 使用仙人掌的原始大小
                cactus_width = self.cactus_widths[cactus_type]
                cactus_height = self.cactus_heights[cactus_type]

                # 创建仙人掌障碍物
                obstacle = self.canvas.create_image(
                    800, 350 - cactus_height // 2,
                    image=cactus_img, anchor=tk.CENTER
                )

                # 存储障碍物的额外信息用于碰撞检测
                obstacle_info = {
                    "type": "cactus",
                    "width": cactus_width,
                    "height": cactus_height,
                    "image": cactus_img  # 保持引用，防止被垃圾回收
                }

                self.obstacles.append(obstacle)
                self.obstacle_types.append(obstacle_info)
            else:
                # 如果没有图片，使用矩形
                height = random.choice([20, 30, 40, 50])
                width = 20
                obstacle = self.canvas.create_rectangle(
                    800, 350 - height,
                         800 + width, 350,
                    fill="gray"
                )
                self.obstacles.append(obstacle)
                self.obstacle_types.append("cactus")

    def move_obstacles(self):
        # 如果游戏结束，障碍物停止移动
        if self.is_game_over:
            return

        obstacles_to_remove = []

        for i, obstacle in enumerate(self.obstacles):
            self.canvas.move(obstacle, -self.game_speed, 0)

            # 获取障碍物位置
            pos = self.canvas.coords(obstacle)

            # 如果障碍物移出屏幕，标记为待删除
            if pos and pos[0] + (
            self.obstacle_types[i].get("width", 20) if isinstance(self.obstacle_types[i], dict) else 20) < 0:
                obstacles_to_remove.append((i, obstacle))
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

                # 每得5分增加游戏速度
                if self.score % 5 == 0:
                    self.game_speed += 1
                    # 随着游戏进行，增加翼龙出现的概率
                    self.pterodactyl_chance = min(0.6, self.pterodactyl_chance + 0.05)

        # 删除已移出屏幕的障碍物
        for i, obstacle in obstacles_to_remove:
            self.canvas.delete(obstacle)
            self.obstacles.pop(i)
            self.obstacle_types.pop(i)

            # 当一个障碍物移出屏幕时，立即生成一个新的障碍物
            self.generate_obstacle()

    def check_collision(self):
        if not self.game_started or self.is_game_over:
            return

        if self.use_images:
            # 对于图片，获取图片的边界框
            dino_pos = self.canvas.bbox(self.dino)
        else:
            # 对于矩形，直接获取坐标
            dino_pos = self.canvas.coords(self.dino)

        for i, obstacle in enumerate(self.obstacles):
            obstacle_pos = self.canvas.coords(obstacle)
            obstacle_type = self.obstacle_types[i]

            # 根据障碍物类型调整碰撞检测
            if isinstance(obstacle_type, dict):
                if obstacle_type["type"] == "cactus":
                    # 仙人掌的碰撞检测
                    cactus_width = obstacle_type["width"]
                    cactus_height = obstacle_type["height"]

                    # 计算仙人掌的实际边界
                    cactus_left = obstacle_pos[0] - cactus_width // 2
                    cactus_right = obstacle_pos[0] + cactus_width // 2
                    cactus_top = obstacle_pos[1] - cactus_height // 2
                    cactus_bottom = obstacle_pos[1] + cactus_height // 2

                    if (dino_pos[2] > cactus_left and  # 恐龙右边缘 > 仙人掌左边缘
                            dino_pos[0] < cactus_right and  # 恐龙左边缘 < 仙人掌右边缘
                            dino_pos[3] > cactus_top):  # 恐龙底部 > 仙人掌顶部
                        self.start_game_over()
                        return
                elif obstacle_type["type"] == "pterodactyl":
                    # 翼龙的碰撞检测
                    ptera_width = obstacle_type["width"]
                    ptera_height = obstacle_type["height"]

                    # 计算翼龙的实际边界
                    ptera_left = obstacle_pos[0] - ptera_width // 2
                    ptera_right = obstacle_pos[0] + ptera_width // 2
                    ptera_top = obstacle_pos[1] - ptera_height // 2
                    ptera_bottom = obstacle_pos[1] + ptera_height // 2

                    # 翼龙的碰撞检测 - 恐龙必须完全在翼龙下方或上方才能避免碰撞
                    if (dino_pos[2] > ptera_left and  # 恐龙右边缘 > 翼龙左边缘
                            dino_pos[0] < ptera_right and  # 恐龙左边缘 < 翼龙右边缘
                            not (dino_pos[3] < ptera_top or dino_pos[1] > ptera_bottom)):  # 恐龙不在翼龙完全下方或上方
                        self.start_game_over()
                        return
            elif obstacle_type == "cactus":
                # 矩形仙人掌的碰撞检测
                if (dino_pos[2] > obstacle_pos[0] and  # 恐龙右边缘 > 障碍物左边缘
                        dino_pos[0] < obstacle_pos[2] and  # 恐龙左边缘 < 障碍物右边缘
                        dino_pos[3] > obstacle_pos[1]):  # 恐龙底部 > 障碍物顶部
                    self.start_game_over()
                    return
            elif obstacle_type == "pterodactyl":
                # 矩形翼龙的碰撞检测 - 恐龙必须完全在翼龙下方或上方才能避免碰撞
                if (dino_pos[2] > obstacle_pos[0] and  # 恐龙右边缘 > 翼龙左边缘
                        dino_pos[0] < obstacle_pos[2] and  # 恐龙左边缘 < 翼龙右边缘
                        not (dino_pos[3] < obstacle_pos[1] or dino_pos[1] > obstacle_pos[3])):  # 恐龙不在翼龙完全下方或上方
                    self.start_game_over()
                    return

    def start_game_over(self):
        self.is_game_over = True
        self.dead_animation_started = True
        self.dead_animation_counter = 0

        # 立即切换到失败图片（如果有）
        if self.use_images and self.dino_dead_img:
            self.canvas.itemconfig(self.dino, image=self.dino_dead_img)
        elif not self.use_images:
            # 如果没有图片，将恐龙颜色改为红色表示失败
            self.canvas.itemconfig(self.dino, fill="red")
        if self.on_game_over_callback:
            self.on_game_over_callback(self.score)

    def show_game_over_text(self):
        # 显示游戏结束文字
        self.canvas.create_text(400, 150, text="Game over", font=("Arial", 30), fill="black", tags="game_over")
        self.canvas.create_text(400, 200, text=f"最终得分: {self.score}", font=("Arial", 20), tags="game_over")
        self.canvas.create_text(400, 250, text="点击鼠标重新开始", font=("Arial", 16), tags="game_over")

    def update_game(self):
        if self.game_started and not self.is_game_over:
            self.jump()
            self.move_obstacles()
            self.check_collision()
            self.update_animation()
            self.update_ptera_animation()
        elif self.dead_animation_started:
            self.update_dead_animation()

        self.root.after(30, self.update_game)

    def get_score(self):
        return self.score

def start_():#制作弹窗
    root = tk.Toplevel()
    game = DinoGame(root)
    root.mainloop()
def start_game(player_name=None):
    return DinoGame.get_score()

if __name__ == "__main__":
    a=tk.Tk()#设置主窗口
    a.geometry('400x400')
    a.title('小恐龙跑酷')
    b=tk.Button(a,text='start',command=start_)
    b.pack()
    #root = tk.Toplevel()
    #game = DinoGame(root)
    a.mainloop()