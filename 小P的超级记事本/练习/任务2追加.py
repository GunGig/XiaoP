# 1. 获取用户想记录的内容
memo_to_add = input("小P，这次你想记下什么？")

# 2. 打开文件 (追加模式)
file = open("memos.txt", ？？, encoding="utf-8")
# "a" 代表追加模式 (append)

# 3. 写入新内容，并在末尾加上换行符 \n
file.write(memo_to_add + "\n") # "\n" 让每条记录占一行

# 4. 关闭文件
file.close()

print("小P又补充了一条日记！")