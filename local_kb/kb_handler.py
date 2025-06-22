# features/local_kb/kb_handler.py

KNOWLEDGE_BASE = {
    "python是什么": "Python是一种非常流行的编程语言，简单易学，功能强大！我们现在就在用Python来创造我哦！",
    "小p是谁": "我就是小P呀，一个正在学习成长的AI助手，很高兴认识你！",
    "今天天气怎么样": "我现在还不能联网看天气呢，不过你可以问问我别的问题！",
    "我们班有多少人": "这个问题我需要你告诉我答案，然后我就能记住了！下次你问我，我就能回答啦！",
    "你会做什么": "我会和你聊天，帮你记事，讲故事，玩随机魔法，还能回答一些我知道的问题！",
    "你好": "你好呀！很高兴再次和你对话！"  # 知识库内的特定问候
}


def add_knowledge(question, answer):
    """向知识库添加新的问答对 (简单实现，不持久化，程序关闭后会丢失)"""
    question_key = question.lower().strip().replace("？", "").replace("?", "").replace("！", "").replace("!", "")
    if not question_key:
        return "问题不能为空哦！"
    if not answer.strip():
        return "答案不能为空哦！"

    KNOWLEDGE_BASE[question_key] = answer.strip()
    return f"好嘞，我已经记住了：'{question}'的答案是'{answer}'。"


def query_knowledge_base(user_query):
    """根据用户的问题查询知识库。"""
    query_lower = user_query.lower().strip().replace("？", "").replace("?", "").replace("！", "").replace("!", "")

    if not query_lower:
        return None  # 或者返回一个特定提示，由调用者处理

    # 1. 精确匹配
    if query_lower in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[query_lower]

    # 2. 简单的关键词包含匹配 (用户问题包含知识库的某个键)
    for key_question, answer in KNOWLEDGE_BASE.items():
        if key_question in query_lower:
            return answer

    # 3. 更松散的关键词匹配 (知识库键的词语在用户问题中，或反之)
    #    这部分需要更小心处理，避免不相关的匹配，这里简化
    query_words = set(query_lower.split())
    for key_question, answer in KNOWLEDGE_BASE.items():
        key_q_words = set(key_question.split())
        # 如果有共同的词语（忽略太短的词）
        common_words = {w for w in query_words if len(w) > 1}.intersection({w for w in key_q_words if len(w) > 1})
        if common_words:  # 如果有交集，可以认为相关
            # 这里可以根据交集词的数量或重要性来决定是否返回，现在简单返回第一个匹配到的
            return answer

    return None  # 表示没有找到答案


def run_knowledge_menu():
    """本地知识库交互菜单"""
    print("\n🧠 小P的知识库问答 🧠")
    while True:
        print("\n你可以：")
        print("1. 问小P一个问题 (直接在聊天中问也可以)")
        print("2. 教小P新的知识")
        print("0. 返回与小P聊天")

        choice = input("请输入你的选择 (0-2): ").strip()

        if choice == '1':
            user_question = input("你有什么问题想问小P？\n你：")
            answer = query_knowledge_base(user_question)
            if answer:
                print(f"小P：{answer}")
            else:
                print(f"小P：嗯...这个问题我现在还不知道答案呢。也许你可以通过选项2教我？")
        elif choice == '2':
            new_q = input("你想教小P什么问题？\n问题：")
            new_a = input(f"'{new_q}'的答案是什么呢？\n答案：")
            result = add_knowledge(new_q, new_a)
            print(f"小P：{result}")
        elif choice == '0':
            print("已退出知识库问答。")
            break
        else:
            print("无效的选择，请输入0到2之间的数字哦！")


if __name__ == "__main__":
    print("测试本地知识库模块...")
    # run_knowledge_menu()
    print(f"问：Python是什么?  答：{query_knowledge_base('Python?')}")
    print(f"问：小p是谁呀  答：{query_knowledge_base('小p是谁呀')}")
    print(add_knowledge("地球的形状", "地球是一个近似球形的行星。"))
    print(f"问：地球的形状是什么  答：{query_knowledge_base('地球的形状是什么')}")
    print(f"问：hello  答：{query_knowledge_base('hello')}")  # 测试找不到的情况
