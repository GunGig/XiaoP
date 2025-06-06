# 任务6的参考代码
MEMO_FILENAME = "my_notes.txt"

def view_memos():
    """这个函数会读取并展示所有备忘录。"""
    try:
        with open(MEMO_FILENAME, "r", encoding="utf-8") as file:
            memos = file.readlines()

        if not memos: # 检查列表是否为空
            print("小P的记事本还是空的，快去添加一些吧！")
            return # 如果为空，直接结束函数

        print("\\n--- 小P的超级记事本 ---")
        for index, memo in enumerate(memos):
            print(f"{index + 1}. {memo.strip()}") # index从0开始，所以+1
        print("-----------------------")

    except FileNotFoundError:
        print(f"小P的记事本 ({MEMO_FILENAME}) 还没创建呢！先添加一条备忘吧。")

# 测试我们的新函数
# 假设你已经通过 add_memo 添加过一些内容
# add_memo("今天要完成HTML页面") # 如果需要，可以先添加一些
view_memos()