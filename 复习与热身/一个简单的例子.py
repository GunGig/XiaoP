# creator：XianSong_Lin
# Time in 2025/6/5 15:27
# 1. 给我们的小P起个名字
my_ai_name = "小P助手"

# 2. 小P做自我介绍
print(f"你好！我是{my_ai_name}。很高兴认识你！")

# 3. 问用户问题
user_greeting = input("你也跟我打个招呼吧？(可以说'你好呀')：")

# 4. 准备一些小P能听懂的话和回答
responses = {
    "你好呀": "你好你好！今天天气真不错！",
    "你叫什么名字": f"我叫{my_ai_name}，很高兴为你服务！",
    "你好": "你好！很高兴和你聊天！" # 多准备几种问候
}

# 5. 根据用户的输入，让小P回答
if user_greeting in responses:
    print(responses[user_greeting])
elif "你好" in user_greeting: # 如果用户说了包含"你好"的句子
    print("你好呀！很高兴认识你！")
else:
    print("嗯...我现在还只会简单的问候，以后我会学更多本领的！")