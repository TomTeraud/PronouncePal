class MainPageButtonController:
    def __init__(self):
        self.sentence_button = None
        self.word_button = None
        self.record_button = None
        self.is_recording = False
        self.is_transcribing = False

    def set_word_button(self, word_button):
        self.word_button = word_button

    def set_sentence_button(self, sentence_button):
        self.sentence_button = sentence_button

    def set_record_button(self, record_button):
        self.record_button = record_button

    def start_recording(self):
        self.is_recording = True
        self.update_buttons()

    def stop_recording(self):
        self.is_recording = False
        self.update_buttons()

    def start_transcribing(self):
        self.is_transcribing = True
        self.update_buttons()

    def stop_transcribing(self):
        self.is_transcribing = False
        self.update_buttons()

    def update_buttons(self):
        # Update button states based on recording, transcribing status
        if self.sentence_button:
            self.sentence_button.update_button_state()
        if self.word_button:
            self.word_button.update_button_state()
        if self.record_button:
            self.record_button.update_button_state()
