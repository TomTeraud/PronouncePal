from model.api_handler import OpenaiApiKeyHandler

class TitlePageButtonController:
    def __init__(self):
        # Initialize status flags
        self.openai_api_key_ready = OpenaiApiKeyHandler.openai_api_key_status()
        self.openai_selected = False 
        self.openai_locked = False
        self.alternative_selected = False
        self.alternative_locked = False
        self.ready_to_start = False
        self.buttons = []  # List to store all button instances
    
    def set_button(self, button_type, button_instance):
        """
        Set a button instance based on its type.

        Args:
            button_type (str): Type of the button ('openai_key', 'openai', 'alternative', 'app_start').
            button_instance: The instance of the button to set.
        """
        if button_type == 'openai_key':
            self.openai_key_button = button_instance
        elif button_type == 'openai':
            self.openai_button = button_instance
        elif button_type == 'alternative':
            self.alternative_button = button_instance
        elif button_type == 'main_page':
            self.app_start_button = button_instance
        self.buttons.append(button_instance)  # Add the button to the list

    def openai_triggered(self):
        if self.openai_selected:
            self.alternative_locked = False
            self.openai_selected = False
            self.ready_to_start = False
        else:
            self.alternative_locked = True
            self.openai_selected = True
            self.ready_to_start = True
        self.update_buttons()


    def alternative_triggered(self):
        if self.alternative_selected:
            self.openai_locked = False
            self.alternative_selected = False
            self.ready_to_start = False
        else:
            self.openai_locked = True
            self.alternative_selected = True
            self.ready_to_start = True
        self.update_buttons()



    def update_buttons(self):
        """
        Update the state of buttons based on status.
        """
        for button in self.buttons:
            button.update_button_state()

    def set_openai_api_key_status(self, status):
        self.openai_api_key_ready = status

    def get_openai_api_key_status(self):
        return self.openai_api_key_ready