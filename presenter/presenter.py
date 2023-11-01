from __future__ import annotations

from typing import Protocol

from model.model import Model


class View(Protocol):

    def init_main_or_setup_ui(self, presenter: Presenter, status: bool) -> None:
        ...
    
    def mainloop(self) -> None:
        ...

    def update_text_field(self, sample_text: str) -> None:
        ...

    def update_rating_bar_base_value(self, rating: int) -> None:
        ...

    def update_transcribed_text_field(self, text: str) -> None:
        ...

    def config_buttons_state(self, state:int) -> None:
        ...

    def config_button_names(self, state: int, time: float) -> None:
        ...

class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def handle_new_word_loading(self, event=None):
        sample_text = self.model.get_word_text()
        self.view.update_text_field(sample_text)
        time = self.model.get_reading_time()
        self.view.config_button_names(0, time)
        self.handle_avg_rating_receiving()

    def handle_new_sentence_loading(self, event=None):
        sample_text = self.model.get_sentence_text()
        time = self.model.get_reading_time()
        self.view.update_text_field(sample_text)
        self.view.config_button_names(0, time)
        self.handle_avg_rating_receiving()

    def handle_recording_start(self, event=None) -> None:
        self.view.config_buttons_state(1)
        self.view.config_button_names(1, None)
        self.model.start_audio_recording(self)

    def handle_audio_transcribing(self) -> None:
        self.view.config_button_names(2, None)
        sample_text = self.model.start_audio_transcribing()
        self.view.update_transcribed_text_field(sample_text)
        self.view.config_buttons_state(0)
        time = self.model.get_reading_time()
        self.view.config_button_names(0, time)

    def handle_avg_rating_receiving(self, event=None):
        rating = self.model.get_avg_rating()
        self.view.update_rating_bar_base_value(rating)

    def start_new_view_structure(self) -> None:
        status = self.model.get_setup_page_status()
        self.view.init_main_or_setup_ui(self, status)
        self.handle_new_word_loading()
            
    def run(self) -> None:
        self.start_new_view_structure()
        self.view.mainloop()
