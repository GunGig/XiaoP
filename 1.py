# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-da89d7b109754732a009f30bce6b131a", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=True
)

for chunk in response:
    # 检查每个数据块中是否有内容
    if chunk.choices[0].delta.content is not None:
        # 使用yield关键字，像吐泡泡一样把一小块内容吐出去
        print(chunk.choices[0].delta.content,end="")