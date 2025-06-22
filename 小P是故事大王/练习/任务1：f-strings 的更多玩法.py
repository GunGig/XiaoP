name = "小P"
action = "学习"
item = "Python"
# 思考：如何打印出 "小P 正在 学习 Python。" ？
# 传统方法：
print(name + " 正在 " + action + " " + item + "。")

apples = 5
oranges = 3
print(f"1我总共有",apples + oranges,"个水果。")
print(f"我总共有 {apples + oranges} 个水果。")

# 调用简单函数/方法：
guest_name = input("请输入你的名字：")
print(f"欢迎你，{guest_name.upper()}！你的名字大写是不是很酷？")
word_count = len(guest_name)
print(f"你的名字有 {word_count} 个字母。")

price = 19.998
print(f"这个商品的价格是：${price:.2f}") # 保留两位小数
