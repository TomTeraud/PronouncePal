import openai
from config import engine_id, file_path
import os
from dotenv import load_dotenv

class Transcriber:
    @staticmethod
    def get_api_key():
        """
        Get the OpenAI API key from the .env file or user input.
        Returns:
            str: The API key.
        """
        load_dotenv()

        # Try to load the API key from the .env file
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            return api_key

        # Ask the user to enter the API key in the console
        api_key = input("Enter your OpenAI API key: ").strip()
        if not api_key:
            print("Error: API key is required.")
            return None

        # Save the entered API key to the .env file for future use
        with open(".env", "a") as env_file:
            env_file.write(f"\nOPENAI_API_KEY={api_key}")

        return api_key

    @classmethod
    def transcribe_audio(cls, callback=None):
        try:
            api_key = cls.get_api_key()  # Get the API key

            if api_key:
                openai.api_key = api_key  # Set the API key

                with open(file_path, "rb") as audio_file:
                    response = openai.Audio.transcribe(engine_id, audio_file)
                    transcribed_text = response["text"]
                    print(f"Transcribed text: {transcribed_text}")

                    if callback:
                        callback(transcribed_text)  # Call the callback with the transcribed text

                    return transcribed_text
        except openai.error.OpenAIError as e:
            print("Transcription failed:", e)
            return None
