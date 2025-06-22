# mian.py
# creator：XianSong_Lin
# Time in 2025/6/5 15:27

# 导入我们自己的模块
# 注意：这里的导入路径是基于 mian.py 在 XiaoP 根目录，
# 并且模块文件夹也在 XiaoP 根目录。
try:
    # 你的现有导入，确保它们能正常工作
    import 小P的超级记事本.jishiben  # 如果 jishiben.py 在 XiaoP/小P的超级记事本/ 目录下

    notepad_module_found = True
except ImportError:
    print("警告：未能找到 '记事本' 模块 (小P的超级记事本.jishiben)。")
    notepad_module_found = False

try:
    import 小P是故事大王.gushidawang as gushi  # 如果 gushidawang.py 在 XiaoP/小P是故事大王/ 目录下

    story_module_found = True
except ImportError:
    print("警告：未能找到 '故事大王' 模块 (小P是故事大王.gushidawang)。")
    story_module_found = False

# 新增导入
try:
    import random_magic.magic_handler  # 从 XiaoP/random_magic/ 目录导入 magic_handler.py

    magic_module_found = True
except ImportError:
    print("警告：未能找到 '随机魔法' 模块 (random_magic.magic_handler)。该功能可能不可用。")
    magic_module_found = False

try:
    import local_kb.kb_handler  # 从 XiaoP/local_kb/ 目录导入 kb_handler.py

    kb_module_found = True
except ImportError:
    print("警告：未能找到 '本地知识库' 模块 (local_kb.kb_handler)。该功能可能不可用。")
    kb_module_found = False

# 1. 给我们的小P起个名字
my_ai_name = "小P助手"

# 2. 小P做自我介绍 (更新)
print(f"你好！我是{my_ai_name}。很高兴认识你！")
print(f"你可以对我说 '你好'。")
if notepad_module_found:
    print(f"输入 '记事本' 可以使用我的记事本功能。")
if story_module_found:
    print(f"输入 '讲故事' 或 '吹牛' 可以听我讲故事。")
if magic_module_found:
    print(f"输入 '随机魔法' 或 '魔法' 可以让我帮你做选择或玩游戏。")
if kb_module_found:
    print(f"输入 '知识库' 或 '问问题' 可以考考我的知识，或者直接问我问题！")
print(f"输入 '退出' 或 '再见' 就可以结束聊天。")

# 4. 准备一些小P能听懂的话和回答
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

    elif "记事本" in user_input and notepad_module_found:
        print(f"小P：好的，正在为你打开记事本功能...")
        小P的超级记事本.jishiben.run_notepad()  # 注意这里的调用方式
        print(f"\n小P：记事本已关闭。我们继续聊天吧！")

    elif ("吹牛" in user_input or "讲故事" in user_input) and story_module_found:
        print(f"小P：好的，准备听我大显身手吧！")
        gushi.tell_a_story()  # 注意这里的调用方式 (gushi 是 as gushi 的别名)
        print(f"\n小P：故事讲完啦！我们继续聊天吧！")

    elif ("随机魔法" in user_input or "魔法" in user_input) and magic_module_found:
        print(f"小P：好的，准备好见证奇迹了吗？进入随机魔法屋！")
        random_magic.magic_handler.run_random_magic_menu()  # 调用新模块的函数
        print(f"\n小P：魔法时间结束。我们继续聊天吧！")

    elif (
            "知识库" == user_input.lower() or "教你" in user_input or "问问题" in user_input and "知识库" not in user_input) and kb_module_found:  # 调整了条件，允许“问问题”直接触发
        if "教你" in user_input or "知识库" == user_input.lower():  # 特定指令进入知识库菜单
            print(f"小P：好的，我们来探索一下我的知识库吧！")
            local_kb.kb_handler.run_knowledge_menu()
            print(f"\n小P：知识库互动结束。还有其他想聊的吗？")
        else:  # 直接问问题，不进入菜单
            kb_answer = local_kb.kb_handler.query_knowledge_base(user_input)
            if kb_answer:
                print(f"小P：{kb_answer}")
            else:
                print("小P：嗯...我对这个还不太了解。你可以试试通过输入“知识库”然后选择“教小P”来教我哦！")

    else:  # 默认回复逻辑
        found_answer = False
        if user_input.lower() in responses:
            print(f"小P：{responses[user_input.lower()]}")
            found_answer = True
        elif "你好" in user_input.lower():
            print("小P：你好呀！很高兴认识你！")
            found_answer = True

        if not found_answer and kb_module_found and "知识库" not in user_input and "教你" not in user_input:  # 避免重复查询
            kb_answer = local_kb.kb_handler.query_knowledge_base(user_input)
            if kb_answer:
                print(f"小P：{kb_answer}")
                found_answer = True

        if not found_answer:
            # 确保 random 模块已导入
            import random

            default_responses = [
                "嗯...你说的这个我还在学习中呢。",
                "这个问题有点深奥，我得回去查查书！",
                "你可以试试问我“你会做什么”，或者通过输入“知识库”然后选择“教小P”来教我一些新东西哦！",
                "我对这个还不太了解，能换个话题吗？"
            ]
            print(f"小P：{random.choice(default_responses)}")
