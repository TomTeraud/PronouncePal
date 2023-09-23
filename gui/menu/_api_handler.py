from tkinter import simpledialog, messagebox
import requests
from dotenv import load_dotenv

class ApiMenuHandler:
    @classmethod
    def get_api_key(cls):
        api_key = simpledialog.askstring("Input", "Enter your API key:")
        if api_key:
            if cls.validate_api_key(api_key):
                with open(".env", "a") as env_file:
                    env_file.write(f"\nOPENAI_API_KEY={api_key}")
                load_dotenv()
                messagebox.showinfo("Success", "API key set successfully!")
                return True
            else:
                messagebox.showerror("Error", "Invalid API key")
                return False

    @staticmethod
    def validate_api_key(api_key):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.get("https://api.openai.com/v1/engines", headers=headers)
        return response.status_code == 200
