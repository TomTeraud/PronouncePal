import os
from dotenv import load_dotenv

def get_api_key():
    # Get the OpenAI API key from the environment variable
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OpenAI API key not found in environment variable (OPENAI_API_KEY).")
        return None
    return api_key
