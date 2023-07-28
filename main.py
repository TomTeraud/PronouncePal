import os
import openai
from dotenv import load_dotenv
from utils.audio_utils import record_audio
from utils.api_utils import get_api_key

# Load environment variables from .env file
load_dotenv()

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
