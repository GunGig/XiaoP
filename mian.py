# creator：XianSong_Lin
# Time in 2025/6/5 15:27

# 导入我们自己的记事本模块
import 小P的超级记事本.jishiben
import 小P是故事大王.gushidawang as gushi
# 1. 给我们的小P起个名字
my_ai_name = "小P助手"

# 2. 小P做自我介绍
print(f"你好！我是{my_ai_name}。很高兴认识你！")
print(f"你可以对我说 '你好'，或者输入 '记事本' 来使用我的记事本功能。")
print(f"输入 '退出' 或 '再见' 就可以结束聊天。")

# 4. 准备一些小P能听懂的话和回答
responses = {
    "你好呀": "你好你好！今天天气真不错！",
    "你叫什么名字": f"我叫{my_ai_name}，很高兴为你服务！",
    "你好": "你好！很高兴和你聊天！"
}

# 5. 创建一个主循环，让小P可以持续和用户交互
while True:
    # 3. 问用户问题
    user_input = input("\n你：")

    # 检查用户是否想退出
    if user_input in ["退出", "再见", "bye"]:
        print(f"小P：好的，下次再聊！拜拜！")
        break

    # 检查用户是否想用记事本功能
    elif "记事本" in user_input:
        print(f"小P：好的，正在为你打开记事本功能...")
        # 调用 jishiben.py 文件中的 run_notepad() 函数
        小P的超级记事本.jishiben.run_notepad()
        print(f"\n小P：记事本已关闭。我们继续聊天吧！")

    elif "吹牛" in user_input:
        print(f"小P：好的，正在为你打开记吹牛功能...")
        # 调用吹牛py文件中的函数
？？？？？？？？？？？？？？？？？？？？？
        print(f"\n小P：吹牛模式已关闭。我们继续聊天吧！")

    # 如果不是特殊指令，就用之前的方式回答
    elif user_input in responses:
        print(f"小P：{responses[user_input]}")
    elif "你好" in user_input:
        print("小P：你好呀！很高兴认识你！")
    else:
        print("小P：嗯...我现在还只会简单的问候和打开记事本，以后我会学更多本领的！")