import openai
from utils.openai_utils import get_api_key

def transcribe_audio(audio_file_path):
    # Rest of the transcribe_audio() function
    api_key = get_api_key()
    if not api_key:
        return None

    if audio_file_path is None:
        return None

    # Set the OpenAI API key
    openai.api_key = api_key

    with open(audio_file_path, "rb") as audio_file:
        engine_id = "whisper-1"  # Replace with your engine ID
        response = openai.Audio.transcribe(engine_id, audio_file)

    # Extract the transcribed text from the JSON response
    transcript = response["text"]
    return transcript
