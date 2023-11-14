from model.model import Model
from typing import Protocol


class View(Protocol):
    def setup_page_menubar(self, presenter) -> None:
        ...

    def main_page_menubar(self, presenter) -> None:
        ...

    def show_readme(self, readme_content: str) -> None:
        ...

    def show_words_rating(self, data: list[tuple]) -> None:
        ...

    def show_sentences_rating(self, data: list[tuple]) -> None:
        ...

class MenuBarPresenter:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        
    def handle_menu_bar_for_main_page(self) -> None:
        self.view.main_page_menubar(self)

    def handle_menu_bar_for_setup_page(self) -> None:
        self.view.setup_page_menubar(self)

    def open_file(self):
        print("Open file action")

    def save_file(self):
        print("Save file action")

    def handle_readme_clicked(self, event=None):
        text = self.model.get_readme_text_for_menubar()
        self.view.show_readme(text)

    def handle_words_rating_clicked(self, event=None) -> None:
        data_list_tuples = self.model.get_single_word_ratings()
        self.view.show_words_rating(data_list_tuples)

    def handle_sentences_rating_clicked(self, event=None) -> None:
        data_list_tuples = self.model.get_sentence_ratings()
        self.view.show_sentences_rating(data_list_tuples)