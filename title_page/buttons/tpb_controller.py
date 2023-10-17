import os


class ButtonState:
    openai_key_set = False

    openai_state_disabled = False
    openai_selected = False
        
    alter_state_disabled = False
    alter_selected = False
    
    start_app_state = False
    ready_to_start = False     


    @classmethod
    def check_start_state(cls):
        if cls.ready_to_start:
            return True

    @classmethod
    def update_openai_state(cls):
        if cls.alter_selected is False and cls.openai_key_set:
            return True
        else:
            return False

    @classmethod
    def update_alter_state(cls):
        if cls.alter_selected is True:
            return True
        else:
            return False

    @classmethod
    def toggle_openai_selected(cls):
        if cls.openai_selected:
            cls.openai_selected = False
            cls.alter_state_disabled = False
            return False
        else:
            cls.openai_selected = True        
            cls.alter_state_disabled = True    
            return True

    @classmethod
    def toggle_alter_selected(cls):
        if cls.alter_selected:
            cls.alter_selected = False
            cls.openai_state_disabled = False
            return False
        else:
            cls.alter_selected = True
            cls.openai_state_disabled = True
        return True

    @classmethod
    def check_openai_key(cls):
        # Check if OpenAI API key is set
        if os.environ.get("OPENAI_API_KEY"):
            cls.openai_key_set = True
            return True
        else:
            cls.openai_key_set = False
            return False