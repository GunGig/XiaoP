# 1. 打开文件 (如果不存在则创建，如果存在则清空内容后写入)
file = open("memos.txt", "w", encoding="utf-8")
# "w" 代表写入模式 (write)
# encoding="utf-8" 确保中文字符能正确保存

# 2. 写入内容
file.write("今天天气真好！")

# 3. 关闭文件 (非常重要！确保内容真正保存到磁盘)
file.close()

print("小P已经把第一行日记写好啦！去看看 memos.txt 文件吧！")