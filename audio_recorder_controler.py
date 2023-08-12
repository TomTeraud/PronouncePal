import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import threading
import time
from config import file_path
from utils.transcribe_audio import transcribe_audio

class AudioRecorderController:
    def __init__(self, text_sample):
        """
        Initialize the AudioRecorderController.

        Args:
            text_sample (TextSample): An instance of the TextSample class.
        """
        self.audio_data = None
        self.recording = False
        self.file_path = file_path
        self.text_sample = text_sample
        self.transcribed_text = None
        self.start_transcribtion = transcribe_audio

    def start_recording(self):
        """
        Start the audio recording process and automatically stop after recording_duration.
        """
        self.recording_duration = self.text_sample.sec_to_read  # Update recording duration based on the current text sample
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

        # Perform transcription after stopping recording
        self.transcribed_text = self.start_transcribtion()
        print(f"TRANSCRIBED TEXT IN AUD_REC_CONTROL: {self.transcribed_text}")
    def is_recording(self):
        """
        Check if the audio recording is currently in progress.

        Returns:
            bool: True if recording is in progress, False otherwise.
        """
        return self.recording
