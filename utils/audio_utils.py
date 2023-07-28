import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import threading


class AudioRecorder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.audio_data = None
        self.recording = False
        self.recording_duration = 2  # Adjust the recording duration as needed

    def start_recording(self):
        self.recording = True
        self.audio_data = sd.rec(int(self.recording_duration * 44100), samplerate=44100, channels=1, dtype=np.int16)

    def stop_recording(self):
        self.recording = False
        sd.wait()
        wav_data = np.array(self.audio_data, dtype=np.int16)
        wavfile.write(self.file_path, 44100, wav_data)

    @property
    def elapsed_time(self):
        return len(self.audio_data) / 44100

    def is_recording(self):
        return self.recording
