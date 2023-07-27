import os
import openai
import sounddevice as sd
import numpy as np
from dotenv import load_dotenv
from scipy.io import wavfile

# Load environment variables from .env file
load_dotenv()

# Function to record audio
def record_audio(file_path, duration=5):
    print(f"Recording audio for {duration} seconds... (Please speak)")
    audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype=np.int16)
    sd.wait()
    wav_data = np.array(audio_data, dtype=np.int16)
    wavfile.write(file_path, 44100, wav_data)

# Function to get API key from string or environment variable
def get_api_key(api_key_string=None):
    if api_key_string is None:
        # Get the API key from environment variable if None provided
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            print("Error: API key not found in environment variable (OPENAI_API_KEY).")
            exit()
    else:
        api_key = api_key_string

    return api_key

# Set the API key
api_key_string = None  # Replace this string with your actual API key or leave it as None
openai.api_key = get_api_key(api_key_string)


# Prompt the user to record audio
audio_file_path = "/home/toms/code/audio-to-text/temp_audio.wav"
record_audio(audio_file_path)

# Ensure the audio file exists
if not os.path.exists(audio_file_path):
    print("Error: Audio file not found.")
    exit()

# Open the audio file in binary read mode
with open(audio_file_path, "rb") as audio_file:
    # Transcribe the audio using the specified engine ID
    engine_id = "whisper-1"  # Replace this with the appropriate engine ID
    transcript = openai.Audio.transcribe(engine_id, audio_file)

# Print the transcript
print("Transcript:")
print(transcript)
