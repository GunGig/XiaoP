memo_to_add = input("小P (使用 with 语句)，你想记下什么？")

# 使用 with 语句打开文件
？ open("memos.txt", "a", encoding="utf-8") ？ file:
    file.write(memo_to_add + "\n")
# 当代码块结束时 (离开 with 语句)，文件会自动关闭，不需要 file.close()

print("小P用更高级的方法记好了！")