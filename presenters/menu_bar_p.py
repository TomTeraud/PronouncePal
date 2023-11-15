from model.model import Model
from typing import Protocol


class View(Protocol):
    def add_defoult_menubar(self, presenter) -> None:
        ...

    def show_readme(self, readme_content: str) -> None:
        ...

    def show_words_rating(self, data: list[tuple]) -> None:
        ...

    def show_sentences_rating(self, data: list[tuple]) -> None:
        ...

    def get_path_for_sample_file(self) -> str:
        ...

    def handle_sample_upload_with_given_path(self, path: str) -> bool:
        ...

    def notify_file_upload_status(self, status:bool) -> None:
        ...

    def get_deletion_confirmation(self) -> bool:
        ...

    def notify_deletion_status(self, status: bool) -> None:
        ...

class MenuBarPresenter:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        
    def handle_defoult_menu_bar_creation(self) -> None:
        self.view.add_defoult_menubar(self)

    def handle_sample_text_upload_clicked(self, event=None) -> None:
        path = self.view.get_path_for_sample_file()
        result = self.model.handle_sample_upload_with_given_path(path)
        self.view.notify_file_upload_status(result)

    def handle_readme_clicked(self, event=None):
        text = self.model.get_readme_text_for_menubar()
        self.view.show_readme(text)

    def handle_words_rating_clicked(self, event=None) -> None:
        data_list_tuples = self.model.get_single_word_ratings()
        self.view.show_words_rating(data_list_tuples)

    def handle_sentences_rating_clicked(self, event=None) -> None:
        data_list_tuples = self.model.get_sentence_ratings()
        self.view.show_sentences_rating(data_list_tuples)

    def handle_personal_data_deletion_clicked(self, event=None) -> None:
        if self.view.get_deletion_confirmation() and self.model.handle_personal_data_deletion():
            self.view.notify_deletion_status(True)
        else:
            self.view.notify_deletion_status(False)