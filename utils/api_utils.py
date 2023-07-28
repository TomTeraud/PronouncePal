import os
from dotenv import load_dotenv

def get_api_key():
    # Try to load the API key from the .env file
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    # If the API key is set in the .env file, return it
    if api_key:
        return api_key

    # Check if the API key is set in the file
    default_api_key = "YOUR_DEFAULT_API_KEY"  # Replace this with your actual default API key
    if default_api_key != "YOUR_DEFAULT_API_KEY":
        api_key = default_api_key
    else:
        # If the default API key is not set, ask the user to enter the API key in the console
        api_key = input("Enter your OpenAI API key: ").strip()
        if not api_key:
            print("Error: API key is required.")
            return None

    # Save the entered API key to the .env file for future use
    with open(".env", "a") as env_file:
        env_file.write(f"\nOPENAI_API_KEY={api_key}")

    return api_key
