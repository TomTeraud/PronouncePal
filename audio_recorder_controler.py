import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import threading
import time

class AudioRecorderController:
    def __init__(self, file_path, text_sample):
        """
        Initialize the AudioRecorderController.

        Args:
            file_path (str): Path to the audio file where the recording will be saved.
            text_sample (TextSample): An instance of the TextSample class.
        """
        self.audio_data = None
        self.recording = False
        self.file_path = file_path
        self.recording_duration = text_sample.sec_to_read  

    def start_recording(self):
        print(f"start recording for:{self.recording_duration} sec")
        """
        Start the audio recording process and automatically stop after recording_duration.
        """
        self.recording = True
        self.audio_data = sd.rec(int(self.recording_duration * 44100), samplerate=44100, channels=1, dtype=np.int16)
        
        # Create a separate thread to handle the recording process
        recording_thread = threading.Thread(target=self._wait_and_stop_recording)
        recording_thread.start()

    def _wait_and_stop_recording(self):
        # Wait for recording_duration seconds and then stop the recording
        time.sleep(self.recording_duration)
        self.stop_recording()

    def stop_recording(self):
        """
        Stop the audio recording process and save the recorded audio to the file.
        """
        self.recording = False
        sd.wait()
        wav_data = np.array(self.audio_data, dtype=np.int16)
        wavfile.write(self.file_path, 44100, wav_data)

    def is_recording(self):
        """
        Check if the audio recording is currently in progress.

        Returns:
            bool: True if recording is in progress, False otherwise.
        """
        return self.recording
