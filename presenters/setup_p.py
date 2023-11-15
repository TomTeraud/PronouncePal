from __future__ import annotations
from typing import Protocol
from model.model import Model


class View(Protocol):
    def init_setup_page_ui(self, presenter: SetupPresenter) -> None:
        ...
        

class SetupPresenter:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def handle_setup_page_ui_loading(self) -> None:
        self.view.init_setup_page_ui(self)

