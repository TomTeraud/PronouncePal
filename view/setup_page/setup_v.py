from tkinter import *
from tkinter import ttk
from typing import Protocol
from view.master_view import MasterView

class SetupPresenter(Protocol):
    
    def handle_main_page_start_button_click(self, event=None) -> None:
        ...

class SetupView(MasterView):
    def __init__(self, ):
        super().__init__()

    def create_setup_widgets(self, presenter: SetupPresenter) -> None:
        label = ttk.Label(self.mainframe, text="Setup page")
        label.grid(column=0, row=0, sticky=(N, S, E, W))
        start_main_page_button = ttk.Button(self.mainframe, text="Start main page!")
        start_main_page_button.grid(column=0, row=1, sticky=(N, S, E, W))
        start_main_page_button.config(command=presenter.handle_main_page_start_button_click)
