import pyttsx3

def voice_output(text):
    """
    朗读文本
    """
    engine = pyttsx3.init()
    # 可选：设置语速、音量、声音
    engine.setProperty('rate', 180)    # 语速
    engine.setProperty('volume', 1.0)  # 音量
    # engine.setProperty('voice', ...) # 可选：切换不同声音
    engine.say(text)
    engine.runAndWait()