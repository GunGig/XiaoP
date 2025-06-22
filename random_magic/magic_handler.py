# XiaoP/random_magic/magic_handler.py
import random


def random_choice_from_list(options_str):
    """
    从用户提供的逗号分隔的选项中随机选择一个。
    """
    if not options_str:
        return "你还没有告诉我有什么选项呢！"
    options = [opt.strip() for opt in options_str.split(',') if opt.strip()]
    if not options:
        return "看起来你提供的选项都是空的哦。"
    return f"嗯... 我帮你选了：**{random.choice(options)}**！"


def generate_random_password(length=8):
    """生成一个指定长度的随机密码（包含大小写字母和数字）。"""
    if length < 4:
        return "密码长度至少要4位才能有点意义哦！"

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(random.choice(chars) for _ in range(length))
    return f"为你生成了一个{length}位的随机密码：**{password}** (请妥善保管！)"


def guess_the_number_game():
    """一个简单的猜数字游戏。"""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\n--- 猜数字游戏开始！---")
    print("我已经想好了一个1到100之间的数字，你来猜猜看！")
    print(f"你总共有 {max_attempts} 次机会。")

    while attempts < max_attempts:
        try:
            guess_str = input(f"第 {attempts + 1} 次尝试，请输入你猜的数字 (1-100)，或输入 'q' 退出游戏: ")
            if guess_str.lower() == 'q':
                print(f"好吧，游戏结束。正确答案是 {secret_number}。")
                return

            guess = int(guess_str)
            attempts += 1

            if guess < 1 or guess > 100:
                print("请输入1到100之间的数字哦！")
                continue  # 不计入有效尝试次数，让用户重新输入

            if guess < secret_number:
                print("太小了，再大一点试试！")
            elif guess > secret_number:
                print("太大了，再小一点试试！")
            else:
                print(f"🎉 恭喜你！在第 {attempts} 次猜中了！数字就是 {secret_number}！你真棒！")
                return
        except ValueError:
            print("请输入一个有效的数字！或者输入 'q' 退出。")

    print(f"哎呀，机会用完了！正确答案是 {secret_number}。下次加油！💪")
    return


def run_random_magic_menu():
    """随机魔法功能的菜单"""
    print("\n✨ 小P的随机魔法屋 ✨")
    while True:
        print("\n你可以选择：")
        print("1. 帮我做选择 (比如今天吃什么？)")
        print("2. 生成一个随机密码")
        print("3. 玩猜数字游戏")
        print("0. 返回与小P聊天")

        choice = input("请输入你的选择 (0-3): ").strip()

        if choice == '1':
            options_input = input("请告诉我都有哪些选项，用逗号隔开 (比如：米饭,面条,饺子): ")
            result = random_choice_from_list(options_input)
            print(f"小P说：{result}")
        elif choice == '2':
            try:
                length_str = input("你希望密码有多少位？(建议8-16位，最少4位，直接回车默认为8): ")
                if not length_str:
                    length = 8
                else:
                    length = int(length_str)

                if length >= 4:
                    result = generate_random_password(length)
                    print(f"小P说：{result}")
                else:
                    print("小P说：密码长度至少要4位哦！")
            except ValueError:
                print("小P说：请输入一个有效的数字作为长度。")
        elif choice == '3':
            guess_the_number_game()
            print("游戏结束，已返回随机魔法屋。")
        elif choice == '0':
            print("已退出随机魔法屋。")
            break
        else:
            print("无效的选择，请输入0到3之间的数字哦！")


if __name__ == "__main__":
    print("测试随机魔法模块...")
    run_random_magic_menu()
