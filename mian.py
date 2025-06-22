# mian.py
# creator：XianSong_Lin
# Time in 2025/6/5 15:27

import csv
import random

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
    import api_services.api_handler

    api_module_found = True
except ImportError:
    print("警告：未能找到 'API服务' 模块。天气功能将不可用。")
    api_module_found = False


# --- 新增功能1：从CSV文件加载城市编码 ---
def load_city_adcodes(filename="AMap_adcode_citycode.csv"):
    """
    在程序启动时，从CSV文件中读取所有城市名和adcode，存入一个字典。
    这样我们就不需要每次都去读文件，程序会运行得更快！
    """
    adcode_map = {}
    try:
        # 使用'utf-8'编码打开文件，以正确读取中文
        with open(filename, mode='r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            next(reader)  # 跳过第一行，因为它是表头 (中文名, adcode, citycode)

            # 遍历文件的每一行数据
            for row in reader:
                # 假设CSV文件的第一列是中文名，第二列是adcode
                # .strip()可以去掉两边的多余空格
                city_name = row[0].strip()
                adcode = row[1].strip()

                # 确保城市名和adcode都不是空的
                if city_name and adcode:
                    # 将城市名作为键，adcode作为值，存入字典
                    # 我们去掉城市名中的'市'、'县'、'区'，让匹配更容易
                    # 比如用户输入"北京"，也能匹配到"北京市"
                    cleaned_city_name = city_name.replace('市', "")
                    adcode_map[cleaned_city_name] = adcode

                    # 为了能同时匹配 "北京市" 和 "北京"，我们把带"市"的也加进去
                    if city_name.endswith('市'):
                        adcode_map[city_name] = adcode

        print(f"成功从 {filename} 加载了 {len(adcode_map)} 个城市/地区编码。")
        return adcode_map
    except FileNotFoundError:
        print(f"错误：找不到城市编码文件 '{filename}'！请确保它和mian.py在同一个文件夹下。")
        return {}  # 返回一个空字典
    except Exception as e:
        print(f"读取城市编码文件 '{filename}' 时发生错误：{e}")
        return {}


# --- 新增功能2：在用户的问话中找到城市 ---
def find_city_in_query(user_input, adcode_map):
    """
    遍历我们所有的城市名，看看哪个城市名出现在了用户的问话里。
    """
    for city_name in adcode_map.keys():
        if city_name in user_input:
            # 找到了！返回这个城市的名字和它的adcode
            # print(city_name, adcode_map[city_name])
            return city_name, adcode_map[city_name]
    # 如果找遍了都没找到
    return None, None


# --- 程序启动时执行，加载城市数据 ---
# 这个字典 CITY_ADCODES 会在整个程序运行期间都存在
CITY_ADCODES = load_city_adcodes()

# 1. 给我们的小P起个名字
my_ai_name = "小P助手"

# 2. 小P做自我介绍 (更新)
print(f"你好！我是{my_ai_name}。很高兴认识你！")
print("你可以对我说 '你好'，或者问我 '北京天气怎么样'。")
# 动态生成介绍
if notepad_module_found: print(f"输入 '记事本' 可以使用我的记事本功能。")
if story_module_found: print(f"输入 '讲故事' 或 '吹牛' 可以听我讲故事。")
if api_module_found: print(f"输入 '笑话' 或 '搞笑点' 可以听我讲笑话。")
if magic_module_found: print(f"输入 '随机魔法' 或 '魔法' 可以让我帮你做选择或玩游戏。")
if kb_module_found: print(f"输入 '知识库' 或 '教你' 可以与我的知识库互动。")
print(f"输入 '退出' 或 '再见' 就可以结束聊天。")

# 4. 准备一些简单的固定回复
responses = {
    "你好呀": "你好你好！今天天气真不错！",
    "你叫什么名字": f"我叫{my_ai_name}，很高兴为你服务！",
}

# 5. 创建一个主循环
while True:
    user_input = input("\n你：").strip()

    if user_input.lower() in ["退出", "再见", "bye", "exit"]:
        print(f"小P：好的，下次再聊！拜拜！")
        break

    # --- 天气查询逻辑 (智能版) ---
    # 条件：用户输入了"天气"，并且API模块和城市数据都已成功加载
    elif "天气" in user_input and api_module_found and CITY_ADCODES:
        city_name, adcode = find_city_in_query(user_input, CITY_ADCODES)

        if city_name and adcode:
            print(f"小P：好的，正在为你查询 {city_name} 的天气...")
            weather_info = api_services.api_handler.get_amap_weather(adcode)
            print(f"小P播报：{weather_info}")
        else:
            # 用户提到了"天气"，但我们没能在他的话里找到我们认识的城市
            print("小P：我听到了“天气”，但不太确定你想查询哪个城市呢？你可以试试说“北京天气怎么样”。")

    elif ("笑话" in user_input or "搞笑点" in user_input) and story_module_found:
        print(f"小P：好的，准备听我大显身手吧！")
        joke=api_services.api_handler.get_random_joke()
        print(joke)
        print(f"\n小P：笑话讲完啦！我们继续聊天吧！")

    elif "记事本" in user_input and notepad_module_found:
        print(f"小P：好的，正在为你打开记事本功能...")
        小P的超级记事本.jishiben.run_notepad()
        print(f"\n小P：记事本已关闭。我们继续聊天吧！")

    elif ("吹牛" in user_input or "讲故事" in user_input) and story_module_found:
        print(f"小P：好的，准备听我大显身手吧！")
        gushi.tell_a_story()
        print(f"\n小P：故事讲完啦！我们继续聊天吧！")

    elif ("随机魔法" in user_input or "魔法" in user_input) and magic_module_found:
        print(f"小P：好的，准备好见证奇迹了吗？进入随机魔法屋！")
        random_magic.magic_handler.run_random_magic_menu()
        print(f"\n小P：魔法时间结束。我们继续聊天吧！")

    elif ("知识库" == user_input.lower() or "教你" in user_input) and kb_module_found:
        print(f"小P：好的，我们来探索一下我的知识库吧！")
        local_kb.kb_handler.run_knowledge_menu()
        print(f"\n小P：知识库互动结束。还有其他想聊的吗？")

    else:  # 默认回复逻辑
        found_answer = False
        # 优先检查知识库
        if kb_module_found:
            kb_answer = local_kb.kb_handler.query_knowledge_base(user_input)
            if kb_answer:
                print(f"小P：{kb_answer}")
                found_answer = True

        # 如果知识库没有，再检查预设的简单回复
        if not found_answer:
            if user_input.lower() in responses:
                print(f"小P：{responses[user_input.lower()]}")
                found_answer = True
            elif "你好" in user_input.lower():
                print("小P：你好呀！很高兴认识你！")
                found_answer = True

        # 如果都没有找到答案
        if not found_answer:
            default_responses = [
                "嗯...你说的这个我还在学习中呢。",
                "这个问题有点深奥，我得回去查查书！",
                "你可以试试问我“你会做什么”，或者通过“知识库”功能教我一些新东西哦！",
                "我对这个还不太了解，能换个话题吗？"
            ]
            print(f"小P：{random.choice(default_responses)}")