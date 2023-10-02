import os


class SetupManager:
    openai_key_set = False
    openai_api_selected = False
    alternative_api_set = True
    alternative_api_selected = False
    transcriber_selected = False     

    @classmethod
    def check_app_setup_state(cls):
        cls.check_openai_key()
        if cls.transcriber_selected is True:
            return True
        else:
            return False

    @classmethod
    def check_openai_key(cls):
        # Check if OpenAI API key is set
        if os.environ.get("OPENAI_API_KEY"):
            cls.openai_key_set = True
        else:
            cls.openai_key_set = False

    @classmethod
    def toggle_openai_api_selected(cls):
        cls.openai_api_selected = not cls.openai_api_selected
        if cls.openai_api_selected:
            cls.alternative_api_selected = False    

    @classmethod
    def toggle_alternative_selected(cls):
        cls.alternative_api_selected = not cls.alternative_api_selected
        if cls.alternative_api_selected:
            cls.openai_api_selected = False