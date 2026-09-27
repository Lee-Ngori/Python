import pygame
import random
import sys

# 初始化Pygame
pygame.init()
pygame.font.init()

# 游戏配置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_ROWS = 5
GRID_COLS = 9
GRID_SIZE = 80  # 每个格子大小
FPS = 30

# 颜色定义
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BROWN = (139, 69, 19)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# 字体
FONT = pygame.font.SysFont("Arial", 24)

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("简易植物大战僵尸")
clock = pygame.time.Clock()

# 植物类
class Plant:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type  # "sunflower" 或 "peashooter"
        self.health = 100 if type == "sunflower" else 150
        self.cooldown = 0  # 攻击/生产冷却

    def draw(self):
        # 简化绘制：向日葵（黄色圆形）、豌豆射手（绿色矩形）
        if self.type == "sunflower":
            pygame.draw.circle(screen, YELLOW, (self.x + GRID_SIZE//2, self.y + GRID_SIZE//2), 30)
        else:
            pygame.draw.rect(screen, GREEN, (self.x + 10, self.y + 10, GRID_SIZE-20, GRID_SIZE-20))
        # 绘制血量条
        pygame.draw.rect(screen, RED, (self.x, self.y - 5, GRID_SIZE, 5))
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 5, self.health * GRID_SIZE // 100, 5))

    def update(self, suns, peas):
        if self.type == "sunflower" and self.cooldown <= 0:
            # 每5秒生产1个阳光
            suns.append(Sun(self.x + GRID_SIZE//2, self.y))
            self.cooldown = 150  # 5秒（FPS=30，30*5=150帧）
        elif self.type == "peashooter" and self.cooldown <= 0:
            # 每2秒发射1颗豌豆
            peas.append(Pea(self.x + GRID_SIZE, self.y + GRID_SIZE//2))
            self.cooldown = 60  # 2秒（30*2=60帧）
        self.cooldown -= 1

# 阳光类
class Sun:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2  # 下落速度

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), 15)

    def update(self):
        self.y += self.speed
        # 超出屏幕则删除
        return self.y > SCREEN_HEIGHT

# 豌豆类
class Pea:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8  # 飞行速度
        self.damage = 20  # 伤害值

    def draw(self):
        pygame.draw.circle(screen, GREEN, (self.x, self.y), 8)

    def update(self):
        self.x += self.speed
        # 超出屏幕则删除
        return self.x > SCREEN_WIDTH

# 僵尸类
class Zombie:
    def __init__(self, row):
        self.x = SCREEN_WIDTH  # 从右侧进入
        self.y = row * GRID_SIZE + 50  # 对应行的位置
        self.health = 200
        self.speed = 2  # 移动速度

    def draw(self):
        # 简化绘制：僵尸（灰色矩形+红色眼睛）
        pygame.draw.rect(screen, GRAY, (self.x, self.y, 60, 70))
        pygame.draw.circle(screen, RED, (self.x + 20, self.y + 20), 5)
        pygame.draw.circle(screen, RED, (self.x + 40, self.y + 20), 5)
        # 绘制血量条
        pygame.draw.rect(screen, RED, (self.x, self.y - 5, 60, 5))
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 5, self.health * 60 // 200, 5))

    def update(self):
        self.x -= self.speed
        # 到达左侧则游戏结束
        return self.x < -60

# 主游戏逻辑
def main():
    plants = []  # 植物列表
    suns = []    # 阳光列表
    peas = []    # 豌豆列表
    zombies = [] # 僵尸列表
    sun_count = 5000  # 初始阳光
    selected_plant = None  # 选中的植物类型
    spawn_timer = 0  # 僵尸生成计时器
    game_over = False

    while not game_over:
        clock.tick(FPS)
        screen.fill(WHITE)

        # 1. 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 鼠标点击：选择植物或种植植物
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                # 点击左侧植物选择区（x<100）
                if x < 100:
                    # 向日葵（50阳光）
                    if 100 < y < 180 and sun_count >= 50:
                        selected_plant = "sunflower"
                    # 豌豆射手（100阳光）
                    elif 200 < y < 280 and sun_count >= 100:
                        selected_plant = "peashooter"
                # 点击种植区（x>=100，y>=50）
                elif x >= 100 and y >= 50 and selected_plant:
                    # 计算种植格子
                    col = (x - 100) // GRID_SIZE
                    row = (y - 50) // GRID_SIZE
                    # 检查格子是否合法且未种植
                    if 0 <= col < GRID_COLS and 0 <= row < GRID_ROWS:
                        plant_x = 100 + col * GRID_SIZE
                        plant_y = 50 + row * GRID_SIZE
                        # 检查该位置是否已有植物
                        if not any(p.x == plant_x and p.y == plant_y for p in plants):
                            # 消耗阳光并种植
                            if selected_plant == "sunflower":
                                sun_count -= 50
                            else:
                                sun_count -= 100
                            plants.append(Plant(plant_x, plant_y, selected_plant))
                            selected_plant = None
            # 收集阳光
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                for sun in suns[:]:
                    if (x - sun.x)**2 + (y - sun.y)**2 <= 15**2:  # 点击阳光范围
                        suns.remove(sun)
                        sun_count += 25

        # 2. 更新游戏元素
        # 更新阳光
        for sun in suns[:]:
            if sun.update():
                suns.remove(sun)
            sun.draw()

        # 更新植物
        for plant in plants[:]:
            plant.update(suns, peas)
            plant.draw()
            # 检查植物是否被僵尸攻击
            for zombie in zombies:
                if (zombie.x < plant.x + GRID_SIZE and zombie.x + 60 > plant.x and
                    zombie.y < plant.y + GRID_SIZE and zombie.y + 70 > plant.y):
                    plant.health -= 1
                    if plant.health <= 0:
                        plants.remove(plant)

        # 更新豌豆
        for pea in peas[:]:
            if pea.update():
                peas.remove(pea)
            pea.draw()
            # 检查豌豆是否击中僵尸
            for zombie in zombies[:]:
                if (pea.x > zombie.x and pea.x < zombie.x + 60 and
                    abs(pea.y - (zombie.y + 35)) < 35):
                    zombies.remove(zombie)
                    peas.remove(pea)
                    break

        # 更新僵尸（每10秒生成1个）
        spawn_timer += 1
        if spawn_timer >= 300:  # 10秒（30*10=300帧）
            row = random.randint(0, GRID_ROWS-1)
            zombies.append(Zombie(row))
            spawn_timer = 0

        for zombie in zombies[:]:
            if zombie.update():
                game_over = True  # 僵尸到达左侧，游戏结束
            zombie.draw()

        # 3. 绘制UI
        # 绘制种植网格
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                x = 100 + col * GRID_SIZE
                y = 50 + row * GRID_SIZE
                pygame.draw.rect(screen, GRAY, (x, y, GRID_SIZE, GRID_SIZE), 1)
        # 绘制左侧植物选择区
        pygame.draw.rect(screen, BROWN, (0, 0, 100, SCREEN_HEIGHT))  # 土地背景
        # 向日葵图标+价格
        pygame.draw.circle(screen, YELLOW, (50, 140), 30)
        screen.blit(FONT.render("50", True, WHITE), (40, 170))
        # 豌豆射手图标+价格
        pygame.draw.rect(screen, GREEN, (20, 220, 60, 60))
        screen.blit(FONT.render("100", True, WHITE), (35, 280))
        # 绘制阳光数量
        screen.blit(FONT.render(f"Sun: {sun_count}", True, YELLOW), (10, 10))
        # 绘制选中植物提示
        if selected_plant:
            tip = f"Selected: {selected_plant}"
            screen.blit(FONT.render(tip, True, RED), (120, 10))

        # 4. 游戏结束处理
        if game_over:
            screen.blit(FONT.render("GAME OVER!", True, RED), (300, 250))
            screen.blit(FONT.render("Press Q to Quit", True, GRAY), (300, 300))
            # 按Q退出
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

        # 更新屏幕
        pygame.display.update()

if __name__ == "__main__":
    main()