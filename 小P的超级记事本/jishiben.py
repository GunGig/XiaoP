# jishiben.py

# 记事本文件的名字
MEMO_FILENAME = "my_notes.txt"


def add_memo(memo_text):
    """添加一条备忘到文件中"""
    # 使用 "a" 模式来追加内容
    with open(MEMO_FILENAME, "a", encoding="utf-8") as file:
        file.write(memo_text + "\n")  # 使用 \n 作为换行符
    print(f"小P已添加备忘：'{memo_text}'")


def view_memos():
    """查看所有备忘"""
    try:
        with open(MEMO_FILENAME, "r", encoding="utf-8") as file:
            memos = file.readlines()

        if not memos:
            print("小P的记事本还是空的！")
            return

        print("\n--- 小P的超级记事本 ---")
        for index, memo in enumerate(memos):
            # .strip() 可以去掉每行末尾的换行符
            print(f"{index + 1}. {memo.strip()}")
        print("-----------------------")
    except FileNotFoundError:
        print(f"记事本 ({MEMO_FILENAME}) 还没创建呢！先添加一条备忘吧。")


def run_notepad():
    """运行记事本的主程序函数"""
    print("\n欢迎使用小P的超级记事本！")
    while True:
        print("\n你可以做什么：")
        print("1. 添加新的备忘")
        print("2. 查看所有备忘")
        print("3. 返回主菜单")  # 修改 "退出" 为 "返回" 更贴切

        choice = input("请输入你的选择 (1/2/3): ")

        if choice == '1':
            memo = input("请输入你要记录的内容: ")
            if memo:  # 确保用户输入了内容
                add_memo(memo)
            else:
                print("你没有输入任何内容哦。")
        elif choice == '2':
            view_memos()
        elif choice == '3':
            print("已退出记事本，返回与小P聊天。👋")
            break  # 退出循环，函数结束，控制权交还给主程序
        else:
            print("无效的选择，请输入数字 1, 2 或 3 哦！")


# 这是一个重要的部分！
# 这行代码的意思是：只有当这个文件被直接运行时，才执行下面的 run_notepad()
# 如果它被其他文件 import，下面的代码就不会执行
if __name__ == "__main__":
    run_notepad()