
from presenters.main_p import MainPresenter
from presenters.setup_p import SetupPresenter
from presenters.menu_bar_p import MenuBarPresenter

from typing import Protocol


class View(Protocol):
    def mainloop(self) -> None:
        ...

    def init_setup_page_ui(self, presenter: SetupPresenter) -> None:
        ...
        
    def init_main_page_ui(self, presenter) -> None:
        ...


class Presenters(MenuBarPresenter, SetupPresenter, MainPresenter):

    def __init__(self, model, view:View):
        super().__init__(model, view)
        self.model = model
        self.view = view

    def handle_main_page_start_button_click(self, event=None) -> None:
        self.handle_main_page_ui_loading()
        self.handle_menu_bar_for_main_page()

    def handle_setup_page_start_button_click(self, event=None) -> None:
        self.handle_setup_page_ui_loading()
        self.handle_menu_bar_for_setup_page()

    def handle_setup_page_ui_loading(self) -> None:
        self.view.init_setup_page_ui(self)

    def handle_main_page_ui_loading(self) -> None:
        self.view.init_main_page_ui(self)

    def run(self) -> None:
        self.view.init_setup_page_ui(self)
        self.handle_menu_bar_for_setup_page()
        self.view.mainloop()