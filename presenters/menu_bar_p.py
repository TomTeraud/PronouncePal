from model.model import Model
from typing import Protocol


class View(Protocol):
    def setup_page_menubar(self, presenter) -> None:
        ...

    def main_page_menubar(self, presenter) -> None:
        ...

    def show_readme(self, readme_content: str) -> None:
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