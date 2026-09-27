import pygame
import random
import sys
import math

# 初始化Pygame
pygame.init()

# 游戏配置
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TILE_SIZE = 32  # 方块大小
CHUNK_SIZE = 16  # 区块大小（方块数）
WORLD_WIDTH = 32  # 世界宽度（区块数）
WORLD_HEIGHT = 16  # 世界高度（区块数）

# 颜色定义（方块材质简化）
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)  # 草方块
BROWN = (139, 69, 19)  # 泥土
GRAY = (128, 128, 128)  # 石头
BLUE = (0, 191, 255)  # 水
YELLOW = (255, 215, 0)  # 沙子
DARK_GRAY = (64, 64, 64)  # 煤炭
PINK = (255, 192, 203)  # 羊毛（装饰方块）

# 方块类型定义（id: (颜色, 是否可破坏, 是否可放置)）
BLOCK_TYPES = {
    0: (BLACK, False, False),    # 空气
    1: (GREEN, True, True),     # 草方块
    2: (BROWN, True, True),     # 泥土
    3: (GRAY, True, True),      # 石头
    4: (BLUE, True, False),     # 水（不可放置）
    5: (YELLOW, True, True),    # 沙子
    6: (DARK_GRAY, True, True), # 煤炭
    7: (PINK, True, True)       # 羊毛
}

# 玩家配置
PLAYER_SPEED = 5
PLAYER_JUMP_POWER = 15
GRAVITY = 0.8

# 设置屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("简易2D我的世界")

# 时钟（控制帧率）
clock = pygame.time.Clock()

# 字体设置
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)

# -------------------------- 世界生成类 --------------------------
class WorldGenerator:
    @staticmethod
    def generate_world():
        """生成随机地形（基于 simplex 噪声简化版）"""
        world = [[0 for _ in range(WORLD_HEIGHT * CHUNK_SIZE)] for __ in range(WORLD_WIDTH * CHUNK_SIZE)]
        sea_level = 6 * CHUNK_SIZE  # 海平面高度

        for x in range(WORLD_WIDTH * CHUNK_SIZE):
            # 生成地形高度（使用正弦函数模拟起伏）
            height = int(sea_level - 10 + math.sin(x / 50) * 15 + random.randint(-3, 3))
            
            # 填充地下方块
            for y in range(height, WORLD_HEIGHT * CHUNK_SIZE):
                if y == height:
                    # 地表：草方块（高于海平面）或沙子（海平面及以下）
                    if y < sea_level:
                        world[x][y] = 1  # 草方块
                    else:
                        world[x][y] = 5  # 沙子
                elif y < height + 3:
                    world[x][y] = 2  # 泥土（草方块下方）
                elif y < height + 10:
                    world[x][y] = 3  # 石头（泥土下方）
                else:
                    # 深层随机生成煤炭
                    if random.randint(1, 20) == 1:
                        world[x][y] = 6  # 煤炭
                    else:
                        world[x][y] = 3  # 石头

            # 生成水面（海平面）
            for y in range(sea_level - 3, sea_level):
                if world[x][y] == 0:
                    world[x][y] = 4  # 水

        return world

