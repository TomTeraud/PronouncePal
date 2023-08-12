import openai
from utils.openai_utils import get_api_key
from config import engine_id, file_path

# Try to get the API key from .env or prompt the user to enter it
openai.api_key = get_api_key()

def transcribe_audio():
    """
    Transcribes the audio from the given file path using the OpenAI API.
    Returns:
        str: Transcribed text if successful, else None.
    """
    api_key = get_api_key()
    if not api_key:
        return None

    if file_path is None:
        return None

    try:
        # Set the OpenAI API key
        openai.api_key = api_key

        with open(file_path, "rb") as audio_file:
            response = openai.Audio.transcribe(engine_id, audio_file)

        # Extract the transcribed text from the JSON response
        transcript = response["text"]
        return transcript
    except Exception as e:
        print("Transcription failed:", e)
        return None

