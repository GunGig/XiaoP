# mian.py
# creator：XianSong_Lin
# Time in 2025/6/5 15:27 (已集成AI大脑)

import csv
import random
from voice_utils.wakeup import wait_for_wakeup
from voice_utils.speech_recog import voice_input
from voice_utils.tts import voice_output
# 设置printPro函数将普通print替换
def printPro(txt):
    print(txt)
    voice_output(txt)


# --- 导入我们自己的所有功能模块 ---
try:
    import 小P的超级记事本.jishiben

    notepad_module_found = True
except ImportError:
    print("警告：未能找到 '记事本' 模块。")
    notepad_module_found = False

try:
    import 小P是故事大王.gushidawang as gushi

    story_module_found = True
except ImportError:
    print("警告：未能找到 '故事大王' 模块。")
    story_module_found = False

try:
    import random_magic.magic_handler

    magic_module_found = True
except ImportError:
    print("警告：未能找到 '随机魔法' 模块。")
    magic_module_found = False

try:
    import local_kb.kb_handler

    kb_module_found = True
except ImportError:
    print("警告：未能找到 '本地知识库' 模块。")
    kb_module_found = False

# 新增API模块的导入
try:
    import api_services.api_tianqi_xiaohua

    api_module_found = True
except ImportError:
    print("警告：未能找到 'API服务' 模块。天气功能将不可用。")
    api_module_found = False

# <-- 关键改动 1：导入我们的AI聊天模块 ---
try:
    from api_services import ai_chat_handler

    ai_chat_module_found = True
except ImportError:
    print("警告：未能找到 'ai_chat_handler.py' 模块。智能对话功能将不可用。")
    ai_chat_module_found = False


# --- 新增功能1：从CSV文件加载城市编码 (原始代码，保持不变) ---
def load_city_adcodes(filename="AMap_adcode_citycode.csv"):
    adcode_map = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                city_name = row[0].strip()
                adcode = row[1].strip()
                if city_name and adcode:
                    cleaned_city_name = city_name.replace('市', "")
                    adcode_map[cleaned_city_name] = adcode
                    if city_name.endswith('市'):
                        adcode_map[city_name] = adcode
        print(f"成功从 {filename} 加载了 {len(adcode_map)} 个城市/地区编码。")
        return adcode_map
    except FileNotFoundError:
        print(f"错误：找不到城市编码文件 '{filename}'！请确保它和mian.py在同一个文件夹下。")
        return {}
    except Exception as e:
        print(f"读取城市编码文件 '{filename}' 时发生错误：{e}")
        return {}


# --- 新增功能2：在用户的问话中找到城市 (原始代码，保持不变) ---
def find_city_in_query(user_input, adcode_map):
    for city_name in adcode_map.keys():
        if city_name in user_input:
            return city_name, adcode_map[city_name]
    return None, None


# --- 程序启动时执行 ---
CITY_ADCODES = load_city_adcodes()
my_ai_name = "小P助手"

# <-- 关键改动 2：在程序启动时，初始化AI聊天核心 ---
ai_chat_initialized = False
if ai_chat_module_found:
    # 调用 ai_chat_handler.py 中的初始化函数
    ai_chat_initialized = ai_chat_handler.initialize_ai_chat()

# <-- 关键改动 3：创建聊天历史记录列表 ---
# 这个列表将保存对话上下文，让AI能理解前因后果
chat_history = []

# 2. 小P做自我介绍 (更新了欢迎语)
print("-" * 30)
voice_output(f"你好！我是{my_ai_name}。很高兴认识你！")
voice_output("你可以对我说 '你好'，或者问我 '北京天气怎么样'。")
# 动态生成介绍
if notepad_module_found: print(f"输入 '记事本' 可以使用我的记事本功能。")
if story_module_found: print(f"输入 '讲故事' 或 '吹牛' 可以听我讲故事。")
if api_module_found: print(f"输入 '笑话' 或 '搞笑点' 可以听我讲笑话。")
if magic_module_found: print(f"输入 '随机魔法' 或 '魔法' 可以让我帮你做选择或玩游戏。")
if kb_module_found: print(f"输入 '知识库' 或 '教你' 可以与我的知识库互动。")
# 根据AI大脑是否启动成功，显示不同信息
if ai_chat_initialized:
    print("我现在拥有了强大的AI大脑，可以进行更复杂的自由对话了！")
else:
    print("（提示：我的AI大脑今天好像没连上线，只能进行预设的简单问答。）")
voice_output(f"输入 '退出' 或 '再见' 就可以结束聊天。")
print("-" * 30)

# 4. 准备一些简单的固定回复 (原始代码，保持不变)
responses = {
    "你好呀": "你好你好！今天天气真不错！",
    "你叫什么名字": f"我叫{my_ai_name}，很高兴为你服务！",
}

