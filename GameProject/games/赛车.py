import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏窗口设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("像素赛车")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

# 游戏参数
clock = pygame.time.Clock()
FPS = 60
score = 0
game_over = False

# 玩家赛车
player_size = 10
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_speed = 5

# 道路参数
road_width = 300
road_x = (WIDTH - road_width) // 2
road_markings = []
marking_height = 30
marking_gap = 40
marking_speed = 5

# 初始化道路标记
for i in range(0, HEIGHT, marking_height + marking_gap):
    road_markings.append(i)

# 障碍物
obstacles = []
obstacle_size = 15
obstacle_speed = 7
obstacle_frequency = 30  # 每隔多少帧生成一个障碍物
frame_count = 0

# 字体
font = pygame.font.SysFont(None, 36)


def draw_player():
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))


def draw_road():
    # 绘制道路
    pygame.draw.rect(screen, GRAY, (road_x, 0, road_width, HEIGHT))

    # 绘制道路标记
    for y in road_markings:
        pygame.draw.rect(screen, YELLOW, (WIDTH // 2 - 5, y, 10, marking_height))


def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))


def update_road():
    global road_markings
    # 更新道路标记位置
    for i in range(len(road_markings)):
        road_markings[i] += marking_speed
        if road_markings[i] > HEIGHT:
            road_markings[i] = -marking_height

    # 重新排序标记，确保连续性
    road_markings.sort()


def update_obstacles():
    global obstacles, score, game_over

    # 生成新障碍物
    if frame_count % obstacle_frequency == 0:
        obstacle_x = random.randint(road_x + 10, road_x + road_width - obstacle_size - 10)
        obstacles.append([obstacle_x, -obstacle_size])

    # 更新障碍物位置
    for obstacle in obstacles[:]:
        obstacle[1] += obstacle_speed

        # 检测碰撞
        if (player_x < obstacle[0] + obstacle_size and
                player_x + player_size > obstacle[0] and
                player_y < obstacle[1] + obstacle_size and
                player_y + player_size > obstacle[1]):
            game_over = True

        # 移除超出屏幕的障碍物并计分
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)
            score += 1


def show_score():
    score_text = font.render(f"得分: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


def show_game_over():
    game_over_text = font.render("游戏结束! 按R键重新开始", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))


def reset_game():
    global player_x, player_y, obstacles, score, game_over, frame_count
    player_x = WIDTH // 2
    player_y = HEIGHT - 50
    obstacles = []
    score = 0
    game_over = False
    frame_count = 0


# 游戏主循环
running = True
while running:
    frame_count += 1

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                reset_game()

    # 获取按键状态
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player_x > road_x:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < road_x + road_width - player_size:
            player_x += player_speed

    # 更新游戏状态
    if not game_over:
        update_road()
        update_obstacles()

    # 绘制
    screen.fill(BLACK)
    draw_road()
    draw_obstacles()
    draw_player()
    show_score()

    if game_over:
        show_game_over()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()







































