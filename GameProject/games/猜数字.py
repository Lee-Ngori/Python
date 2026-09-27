import random
import time
from datetime import datetime


class NumberGuessingGame:
    def __init__(self):
        self.leaderboard = []
        self.stats = {
            'games_played': 0,
            'total_attempts': 0,
            'best_score': float('inf')
        }

    def display_welcome(self):
        print("🎯" * 30)
        print("          高级猜数字游戏 v2.0")
        print("🎯" * 30)
        print("\n游戏特性:")
        print("✅ 多难度选择  ✅ 智能提示  ✅ 排行榜系统")
        print("✅ 游戏统计  ✅ 成就系统  ✅ 时间挑战\n")

    def select_difficulty(self):
        print("\n🎚️  请选择难度级别:")
        print("1. 简单 (1-50, 无限次数)")
        print("2. 中等 (1-100, 15次机会)")
        print("3. 困难 (1-200, 10次机会)")
        print("4. 地狱 (1-500, 8次机会)")
        print("5. 自定义范围")

        while True:
            try:
                choice = int(input("请输入选择 (1-5): "))
                if choice == 1:
                    return 1, 50, float('inf')
                elif choice == 2:
                    return 1, 100, 15
                elif choice == 3:
                    return 1, 200, 10
                elif choice == 4:
                    return 1, 500, 8
                elif choice == 5:
                    return self.custom_range()
                else:
                    print("❌ 请输入1-5之间的数字！")
            except ValueError:
                print("❌ 请输入有效数字！")

    def custom_range(self):
        while True:
            try:
                min_num = int(input("请输入最小值: "))
                max_num = int(input("请输入最大值: "))
                max_attempts = int(input("请输入最大尝试次数: "))

                if min_num >= max_num:
                    print("❌ 最小值必须小于最大值！")
                    continue
                if max_attempts <= 0:
                    print("❌ 尝试次数必须大于0！")
                    continue

                return min_num, max_num, max_attempts
            except ValueError:
                print("❌ 请输入有效数字！")

    def get_intelligent_hint(self, guess, target, attempts, max_attempts):
        difference = abs(guess - target)
        ratio = difference / (target * 0.1)

        if attempts == 1:
            if target % 2 == 0:
                return "💡 提示: 这个数字是偶数"
            else:
                return "💡 提示: 这个数字是奇数"

        if ratio < 0.1:
            return "🔥 非常接近了！就差一点点！"
        elif ratio < 0.3:
            return "👌 比较接近了，继续加油！"
        elif ratio < 0.6:
            return "💪 还有一定距离，再试试看"
        else:
            return "🎯 距离目标还有点远"

    def calculate_score(self, attempts, max_num, max_attempts, time_taken):
        base_score = 1000
        attempt_bonus = (max_attempts - attempts) * 50
        difficulty_bonus = max_num // 10
        time_bonus = max(0, 300 - time_taken)  # 5分钟内完成有奖励

        return base_score + attempt_bonus + difficulty_bonus + time_bonus

    def update_leaderboard(self, player_name, score, attempts, difficulty):
        self.leaderboard.append({
            'name': player_name,
            'score': score,
            'attempts': attempts,
            'difficulty': difficulty,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # 按分数排序，只保留前10名
        self.leaderboard.sort(key=lambda x: x['score'], reverse=True)
        self.leaderboard = self.leaderboard[:10]

    def show_leaderboard(self):
        if not self.leaderboard:
            print("\n📊 排行榜目前为空")
            return

        print(f"\n🏆 排行榜 TOP {len(self.leaderboard)}")
        print("-" * 60)
        print(f"{'排名':<4} {'玩家':<10} {'分数':<8} {'次数':<6} {'难度':<8} {'时间':<12}")
        print("-" * 60)

        for i, entry in enumerate(self.leaderboard, 1):
            print(f"{i:<4} {entry['name']:<10} {entry['score']:<8} {entry['attempts']:<6} "
                  f"{entry['difficulty']:<8} {entry['timestamp'][11:16]:<12}")

    def show_stats(self):
        print(f"\n📈 游戏统计:")
        print(f"总游戏次数: {self.stats['games_played']}")
        if self.stats['games_played'] > 0:
            avg_attempts = self.stats['total_attempts'] / self.stats['games_played']
            print(f"平均尝试次数: {avg_attempts:.1f}")
            print(f"最佳成绩: {self.stats['best_score']} 次")
        else:
            print("暂无游戏数据")

    def check_achievements(self, attempts, max_num):
        achievements = []

        if attempts == 1:
            achievements.append("🎯 一发命中！")
        if attempts <= 3:
            achievements.append("⚡ 速通大师！")
        if max_num >= 200 and attempts <= 5:
            achievements.append("🧠 数学天才！")
        if len(self.leaderboard) > 0 and self.leaderboard[0]['name'] == self.current_player:
            achievements.append("👑 排行榜第一！")

        return achievements

    def play_game(self):
        self.display_welcome()

        min_num, max_num, max_attempts = self.select_difficulty()
        target = random.randint(min_num, max_num)
        attempts = 0
        start_time = time.time()

        difficulty_name = f"{max_num}"
        if max_attempts == float('inf'):
            difficulty_name += "(简单)"

        print(f"\n🎮 游戏开始！数字范围: {min_num}-{max_num}")
        print(f"⏱️  最大尝试次数: {'无限' if max_attempts == float('inf') else max_attempts}")

        while attempts < max_attempts:
            try:
                remaining = max_attempts - attempts
                prompt = f"\n第{attempts + 1}次猜测"
                if max_attempts != float('inf'):
                    prompt += f" (剩余{remaining}次)"
                prompt += ": "

                guess = int(input(prompt))
                attempts += 1

                if guess < min_num or guess > max_num:
                    print(f"❌ 数字必须在 {min_num}-{max_num} 范围内！")
                    continue

                # 检查猜测结果
                if guess < target:
                    print("📉 太小了！", end=" ")
                elif guess > target:
                    print("📈 太大了！", end=" ")
                else:
                    time_taken = time.time() - start_time
                    score = self.calculate_score(attempts, max_num,
                                                 max_attempts if max_attempts != float('inf') else 10,
                                                 time_taken)

                    print(f"\n🎉 恭喜！你在第{attempts}次猜中了数字 {target}！")
                    print(f"⏰ 用时: {time_taken:.1f}秒")
                    print(f"🏅 得分: {score}")

                    # 更新统计
                    self.stats['games_played'] += 1
                    self.stats['total_attempts'] += attempts
                    if attempts < self.stats['best_score']:
                        self.stats['best_score'] = attempts

                    # 检查成就
                    achievements = self.check_achievements(attempts, max_num)
                    if achievements:
                        print("🎖️  获得成就:", " ".join(achievements))

                    # 更新排行榜
                    player_name = input("请输入你的名字记录到排行榜: ") or "匿名玩家"
                    self.current_player = player_name
                    self.update_leaderboard(player_name, score, attempts, difficulty_name)

                    break

                # 提供智能提示
                if attempts > 1:
                    hint = self.get_intelligent_hint(guess, target, attempts, max_attempts)
                    print(hint)

            except ValueError:
                print("❌ 请输入有效数字！")
        else:
            print(f"\n💔 游戏结束！正确答案是: {target}")
            print("别灰心，再试一次！")

    def main_menu(self):
        while True:
            print(f"\n{'=' * 40}")
            print("           主菜单")
            print('=' * 40)
            print("1. 🎮 开始新游戏")
            print("2. 🏆 查看排行榜")
            print("3. 📊 查看统计")
            print("4. 🚪 退出游戏")

            choice = input("请选择 (1-4): ").strip()

            if choice == '1':
                self.play_game()
            elif choice == '2':
                self.show_leaderboard()
            elif choice == '3':
                self.show_stats()
            elif choice == '4':
                print("👋 感谢游玩！再见～")
                break
            else:
                print("❌ 请输入1-4之间的选项！")


# 运行游戏
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.main_menu()