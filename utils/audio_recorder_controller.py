import sounddevice as sd
import numpy as np
import wave
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
        self.text_sample = text_sample

    def set_callback(self, callback):
        """
        Set the callback function to be executed after recording is stopped.

        Args:
            callback (function): The callback function.
        """
        self.callback = callback


    @classmethod
    def check_microphone(cls):
        try:
            input_devices = sd.query_devices(kind='input')
        except sd.PortAudioError as query_error:
            print(f"Error querying input devices: {query_error}")
            return False

        if not input_devices:
            print("No available input devices.")
            return False

        return True

    @classmethod
    def start_recording(cls, text_sample, callback):
        recording_duration = text_sample.sec_to_read

        try:
            audio_data = sd.rec(int(recording_duration * 44100), samplerate=44100, channels=1, dtype=np.int16)
            recording_thread = threading.Thread(target=cls._wait_and_stop_recording, args=(audio_data, recording_duration, callback))
            recording_thread.start()
        except sd.PortAudioError as audio_error:
            error_message = f"An error occurred with audio input: {audio_error}"
            print(error_message)
            if callback:
                callback()

    @staticmethod
    def _wait_and_stop_recording(audio_data, recording_duration, callback):
        # Wait for recording_duration seconds and then stop the recording
        time.sleep(recording_duration)
        sd.wait()
        
        # Convert the audio data to a NumPy array of dtype int16
        wav_data = np.array(audio_data, dtype=np.int16)
        
        # Create a WAV file and write audio data to it
        with wave.open(file_path, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Mono channel
            wav_file.setsampwidth(2)  # 16-bit audio (2 bytes per sample)
            wav_file.setframerate(44100)  # Sample rate
            wav_file.writeframes(wav_data.tobytes())
        
        if callback:
            callback()