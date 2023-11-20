from model.api_key_handler import OpenaiApiKeyHandler

class SetupPageButtonController:
    def __init__(self) -> None:
        self.openai_selector_enabled = True
        self.alternative_selector_enabled = True
        self.openai_selected = False
        self.alternative_selected = False
        self.ready_to_start = False


    def select_openai_triggered(self) -> None:
        # disable or enable alter selector and start app buttons
        if self.openai_selected:
            self.alternative_selector_enabled = True
            self.openai_selected = False
            self.ready_to_start = False
        else:
            self.alternative_selector_enabled = False
            self.openai_selected = True
            self.ready_to_start = True

    def select_alternative_triggered(self) -> None:
        # Disable or enable openai selector and start app buttons
        if self.alternative_selected:
            self.openai_selector_enabled = True
            self.alternative_selected = False
            self.ready_to_start = False
        else:
            self.openai_selector_enabled = False
            self.alternative_selected = True
            self.ready_to_start = True

    def get_openai_selector_button_state(self) -> bool:
        return self.check_openai_key_set_status() and self.openai_selector_enabled

    def get_alternative_selector_button_state(self) -> bool:
        return self.alternative_selector_enabled
    
    def get_app_start_button_state(self) -> bool:
        return self.ready_to_start
    
    def get_openai_api_key_button_state(self) -> bool:
        return not self.check_openai_key_set_status()

    def check_openai_key_set_status(self) -> bool:
        return OpenaiApiKeyHandler.openai_api_key_status()