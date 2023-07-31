import sounddevice as sd
import numpy as np
from scipy.io import wavfile

class AudioRecorderController:
    def __init__(self, file_path, recording_duration):
        """
        Initialize the AudioRecorderController.

        Args:
            file_path (str): Path to the audio file where the recording will be saved.
            recording_duration (float): Duration of the audio recording in seconds.
        """
        self.audio_data = None
        self.recording = False
        self.file_path = file_path
        self.recording_duration = recording_duration

    def start_recording(self):
        """
        Start the audio recording process.
        """
        self.recording = True
        self.audio_data = sd.rec(int(self.recording_duration * 44100), samplerate=44100, channels=1, dtype=np.int16)

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
