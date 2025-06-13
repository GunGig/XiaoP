# 任务5的参考代码
MEMO_FILENAME = "my_notes.txt"

print("--- 方法1: 使用 read() ---")
try: # 使用 try-except 避免文件不存在时报错
    with open(MEMO_FILENAME, "r", encoding="utf-8") as file:
        all_content = file.read()()
        if all_content:
            print(all_content)
        else:
            print("记事本是空的哦！")
except FileNotFoundError:
    print(f"哎呀，找不到 {MEMO_FILENAME} 文件！小P还没开始写日记呢。")

print("\\n--- 方法2: 使用 readlines() ---")
try:
    with open(MEMO_FILENAME, "r", encoding="utf-8") as file:
        memo_lines = file.readlines() # 这是一个列表
        if memo_lines: # 判断列表是否为空
            print("小P的备忘录内容：")
            for line in memo_lines:
                print(line.strip()) # strip() 去掉首尾空白，包括换行符
        else:
            print("记事本是空的哦！")
except FileNotFoundError:
    print(f"哎呀，找不到 {MEMO_FILENAME} 文件！")