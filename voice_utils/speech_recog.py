import pyaudio
from vosk import Model, KaldiRecognizer
import json
import os

MODEL_PATH = "voice_utils/vosk-model-small-cn-0.22"

def voice_input(timeout=5):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Vosk模型未找到，请将模型解压到 {MODEL_PATH}")
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, 16000)
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    print("请开始说话...")

    result = ""
    try:
        for _ in range(0, int(16000 / 8000 * timeout)):
            data = stream.read(8000, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                res = json.loads(recognizer.Result())
                result = res.get("text", "")
                break
        else:
            res = json.loads(recognizer.FinalResult())
            result = res.get("text", "")
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
    print(f"识别结果：{result}")
    return result