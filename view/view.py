from tkinter import *
from tkinter import ttk

from view.main_page import MainPageWidgets


TITLE = "PronouncePal"
MOCK_BTN_TXT = "Print Mock!"


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
            self.setup_page_ui(presenter)
        else:
            self.main_page_ui(presenter)

        
    def menu_bar(self, status):
        ...

    def setup_page_ui(self, presenter) -> None:
        # Create setup page widgets
        Label(self.frame, text="SETUP PAGE!!!").grid(column=0, row=0)
        self.mpw = MainPageWidgets(self, presenter)
        print("create mainpage widgets triggered")


    def main_page_ui(self, presenter) -> None:
        print("create mainpage widgets triggered")
        # Create main page widgets
        self.column_row_configure(self.frame, 4, 2)
        self.main_page_widgets = MainPageWidgets(self, presenter)


    def column_row_configure(self, frame, num_columns: int, num_rows :int) ->None:
        for col in range(num_columns):
            frame.grid_columnconfigure(col, weight=1)
        for row in range(num_rows):
            frame.grid_rowconfigure(row, weight=1, minsize=30)

    def update_text_field(self, sample: str) -> None:
        self.main_page_widgets.update_text_field(sample)

    def update_rating_bar_base_value(self, rating: int) ->None:
        self.main_page_widgets.update_rating_bar_base_value(rating)
        