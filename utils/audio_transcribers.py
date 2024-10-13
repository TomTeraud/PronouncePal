import openai
from config import ENGINE_ID, AUDIO_FILE_PATH

class OpenaiTranscriber:
    @classmethod
    def transcribe_audio(cls):

        try:
            with open(AUDIO_FILE_PATH, "rb") as audio_file:

                response = openai.audio.transcriptions.create(
                    model=ENGINE_ID, 
                    file=audio_file,
                    response_format="text"
                )
                return response
        except openai.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
            return e
        except openai.OpenAIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            return e
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return e