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
        self.is_recording = False
        self.file_path = file_path
        self.text_sample = text_sample
        self.transcribed_text = None
        self.callback = None

    def set_callback(self, callback):
        """
        Set the callback function to be executed after recording is stopped.

        Args:
            callback (function): The callback function.
        """
        self.callback = callback


    def start_recording(self):
        """
        Start the audio recording process and automatically stop after recording_duration.
        """
        self.is_recording = True
        self.recording_duration = self.text_sample.sec_to_read  # Update recording duration based on the current text sample
        self.audio_data = sd.rec(int(self.recording_duration * 44100), samplerate=44100, channels=1, dtype=np.int16)
        
        # Create a separate thread to handle the recording process
        recording_thread = threading.Thread(target=self._wait_and_stop_recording)
        recording_thread.start()

    def _wait_and_stop_recording(self):
        # Wait for recording_duration seconds and then stop the recording
        time.sleep(self.recording_duration)
        self.stop_recording()


    def stop_recording(self, callback=None):
        """
        Stop the audio recording process and save the recorded audio to the file.

        Args:
            callback (function): Callback function to be executed after recording is stopped.
        """
        sd.wait()
        wav_data = np.array(self.audio_data, dtype=np.int16)
        wavfile.write(self.file_path, 44100, wav_data)
        self.is_recording = False
        if self.callback:
            self.callback()
