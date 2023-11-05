from __future__ import annotations

from typing import Protocol

from model.model import Model


class SetupView(Protocol):
    def init_setup_page(self, presenter: Presenter) -> None:
        ...

    def mainloop(self) -> None:
        ...

    def destroy_all_widgets(self) -> None:
        ...

class MainView(Protocol):
    def init_main_page(self, presenter: Presenter) -> None:
        ...

    def update_text_field(self, text: str) -> None:
        ...

    def update_transcribed_text_field(self, sample:str) -> None:
        ...

    def set_button_names(self, state: int, time: float = None) -> None:
        ...

    def set_buttons_state(self, state: int) -> None:
        ...

    def update_rating_bar_base_value(self, rating:int = 0) -> None:
        ...

    def recording_bar_start(self, time: float) -> None:
        ...

class Presenter:
    def __init__(self, model: Model, setup_v: SetupView, main_v: MainView) -> None:
        self.model = model
        self.setup_v = setup_v
        self.main_v = main_v

    def handle_new_word_loading(self, event=None) -> None:
        self.main_v.update_text_field(self.model.get_word_text())
        self.handle_rating_bar_data()
        self.handle_read_time_data()

    def handle_new_sentence_loading(self, event=None) -> None:
        self.main_v.update_text_field(self.model.get_sentence_text())
        self.handle_rating_bar_data()
        self.handle_read_time_data()

    def handle_recording_start(self, event=None) -> None:
        self.main_v.set_buttons_state(1)
        self.main_v.set_button_names(1, None)
        self.main_v.recording_bar_start(self.model.get_reading_time())
        self.model.start_audio_recording(self)

    def handle_audio_transcribing(self) -> None:
        self.main_v.set_button_names(2, None)
        self.main_v.update_transcribed_text_field(self.model.start_audio_transcribing())
        self.main_v.set_buttons_state(0)
        self.handle_read_time_data()

    def handle_rating_bar_data(self, event=None):
        self.main_v.update_rating_bar_base_value(self.model.get_avg_rating())

    def handle_read_time_data(self) -> None:
        self.main_v.set_button_names(0, self.model.get_reading_time())

    def handle_main_view_start(self, event=None) -> None:
        self.setup_v.destroy_all_widgets()
        self.main_v.init_main_page(self)
        self.handle_new_word_loading()
    
    def run(self) -> None:
        self.setup_v.init_setup_page(self)
        self.setup_v.mainloop()
