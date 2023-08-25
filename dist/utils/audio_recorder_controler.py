import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import threading
import time
from config import file_path


class AudioRecorderController:
    def __init__(self, text_sample):
        """
        Initialize the AudioRecorderController.

        Args:
            text_sample (TextSample): An instance of the TextSample class.
        """
        self.audio_data = None
        self.callback = None
        self.file_path = file_path
        self.text_sample = text_sample

    def set_callback(self, callback):
        """
        Set the callback function to be executed after recording is stopped.

        Args:
            callback (function): The callback function.
        """
        self.callback = callback


    @classmethod
    def start_recording(cls, text_sample, callback):
        """
        Start the audio recording process and automatically stop after recording_duration.

        Args:
            text_sample (TextSample): An instance of the TextSample class.
            callback (function): The callback function.
        """
        recording_duration = text_sample.sec_to_read
        audio_data = sd.rec(int(recording_duration * 44100), samplerate=44100, channels=1, dtype=np.int16)
        
        # Create a separate thread to handle the recording process
        recording_thread = threading.Thread(target=cls._wait_and_stop_recording, args=(audio_data, recording_duration, callback))
        recording_thread.start()

    @staticmethod
    def _wait_and_stop_recording(audio_data, recording_duration, callback):
        # Wait for recording_duration seconds and then stop the recording
        time.sleep(recording_duration)
        sd.wait()
        wav_data = np.array(audio_data, dtype=np.int16)
        wavfile.write(file_path, 44100, wav_data)
        if callback:
            callback()
