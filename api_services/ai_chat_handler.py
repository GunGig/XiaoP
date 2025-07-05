# ai_chat_handler.py
# 模块职责：封装所有与 DeepSeek AI 的交互，提供简单的调用接口。

# 导入与 OpenAI API 格式兼容的库
from openai import OpenAI

# --- 配置AI聊天 ---

# 将API Key直接写入代码中。
# 这种方式最直接，适合个人项目或内部使用。
API_KEY = "sk-da89d7b109754732a009f30bce6b131a"

# DeepSeek API的固定地址
BASE_URL = "https://api.deepseek.com"

# 将客户端对象设为全局变量，初始化后可以在模块内共享，避免重复创建
client = None


def initialize_ai_chat():
    """
    初始化AI聊天客户端。
    这个函数应该在主程序(main.py)启动时被调用一次。
    它会检查API Key是否有效，并尝试创建一个可用的API客户端。

    返回:
        bool: 如果初始化成功，返回 True；否则返回 False。
    """
    global client

    # 检查API Key是否已填写
    # （注意：这里不再检查Key是否为默认占位符，因为你已经填入了自己的Key）
    if API_KEY:
        try:
            # 创建OpenAI客户端实例，配置api_key和base_url
            client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
            # 这里的打印信息会显示在主程序的终端上，告知用户初始化状态
            print("AI聊天核心（DeepSeek）初始化成功！")
            return True
        except Exception as e:
            # 如果创建客户端时发生任何错误（如网络问题、库版本问题）
            print(f"错误：初始化AI聊天客户端失败 - {e}")
            return False
    else:
        # 如果API Key是空的
        print("警告：没有找到有效的DeepSeek API Key。AI对话功能将不可用。")
        return False


def get_ai_response_stream(user_input, chat_history):
    """
    以流式方式获取AI的回复。
    这个函数是一个“生成器”，它不会一次性返回所有答案，
    而是像水龙头一样，持续地、一块一块地“产出”(yield)AI的回复片段。

    参数:
        user_input (str): 用户当前输入的问题。
        chat_history (list): 包含过去对话历史的列表。

    产出(Yields):
        str: AI回复的一小部分文本片段。
    """
    # 检查客户端是否已成功初始化。如果未初始化，直接返回一条错误信息。
    if client is None:
        yield "抱歉，我的AI大脑还没有初始化，无法进行深度对话。"
        return  # 使用return来正确地结束一个生成器函数

    # 准备要发送给API的消息列表
    # 1. 添加一个"system"角色的消息，这可以给AI设定一个基本的人设。
    messages = [{"role": "system", "content": "你是一个名为“小P”的乐于助人的AI助手，你的回答应该简洁、友好、适合青少年。"}]

    # 2. 将传入的对话历史扩展到消息列表中
    messages.extend(chat_history)

    # 3. 将用户最新的问题作为"user"角色的消息追加到列表末尾
    messages.append({"role": "user", "content": user_input})

    try:
        # 调用客户端的 chat.completions.create 方法来发起请求
        # stream=True 是实现流式输出的关键！
        stream = client.chat.completions.create(
            model="deepseek-chat",  # 使用DeepSeek的聊天模型
            messages=messages,  # 传入我们精心准备的消息列表
            stream=True,  # 开启流式输出
            max_tokens=200,  # 限制AI单次回复的最大长度，防止失控
            temperature=0.7  # 控制AI回答的创造性，0.7是一个比较均衡的值
        )

        # 遍历从API返回的数据流对象
        for chunk in stream:
            # 每个chunk是一个数据块，我们需要检查里面是否有我们想要的内容
            if chunk.choices[0].delta.content is not None:
                # 如果有内容，就用yield关键字把它“产出”给调用者
                yield chunk.choices[0].delta.content

    except Exception as e:
        # 如果在API调用过程中发生任何错误（如网络超时、API Key失效等）
        print(f"\n[错误：调用AI聊天API时出错 - {e}]")
        # 同样使用yield返回一条用户友好的错误信息
        yield "抱歉，我的AI大脑暂时连接不上，请稍后再试。"


# 这部分代码 (if __name__ == '__main__':) 仅在直接运行此文件时执行。
# 这是一种非常好的编程习惯，可以让你单独测试这个模块的功能，而不会影响到其他程序。
if __name__ == '__main__':
    print("--- 正在单独测试 ai_chat_handler.py 模块 ---")

    # 先尝试初始化
    if initialize_ai_chat():
        # 初始化成功后，进入一个简单的测试循环
        history = []
        while True:
            user_text = input("\n你 (测试模式): ")
            if user_text.lower() in ["退出", "exit"]:
                break

            print("小P (AI): ", end="", flush=True)

            full_response = ""
            # 调用本文件内的函数进行测试
            for chunk in get_ai_response_stream(user_text, history):
                print(chunk, end="", flush=True)
                full_response += chunk
            print()  # 换行

            # 更新测试用的历史记录
            history.append({"role": "user", "content": user_text})
            history.append({"role": "assistant", "content": full_response})
            # 保持历史记录的长度
            if len(history) > 6:
                history = history[-6:]
    else:
        # 如果初始化失败，打印提示信息
        print("AI聊天客户端初始化失败。无法进入测试模式。")