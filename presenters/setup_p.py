from __future__ import annotations
from typing import Protocol
from model.model import Model


class View(Protocol):
    pass

class SetupPresenter:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view



