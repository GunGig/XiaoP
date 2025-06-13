# “在 f-string 出现之前，
# Python程序员常用 .format() 来格式化字符串。

# 基本用法 (占位符 {}):
fruit = "香蕉"
quantity = 10
message1 = "我买了{}，一共{}根。".format(fruit, quantity)
print(message1)

# 按位置指定 (数字索引 {0}, {1}):
message2 = "我想吃{1}，而不是{0}。".format("苹果", "橘子") # 输出：我想吃橘子，而不是苹果。
print(message2)

# 按名称指定 (关键字参数 {name}):
message3 = "你好，{user_name}！你的等级是 {level}。".format(user_name="冒险者007", level=5)
print(message3)