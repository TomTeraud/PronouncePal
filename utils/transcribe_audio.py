import openai
from config import engine_id, file_path
import os
from dotenv import load_dotenv

class Transcriber:
    def __init__(self):
        self.api_key = self.get_api_key()
        openai.api_key = self.api_key
        self.transcribed_text = None
        self.is_transcribing = False


    def set_callback(self, callback):
        """
        Set the callback function to be executed after transcription is finished.

        Args:
            callback (function): The callback function.
        """
        self.callback = callback


    def get_api_key(self):
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


    def transcribe_audio(self, callback=None):
        """
        Transcribes the audio from the given file path using the OpenAI API.
        Returns:
            str: Transcribed text if successful, else None.
        """
        try:
            self.is_transcribing = True
            with open(file_path, "rb") as audio_file:
                response = openai.Audio.transcribe(engine_id, audio_file)
                # Extract the transcribed text from the JSON response
                self.transcribed_text = response["text"]
                print(f"Transcribed text: {self.transcribed_text}")
                return self.transcribed_text
        except openai.error.OpenAIError as e:
            print("Transcription failed:", e)
            self.transcribed_text = None
            return None
        finally:
            self.is_transcribing = False
            
            # Call the provided callback function if it's provided
            if callback:
                callback()  # Call the callback function