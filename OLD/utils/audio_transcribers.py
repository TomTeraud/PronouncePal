import os
import openai
from config import ENGINE_ID, FILE_PATH

class OpenaiTranscriber:
    @classmethod
    def transcribe_audio(cls):
        api_key = os.environ.get("OPENAI_API_KEY") # Get the API key

        try:
            openai.api_key = api_key  
            with open(FILE_PATH, "rb") as audio_file:
                response = openai.Audio.transcribe(ENGINE_ID, audio_file)
                transcribed_text = response["text"]

                return transcribed_text
        except openai.error.RateLimitError as rate_limit_error:
            return rate_limit_error
        except openai.error.OpenAIError as openai_error:
            return openai_error