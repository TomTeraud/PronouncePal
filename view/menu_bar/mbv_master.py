from tkinter import *
from tkinter import Menu
from typing import Protocol

from view.master_view import MasterView
from view.menu_bar._rating_handler import RatingMenuHandler
from view.menu_bar._redme_handler import ReadmeHandler



class MenuBarPresenter(Protocol):
        
    def open_file(self, event=None):
        ...
    def save_file(self, event=None):
        ...
    def handle_readme_clicked(self, event=None):
        ...
    def handle_words_rating_clicked(self, event=None) -> None:
        ...
    def handle_sentences_rating_clicked(self, event=None) -> None:
        ...

class MenuBarView(MasterView):
    def __init__(self):
        super().__init__()
        self.menubar = Menu(self)
        self.config(menu=self.menubar)

    def setup_page_menubar(self, presenter: MenuBarPresenter) -> None:

        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=presenter.open_file)
        file_menu.add_command(label="Save", command=presenter.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        
        rating_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="rating", menu=rating_menu)
        rating_menu.add_command(label="Words rating", command=presenter.handle_words_rating_clicked)
        rating_menu.add_command(label="Sentences rating", command=presenter.handle_sentences_rating_clicked)
        
        help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="help", menu=help_menu)
        help_menu.add_command(label="Readme", command=presenter.handle_readme_clicked)

    def main_page_menubar(self, presenter) -> None:
        demo_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Demo menu", menu=demo_menu)

    def show_readme(self, readme_content: str) -> None:
        ReadmeHandler.show_readme(readme_content)

    def show_words_rating(self, data: list[tuple]) -> None:
        RatingMenuHandler.show_words_ratings(data)
    
    def show_sentences_rating(self, data: list[tuple]) -> None:
        RatingMenuHandler.show_sentences_ratings(data)