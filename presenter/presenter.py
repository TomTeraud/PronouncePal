from __future__ import annotations

from typing import Protocol

from model.model import Model


class View(Protocol):

    def init_main_or_setup_ui(self, presenter: Presenter, status: bool) -> None:
        ...
    
    def mainloop(self) -> None:
        ...

    def update_text_field(self, sample: str) -> None:
        ...


class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def handle_new_word_loading(self, event=None):
        sample = self.model.get_word_text()
        self.view.update_text_field(sample)

    def handle_new_sentence_loading(self, event=None):
        sample = self.model.get_sentence_text()
        self.view.update_text_field(sample)

    def handle_recording_start(self, event=None) -> None:
        print("Recording start triggered!!!")

    def start_new_view_structure(self) -> None:
        status = self.model.get_setup_page_status()
        self.view.init_main_or_setup_ui(self, status)
            
    def run(self) -> None:
        self.start_new_view_structure()
        self.handle_new_word_loading()
        self.view.mainloop()
