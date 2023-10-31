from __future__ import annotations

from typing import Protocol

from model.model import Model
from view.main_page import MainPageWidgets


class View(Protocol):

    def init_main_or_setup_ui(self, presenter: Presenter, status: bool) -> None:
        ...
    
    def mainloop(self) -> None:
        ...

    def update_text_field(self, sample: str) -> None:
        ...

    def update_rating_bar_base_value(self, rating: int) -> None:
        ...    


class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def handle_new_word_loading(self, event=None):
        sample = self.model.get_word_text()
        self.view.update_text_field(sample)
        self.handle_avg_rating_receiving()

    def handle_new_sentence_loading(self, event=None):
        sample = self.model.get_sentence_text()
        self.view.update_text_field(sample)
        self.handle_avg_rating_receiving()

    def handle_recording_start(self, event=None) -> None:
        print("Recording start triggered!!!")

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
