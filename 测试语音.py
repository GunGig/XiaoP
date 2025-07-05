from voice_utils.wakeup import wait_for_wakeup
from voice_utils.speech_recog import voice_input
from voice_utils.tts import voice_output

if __name__ == "__main__":
    while True:
        wait_for_wakeup(access_key="2afcrqBqA8xDJqTjla22kU7Z3zbBF358EivPzli1AkfakFrswi01Ow==")  # 语音唤醒
        user_text = voice_input()  # 语音转文字
        if not user_text:
            voice_output("没有听清，请再说一遍。")
            continue
        # 这里可以接入你的主逻辑，比如AI对话
        print(f"用户说：{user_text}")
        reply = f"你刚才说的是：{user_text}"
        voice_output(reply)