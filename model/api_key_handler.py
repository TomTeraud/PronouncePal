import requests
import os


class OpenaiApiKeyHandler:
    @classmethod
    def write_key_in_env_file(cls, api_key:str) -> bool:
        try:
            with open(".env", "a") as env_file:
                env_file.write(f"\nOPENAI_API_KEY={api_key}")
                return True
        except:
            return False

    @staticmethod
    def validate_key(api_key: str) -> bool:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.get("https://api.openai.com/v1/engines", headers=headers)
        return response.status_code == 200
    
    @staticmethod
    def openai_api_key_status() -> bool:
        return bool(os.environ.get("OPENAI_API_KEY"))