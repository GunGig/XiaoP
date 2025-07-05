import pvporcupine
import pyaudio
import numpy as np
import os

def wait_for_wakeup(access_key="YOUR_ACCESS_KEY_HERE"):
    """
    等待唤醒词“你好皮皮”，检测到后返回
    :param access_key: Picovoice 控制台获取的 Access Key
    """
    keyword_path = os.path.join(os.path.dirname(__file__), "ni_hao_pi_pi_windows.ppn")
    model_path = os.path.join(os.path.dirname(__file__), "porcupine_params_zh.pv")  # 指定中文模型
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=[keyword_path],
        model_path=model_path
    )
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )
    print("请说唤醒词：你好皮皮 ...")
    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = np.frombuffer(pcm, dtype=np.int16)
            result = porcupine.process(pcm)
            if result >= 0:
                print("唤醒成功！")
                break
    finally:
        audio_stream.stop_stream()
        audio_stream.close()
        pa.terminate()
        porcupine.delete()