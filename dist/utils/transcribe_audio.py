import os
import openai
from config import engine_id, file_path


class Transcriber:
    @classmethod
    def transcribe_audio(cls, callback=None):
        api_key = os.environ.get("OPENAI_API_KEY")

        try:
            openai.api_key = api_key  # Get the API key
            with open(file_path, "rb") as audio_file:
                response = openai.Audio.transcribe(engine_id, audio_file)
                transcribed_text = response["text"]

                if callback:
                    callback(transcribed_text)  # Call the callback with the transcribed text

                return transcribed_text
        except openai.error.OpenAIError as e:
            print("Transcription failed:", e)
            return None
