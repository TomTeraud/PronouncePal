class MainPageButtonController:
    def __init__(self):
        self.is_recording = False
        self.is_transcribing = False
        self.buttons = []  # List to store all button instances

    def set_button(self, button_type, button_instance):
        """
        Set a button instance based on its type.

        Args:
            button_type (str): Type of the button ('sentence', 'word', or 'record').
            button_instance: The instance of the button to set.
        """
        if button_type == 'sentence':
            self.sentence_button = button_instance
        elif button_type == 'word':
            self.word_button = button_instance
        elif button_type == 'record':
            self.record_button = button_instance
        self.buttons.append(button_instance)

    def set_recording_status(self, is_recording):
        self.is_recording = is_recording
        self.update_buttons()

    def set_transcribing_status(self, is_transcribing):
        self.is_transcribing = is_transcribing
        self.update_buttons()

    def update_buttons(self):
        for button in self.buttons:
            button.update_button_state()
