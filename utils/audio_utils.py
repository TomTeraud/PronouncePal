import sounddevice as sd
import numpy as np
from scipy.io import wavfile

def record_audio(file_path, duration=3):
    print(f"Recording audio for {duration} seconds... (Please speak)")
    audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype=np.int16)
    sd.wait()
    wav_data = np.array(audio_data, dtype=np.int16)
    wavfile.write(file_path, 44100, wav_data)
