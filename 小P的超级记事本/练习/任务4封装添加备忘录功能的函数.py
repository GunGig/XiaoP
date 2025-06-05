# 任务4的参考代码
MEMO_FILENAME = "my_notes.txt" # 把文件名定义成一个变量，方便以后修改

def ？(memo_text):
    """这个函数会把一条备忘录追加到文件中。"""
    with open(MEMO_FILENAME, "a", encoding="utf-8") as file:
        file.write(memo_text + "\\n") # 函数内部确保添加换行符
    print(f"小P已添加备忘：'{memo_text}'")

# 测试我们的新函数
add_memo("今天下午3点开会")
add_memo("买牛奶")
add_memo("给妈妈打电话")