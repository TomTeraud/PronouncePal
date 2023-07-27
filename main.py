import os
import openai

# Read the API key from the .env file
with open(".env", "r") as f:
    for line in f:
        if line.startswith("OPENAI_API_KEY"):
            api_key = line.split("=")[1].strip()

# Set the API key
openai.api_key = api_key

# Path to the audio file
audio_file_path = "/home/toms/code/audio-to-text/demo.mp4"

# Ensure the audio file exists
if not os.path.exists(audio_file_path):
    print("Error: Audio file not found.")
    exit()

# Open the audio file in binary read mode
with open(audio_file_path, "rb") as audio_file:
    # Transcribe the audio using the specified engine ID
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

# Print the transcript
print(transcript)
