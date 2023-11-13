from __future__ import annotations
from typing import Protocol

from model.model import Model

class View(Protocol):
    pass

class MainPresenter:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view


    def handle_main_button_click(self, event=None) -> None:
        self.model.main_action()


