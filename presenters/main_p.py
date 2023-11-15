from __future__ import annotations
from typing import Protocol

from model.model import Model

class View(Protocol):
    def init_main_page_ui(self, presenter:MainPresenter) -> None:
        ...

class MainPresenter:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def handle_main_page_ui_loading(self) -> None:
        self.view.init_main_page_ui(self)

    def handle_main_button_click(self, event=None) -> None:
        self.model.main_action()


