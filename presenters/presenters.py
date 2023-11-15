
from presenters.main_p import MainPresenter
from presenters.setup_p import SetupPresenter
from presenters.menu_bar_p import MenuBarPresenter

from typing import Protocol


class View(Protocol):
    def mainloop(self) -> None:
        ...



class Presenters(MenuBarPresenter, SetupPresenter, MainPresenter):

    def __init__(self, model, view:View):
        super().__init__(model, view)
        self.model = model
        self.view = view

    def handle_main_page_start_button_click(self, event=None) -> None:
        self.handle_main_page_ui_loading()

    def handle_setup_page_start_button_click(self, event=None) -> None:
        self.handle_setup_page_ui_loading()

    def run(self) -> None:
        self.handle_defoult_menu_bar_creation()
        self.handle_setup_page_ui_loading()
        self.view.mainloop()