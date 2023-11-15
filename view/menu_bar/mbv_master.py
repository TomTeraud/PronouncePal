from tkinter import *
from tkinter import Menu
from typing import Protocol

from view.master_view import MasterView
from view.menu_bar._rating_handler import RatingMenuHandler
from view.menu_bar._redme_handler import ReadmeHandler
from view.menu_bar._file_handler import FileMenuHandler


class MenuBarPresenter(Protocol):
        
    def handle_sample_text_upload(self, event=None) -> None:
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

    def add_defoult_menubar(self, presenter: MenuBarPresenter) -> None:

        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Upload your sample text", command=presenter.handle_sample_text_upload)
        file_menu.add_command(label="Delete personal data", command=self.handle_personal_data_deletion)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        
        rating_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="rating", menu=rating_menu)
        rating_menu.add_command(label="Words rating", command=presenter.handle_words_rating_clicked)
        rating_menu.add_command(label="Sentences rating", command=presenter.handle_sentences_rating_clicked)
        
        help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="help", menu=help_menu)
        help_menu.add_command(label="Readme", command=presenter.handle_readme_clicked)

    def handle_personal_data_deletion(self):
        print("deleeete!")

    def get_path_for_sample_file(self) -> str:
        return FileMenuHandler.get_path()
    
    def notify_file_upload_status(self, status:bool) -> None:
        FileMenuHandler.message_file_upload_status(status)

    def show_readme(self, readme_content: str) -> None:
        ReadmeHandler.show_readme(readme_content)

    def show_words_rating(self, data: list[tuple]) -> None:
        RatingMenuHandler.show_words_ratings(data)
    
    def show_sentences_rating(self, data: list[tuple]) -> None:
        RatingMenuHandler.show_sentences_ratings(data)