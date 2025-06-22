# XiaoP/ai_chat/chat_handler.py

from openai import OpenAI

# --- 配置AI聊天 ---
API_KEY = "sk-da89d7b109754732a009f30bce6b131a"
BASE_URL = "https://api.deepseek.com"

client = None


def initialize_ai_chat():
    """初始化AI聊天客户端。"""
    global client
    if API_KEY and API_KEY != "<YOUR_API_KEY>":
        try:
            client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
            return True
        except Exception as e:
            print(f"错误：初始化AI聊天客户端失败 - {e}")
            return False
    else:
        print("警告：没有找到有效的DeepSeek API Key。AI对话功能将不可用。")
        return False


def get_ai_response_stream(user_input, chat_history=None):
    """
    (流式版) 获取AI的回复。
    这个函数会变成一个“生成器”，逐块返回(yield)AI的回复片段。
    """
    if client is None:
        # 如果客户端未初始化，我们也用yield来返回一个错误信息，保持接口一致
        yield "抱歉，我的AI大脑还没有初始化，无法进行深度对话。"
        return  # 必须用return来结束生成器

    if chat_history is None:
        chat_history = []

    messages = [{"role": "system", "content": "你是一个名为“小P”的乐于助人的AI助手，你的回答应该简洁、友好、适合青少年。"}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": user_input})

    try:
        # --- 关键改动：stream=True ---
        stream = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=True,  # 开启流式输出！
            max_tokens=200,
            temperature=0.7
        )

        # 遍历从API返回的数据流
        for chunk in stream:
            # 检查每个数据块中是否有内容
            if chunk.choices[0].delta.content is not None:
                # 使用yield关键字，像吐泡泡一样把一小块内容吐出去
                yield chunk.choices[0].delta.content

    except Exception as e:
        print(f"错误：调用AI聊天API时出错 - {e}")
        yield "抱歉，我的AI大脑暂时连接不上，请稍后再试。"


# --- 主程序入口和测试区 (也需要修改以处理流式输出) ---
if __name__ == '__main__':
    print("--- 开始测试 ai_chat 模块 (流式版) ---")
    if initialize_ai_chat():
        print("AI聊天客户端初始化成功！")

        history = []

        while True:
            user_text = input("\n你: ")
            if user_text.lower() in ["退出", "exit"]:
                break

            print("小P (正在思考中): ", end="", flush=True)  # 打印前缀，end=""表示不换行

            # --- 关键改动：用 for 循环处理流式返回 ---
            full_response = ""
            # get_ai_response_stream 返回的是一个可以循环的对象
            for chunk in get_ai_response_stream(user_text, history):
                print(chunk, end="", flush=True)  # 打印每个数据块，不换行，并立即显示
                full_response += chunk  # 将数据块拼成完整的回复

            print()  # 打印完所有数据块后，手动换行

            # 更新聊天历史
            history.append({"role": "user", "content": user_text})
            history.append({"role": "assistant", "content": full_response})  # 存入完整的回复

            if len(history) > 6:
                history = history[-6:]
    else:
        print("AI聊天客户端初始化失败。")