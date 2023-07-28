import os

def get_api_key(api_key_string=None):
    if api_key_string is None:
        # Get the API key from environment variable if None provided
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            print("Error: API key not found in environment variable (OPENAI_API_KEY).")
            exit()
    else:
        api_key = api_key_string

    return api_key
