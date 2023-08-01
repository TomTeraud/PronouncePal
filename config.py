import os

# Recording configuration
file_path = "audio_recording.wav"
recording_duration = 2

# API key configuration
api_key = os.environ.get("OPENAI_API_KEY")

# Engine ID for audio transcription
engine_id = "whisper-1"  # Replace with your desired engine ID

# Set db name
DATABASE = 'your_database.db'