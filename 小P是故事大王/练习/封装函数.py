def tell_a_story():
    print("--- 小P故事大王出场！ ---")
    word_prompts = [
        "一个形容词 (如：勇敢的)", "一个人物类型 (如：公主、巫师)", "一个人物名字",
        "再一个形容词 (如：魔法的)", "一个地点 (如：森林)",
        "一个动词 (如：寻找)", "一个名词 (如：宝藏)"
    ]
    user_words = []

    print("请按提示输入词语来创作故事：")
    for prompt in word_prompts:
        word = input(f"{prompt}: ")
        user_words.append(word)

    # 假设我们知道 user_words 中词语的顺序
    story = f"""
    很久很久以前，
    有一位{user_words[0]}的{user_words[1]}，名叫{user_words[2]}。
    Ta住在一个{user_words[3]}的{user_words[4]}。
    有一天，Ta决定去{user_words[5]}一个神秘的{user_words[6]}。
    哇，这真是一个精彩的冒险！
    """  # 使用三引号可以写多行字符串

    print("\n--- 小P为你讲述的专属故事 ---")
    print(story)
    print("-----------------------------")

# 测试函数
tell_a_story()