# 5. 创建一个主循环
while True:
    user_input = input("\n你：").strip()

    if user_input.lower() in ["退出", "再见", "bye", "exit"]:
        voice_output(f"小P：好的，下次再聊！拜拜！")
        break

    # --- 优先处理所有预设的功能模块 ---
    # 天气查询逻辑 (智能版)
    if "天气" in user_input and api_module_found and CITY_ADCODES:
        city_name, adcode = find_city_in_query(user_input, CITY_ADCODES)
        if city_name and adcode:
            voice_output(f"小P：好的，正在为你查询 {city_name} 的天气...")
            weather_info = api_services.api_handler.get_amap_weather(adcode)
            response_text = f"播报：{weather_info}"  # <-- 存为变量
            voice_output(f"小P：{response_text}")
            # <-- 关键改动 4a：将有效的本地功能问答也加入历史记录 ---
            chat_history.append({"role": "user", "content": user_input})
            chat_history.append({"role": "assistant", "content": response_text})
        else:
            voice_output("小P：我听到了“天气”，但不太确定你想查询哪个城市呢？你可以试试说“北京天气怎么样”。")

    elif ("笑话" in user_input or "搞笑点" in user_input) and api_module_found:  # 注意：笑话功能依赖api_handler
        voice_output(f"小P：好的，准备听我大显身手吧！")
        joke = api_services.api_tianqi_xiaohua.get_random_joke()
        voice_output(joke)
        voice_output(f"\n小P：笑话讲完啦！我们继续聊天吧！")
        # 笑话这种单次互动可以不加入历史，以免干扰后续对话

    elif "记事本" in user_input and notepad_module_found:
        voice_output(f"小P：好的，正在为你打开记事本功能...")
        小P的超级记事本.jishiben.run_notepad()
        voice_output(f"\n小P：记事本已关闭。我们继续聊天吧！")

    elif ("吹牛" in user_input or "讲故事" in user_input) and story_module_found:
        voice_output(f"小P：好的，准备听我大显身手吧！")
        gushi.tell_a_story()
        voice_output(f"\n小P：故事讲完啦！我们继续聊天吧！")

    elif ("随机魔法" in user_input or "魔法" in user_input) and magic_module_found:
        voice_output(f"小P：好的，准备好见证奇迹了吗？进入随机魔法屋！")
        random_magic.magic_handler.run_random_magic_menu()
        voice_output(f"\n小P：魔法时间结束。我们继续聊天吧！")

    elif ("知识库" == user_input.lower() or "教你" in user_input) and kb_module_found:
        voice_output(f"小P：好的，我们来探索一下我的知识库吧！")
        local_kb.kb_handler.run_knowledge_menu()
        voice_output(f"\n小P：知识库互动结束。还有其他想聊的吗？")

    # <-- 关键改动 5：修改最终的 else 兜底逻辑 ---
    else:
        found_answer = False

        # 1. 优先检查知识库的直接查询
        if kb_module_found:
            kb_answer = local_kb.kb_handler.query_knowledge_base(user_input)
            if kb_answer:
                voice_output(f"小P：{kb_answer}")
                chat_history.append({"role": "user", "content": user_input})
                chat_history.append({"role": "assistant", "content": kb_answer})
                found_answer = True

        # 2. 如果知识库没有，再检查预设的简单回复
        if not found_answer:
            response_text = ""
            if user_input.lower() in responses:
                response_text = responses[user_input.lower()]
            elif "你好" in user_input.lower():
                response_text = "你好呀！很高兴认识你！"

            if response_text:
                voice_output(f"小P：{response_text}")
                chat_history.append({"role": "user", "content": user_input})
                chat_history.append({"role": "assistant", "content": response_text})
                found_answer = True

        # 3. 如果以上所有规则都未命中，并且AI大脑已初始化，则调用AI！
        if not found_answer and ai_chat_initialized:
            print("小P (正在深度思考中): ", end="", flush=True)

            full_response = ""
            # 调用AI模块的流式接口，并传入历史记录
            response_stream = ai_chat_handler.get_ai_response_stream(user_input, chat_history)

            for chunk in response_stream:
                voice_output(chunk, end="", flush=True)
                full_response += chunk
            print()  # 打印完后换行

            # 只有在AI真的回复了内容时才更新历史
            if full_response.strip():
                chat_history.append({"role": "user", "content": user_input})
                chat_history.append({"role": "assistant", "content": full_response})

            found_answer = True  # 标记已找到答案

        # 4. 如果连AI都失败了，或者AI模块未加载，才使用最终的随机回复 (原始代码)
        if not found_answer:
            default_responses = [
                "嗯...你说的这个我还在学习中呢。",
                "这个问题有点深奥，我得回去查查书！",
                "你可以试试问我“你会做什么”，或者通过“知识库”功能教我一些新东西哦！",
                "我对这个还不太了解，能换个话题吗？"
            ]
            voice_output(f"小P：{random.choice(default_responses)}")

    # <-- 关键改动 6：管理历史记录长度 ---
    # 在每次循环结束后，检查并修剪历史记录，防止内存占用过大
    if len(chat_history) > 6:  # 保留最近3轮对话（3*2=6条）
        chat_history = chat_history[-6:]