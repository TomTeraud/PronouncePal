from tkinter import *
from tkinter import ttk

from view.main_page import MainPagesWidgets


TITLE = "PronouncePal"

class PronouncePal(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(TITLE)
        self.geometry("500x300")

        self.column_row_configure(self, 1, 1)

        self.frame = ttk.Frame(self, padding="5 5 5 5", borderwidth=10, relief="solid")
        self.frame.grid(column=0, row=0, sticky=(N, S, E, W))

    def init_main_or_setup_ui(self, presenter, status: bool) -> None:
        self.status = status
        # Init menu bar
        self.menu_bar(self.status)# Placeholder
        if self.status:
            self.setup_pages_ui(presenter)
        else:
            self.main_pages_ui(presenter)

    def menu_bar(self, status):
        ...

    def setup_pages_ui(self, presenter) -> None:
        # Create setup page widgets
        Label(self.frame, text="SETUP PAGE!!!").grid(column=0, row=0)
        # self.mpw = MainPageWidgets(self, presenter)
        print("create mainpage widgets triggered")

    def main_pages_ui(self, presenter) -> None:
        # Create main page widgets
        self.column_row_configure(self.frame, 4, 2)
        self.main_pages_widgets = MainPagesWidgets(self, presenter)

    def update_text_field(self, sample_text: str) -> None:
        self.main_pages_widgets.update_text_field(sample_text)

    def update_transcribed_text_field(self, sample_text: str) -> None:
        self.main_pages_widgets.update_transcribed_text_field(sample_text)

    def update_rating_bar_base_value(self, rating: int) ->None:
        self.main_pages_widgets.update_rating_bar_base_value(rating)

    def config_buttons_state(self, state:int) -> None:
        self.main_pages_widgets.set_button_state(state)

    def config_button_names(self, state: int, time: float) -> None:
        self.main_pages_widgets.set_button_names(state, time)

    def column_row_configure(self, frame, num_columns: int, num_rows :int) ->None:
        for col in range(num_columns):
            frame.grid_columnconfigure(col, weight=1)
        for row in range(num_rows):
            frame.grid_rowconfigure(row, weight=1, minsize=30)
