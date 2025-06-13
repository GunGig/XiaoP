# 词语提示列表
word_prompts = [
    "一个形容词 (如：勇敢的)",
    "一个人物类型 (如：公主、巫师)",
    "一个人物名字",
    "再一个形容词 (如：魔法的)",
    "一个地点 (如：森林)",
    "一个动词 (如：寻找)",
    "一个名词 (如：宝藏)"
]

user_words = []  # 创建一个空列表，用来存放用户输入的词

print("--- 请按提示输入词语 ---")
for prompt in word_prompts:
    word = input(f"{prompt}: ")
    user_words.append(word)  # 将用户输入的词添加到列表中

print(f"\n你提供的词语是：{user_words}")

# 如何将 user_words 里的词填入故事？
# 方法1: 确保列表顺序和模板空位顺序一致，然后逐个取出
story = f"很久很久以前，有一位{user_words[0]}的{user_words[1]}，名叫{user_words[2]}。Ta住在一个{user_words[3]}的{user_words[4]}。有一天，Ta决定去{user_words[5]}一个神秘的{user_words[6]}。"

print("\n--- 你的精彩故事 (列表版) ---")
print(story)
print("-----------------------------")