# -------------------------- 玩家类 --------------------------
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 40
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        self.inventory = [1, 2, 3, 5, 6, 7]  # 初始背包（方块id）
        self.selected_block = 0  # 当前选中的背包索引

    def update(self, world):
        # 重力应用
        self.velocity_y += GRAVITY
        if self.velocity_y > 10:  # 最大下落速度
            self.velocity_y = 10

        # 水平移动
        self.x += self.velocity_x
        # 碰撞检测（水平）
        self.collide(world, horizontal=True)

        # 垂直移动
        self.y += self.velocity_y
        self.on_ground = False
        # 碰撞检测（垂直）
        self.collide(world, horizontal=False)

    def collide(self, world, horizontal):
        """碰撞检测"""
        # 计算玩家所在的方块范围
        left = int(self.x // TILE_SIZE)
        right = int((self.x + self.width) // TILE_SIZE)
        top = int(self.y // TILE_SIZE)
        bottom = int((self.y + self.height) // TILE_SIZE)

        # 确保不超出世界边界
        left = max(0, left)
        right = min(WORLD_WIDTH * CHUNK_SIZE - 1, right)
        top = max(0, top)
        bottom = min(WORLD_HEIGHT * CHUNK_SIZE - 1, bottom)

        for x in range(left, right + 1):
            for y in range(top, bottom + 1):
                block_id = world[x][y]
                if block_id != 0:  # 非空气方块
                    block_x = x * TILE_SIZE
                    block_y = y * TILE_SIZE
                    block_rect = pygame.Rect(block_x, block_y, TILE_SIZE, TILE_SIZE)
                    player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

                    if player_rect.colliderect(block_rect):
                        if horizontal:
                            # 水平碰撞
                            if self.velocity_x > 0:  # 向右移动
                                self.x = block_rect.left - self.width
                            if self.velocity_x < 0:  # 向左移动
                                self.x = block_rect.right
                            self.velocity_x = 0
                        else:
                            # 垂直碰撞
                            if self.velocity_y > 0:  # 下落
                                self.y = block_rect.left - self.height
                                self.on_ground = True
                            if self.velocity_y < 0:  # 上升（撞顶）
                                self.y = block_rect.bottom
                            self.velocity_y = 0

    def move(self, direction):
        """水平移动控制"""
        if direction == "left":
            self.velocity_x = -PLAYER_SPEED
        elif direction == "right":
            self.velocity_x = PLAYER_SPEED
        else:
            self.velocity_x = 0  # 停止移动

    def jump(self):
        """跳跃（只能在地面上跳跃）"""
        if self.on_ground:
            self.velocity_y = -PLAYER_JUMP_POWER

    def get_selected_block_id(self):
        """获取当前选中的方块id"""
        return self.inventory[self.selected_block]

    def change_selected_block(self, direction):
        """切换选中的方块（左右箭头）"""
        if direction == "left":
            self.selected_block = (self.selected_block - 1) % len(self.inventory)
        else:
            self.selected_block = (self.selected_block + 1) % len(self.inventory)

# -------------------------- 游戏工具类 --------------------------
class GameUtils:
    @staticmethod
    def get_block_at_mouse(world, player_x, player_y, camera_x, camera_y):
        """获取鼠标指向的方块坐标"""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # 转换鼠标坐标到世界坐标
        world_mouse_x = mouse_x + camera_x
        world_mouse_y = mouse_y + camera_y
        # 计算对应的方块坐标
        block_x = int(world_mouse_x // TILE_SIZE)
        block_y = int(world_mouse_y // TILE_SIZE)
        # 边界检测
        if 0 <= block_x < WORLD_WIDTH * CHUNK_SIZE and 0 <= block_y < WORLD_HEIGHT * CHUNK_SIZE:
            return (block_x, block_y)
        return None

    @staticmethod
    def draw_world(screen, world, camera_x, camera_y):
        """绘制世界（只绘制屏幕可见区域）"""
        # 计算可见区域的方块范围
        start_x = int(camera_x // TILE_SIZE)
        end_x = int((camera_x + SCREEN_WIDTH) // TILE_SIZE) + 1
        start_y = int(camera_y // TILE_SIZE)
        end_y = int((camera_y + SCREEN_HEIGHT) // TILE_SIZE) + 1

        # 边界检测
        start_x = max(0, start_x)
        end_x = min(WORLD_WIDTH * CHUNK_SIZE, end_x)
        start_y = max(0, start_y)
        end_y = min(WORLD_HEIGHT * CHUNK_SIZE, end_y)

        # 绘制每个方块
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                block_id = world[x][y]
                if block_id != 0:
                    color = BLOCK_TYPES[block_id][0]
                    # 计算方块在屏幕上的位置
                    screen_x = x * TILE_SIZE - camera_x
                    screen_y = y * TILE_SIZE - camera_y
                    # 绘制方块
                    pygame.draw.rect(screen, color, (screen_x, screen_y, TILE_SIZE - 1, TILE_SIZE - 1))  # -1 留间隙

    @staticmethod
    def draw_player(screen, player, camera_x, camera_y):
        """绘制玩家"""
        screen_x = player.x - camera_x
        screen_y = player.y - camera_y
        pygame.draw.rect(screen, (0, 0, 255), (screen_x, screen_y, player.width, player.height))

    @staticmethod
    def draw_hud(screen, player):
        """绘制HUD（背包、选中方块、提示）"""
        # 背包背景
        hud_bg = pygame.Rect(SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT - 80, 320, 60)
        pygame.draw.rect(screen, (50, 50, 50), hud_bg)
        pygame.draw.rect(screen, WHITE, hud_bg, 2)

        # 绘制背包方块
        for i, block_id in enumerate(player.inventory):
            x = SCREEN_WIDTH // 2 - 150 + i * 50
            y = SCREEN_HEIGHT - 70
            # 方块背景
            pygame.draw.rect(screen, (30, 30, 30), (x, y, 40, 40))
            # 选中效果
            if i == player.selected_block:
                pygame.draw.rect(screen, YELLOW, (x - 2, y - 2, 44, 44), 2)
            # 绘制方块
            color = BLOCK_TYPES[block_id][0]
            pygame.draw.rect(screen, color, (x + 2, y + 2, 36, 36))

        # 操作提示
        text1 = font.render("WASD移动 | 空格跳跃 | 鼠标左键破坏 | 右键放置", True, WHITE)
        text2 = font.render("左右箭头切换方块 | ESC退出", True, WHITE)
        screen.blit(text1, (20, 20))
        screen.blit(text2, (20, 60))

        # 选中方块名称
        block_id = player.get_selected_block_id()
        block_names = {1: "草方块", 2: "泥土", 3: "石头", 5: "沙子", 6: "煤炭", 7: "羊毛"}
        name_text = font.render(f"当前选中: {block_names.get(block_id, '未知')}", True, WHITE)
        screen.blit(name_text, (SCREEN_WIDTH - 250, 20))

# -------------------------- 游戏初始化 --------------------------
def init_game():
    global world, player, camera_x, camera_y, day_night_timer, is_day
    # 生成世界
    world = WorldGenerator.generate_world()
    # 创建玩家（出生在世界中心）
    spawn_x = (WORLD_WIDTH * CHUNK_SIZE // 2) * TILE_SIZE
    spawn_y = (WORLD_HEIGHT * CHUNK_SIZE // 2) * TILE_SIZE
    player = Player(spawn_x, spawn_y)
    # 相机位置（跟随玩家）
    camera_x = player.x - SCREEN_WIDTH // 2
    camera_y = player.y - SCREEN_HEIGHT // 2
    # 昼夜切换计时器（1000帧=约16秒切换一次）
    day_night_timer = 0
    is_day = True

# 初始化游戏
init_game()

# -------------------------- 游戏主循环 --------------------------
running = True
moving_left = False
moving_right = False

while running:
    # 控制帧率
    clock.tick(FPS)

    # -------------------------- 事件处理 --------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 键盘按下事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_LEFT:
                player.change_selected_block("left")
            if event.key == pygame.K_RIGHT:
                player.change_selected_block("right")
        # 鼠标点击事件（破坏/放置方块）
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_block = GameUtils.get_block_at_mouse(world, player.x, player.y, camera_x, camera_y)
            if target_block:
                bx, by = target_block
                if event.button == 1:  # 左键破坏
                    if BLOCK_TYPES[world[bx][by]][1]:  # 可破坏方块
                        world[bx][by] = 0  # 变为空气
                elif event.button == 3:  # 右键放置
                    block_id = player.get_selected_block_id()
                    if BLOCK_TYPES[block_id][2]:  # 可放置方块
                        # 检查目标位置是否为空气
                        if world[bx][by] == 0:
                            world[bx][by] = block_id

    # 键盘长按事件（移动）
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        moving_left = True
        moving_right = False
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        moving_right = True
        moving_left = False
    else:
        moving_left = False
        moving_right = False

    # 玩家移动控制
    if moving_left:
        player.move("left")
    elif moving_right:
        player.move("right")
    else:
        player.move("stop")

    # -------------------------- 游戏更新 --------------------------
    # 更新玩家
    player.update(world)
    # 更新相机（跟随玩家）
    camera_x = player.x - SCREEN_WIDTH // 2
    camera_y = player.y - SCREEN_HEIGHT // 2
    # 限制相机不超出世界边界
    camera_x = max(0, min(camera_x, (WORLD_WIDTH * CHUNK_SIZE * TILE_SIZE) - SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, (WORLD_HEIGHT * CHUNK_SIZE * TILE_SIZE) - SCREEN_HEIGHT))

    # 昼夜切换
    day_night_timer += 1
    if day_night_timer >= 1000:
        is_day = not is_day
        day_night_timer = 0

    # -------------------------- 绘制场景 --------------------------
    # 背景色（白天=天蓝色，黑夜=深蓝色）
    bg_color = (135, 206, 235) if is_day else (10, 10, 40)
    screen.fill(bg_color)

    # 绘制世界
    GameUtils.draw_world(screen, world, camera_x, camera_y)
    # 绘制玩家
    GameUtils.draw_player(screen, player, camera_x, camera_y)
    # 绘制HUD
    GameUtils.draw_hud(screen, player)

    # 更新屏幕
    pygame.display.flip()

# 退出游戏
pygame.quit()
sys.exit()