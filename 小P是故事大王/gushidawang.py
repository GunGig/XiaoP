# 同学们自行构建最终的故事大王的程序并修改主程序mian的代码，
# 让小p拥有讲故事的功能
import random

import random


def tell_a_story():
    print("--- 小P故事大王出场！ ---")

    # 故事模板列表
    story_templates = [
        lambda w: f"""
        很久很久以前，
        有一位{w[0]}的{w[1]}，名叫{w[2]}。
        Ta住在一个{w[3]}的{w[4]}。
        有一天，Ta决定去{w[5]}一个神秘的{w[6]}。
        哇，这真是一个精彩的冒险！
        """,
        lambda w: f"""
        在一个遥远的国度，
        生活着一位{w[0]}的{w[1]}，大家都叫Ta{w[2]}。
        这个国度被一片{w[3]}的{w[4]}所环绕。
        有一天，{w[1]}听说了一个关于{w[6]}的传说，
        于是毅然踏上了{w[5]}的旅程。
        这注定是一段不平凡的经历！
        """,
        lambda w: f"""
        传说中，
        {w[2]}是一位{w[0]}的{w[1]}，守护着{w[3]}的{w[4]}。
        然而有一天，{w[4]}突然陷入了危机，
        只有找到{w[6]}才能拯救它。
        {w[2]}毫不犹豫地出发{w[5]}，
        一场惊心动魄的冒险就此展开！
        """
    ]

    # 词汇库
    adjectives = ["勇敢的", "聪明的", "善良的", "神秘的", "强大的", "机智的", "可爱的", "顽皮的"]
    character_types = ["公主", "巫师", "骑士", "探险家", "精灵", "魔法师", "猎人", "发明家"]
    names = ["艾丽", "汤姆", "莉莉", "杰克", "露西", "马克", "索菲亚", "亚历克斯"]
    magic_adjectives = ["魔法的", "神奇的", "神秘的", "古老的", "奇幻的", "闪耀的", "诡异的", "宁静的"]
    locations = ["森林", "城堡", "山谷", "岛屿", "洞穴", "山脉", "沙漠", "海底"]
    verbs = ["寻找", "探索", "拯救", "挑战", "解开", "守护", "发现", "研究"]
    nouns = ["宝藏", "秘密", "力量", "神器", "谜题", "传说", "生物", "王国"]

    word_banks = [adjectives, character_types, names, magic_adjectives, locations, verbs, nouns]

    try:
        num_stories = int(input("你想听几个故事？(输入数字): "))
    except ValueError:
        print("请输入有效的数字！")
        return

    for i in range(num_stories):
        print(f"\n--- 故事 {i + 1} ---")

        # 随机选择故事模板
        template = random.choice(story_templates)

        # 随机生成词汇
        user_words = [random.choice(bank) for bank in word_banks]

        # 生成并打印故事
        story = template(user_words)
        print(story)
        print("-------------------")

    print("\n--- 故事讲完啦！希望你喜欢！ ---")


# 测试函数


if __name__ == "__main__":
    tell_a_story()