from __future__ import annotations

from typing import Protocol


from presenters.main_presenter import MainPresenter


class SetupView(Protocol):
    def init_setup_page(self, presenter: SetupPresenter) -> None:
        ...

    def mainloop(self) -> None:
        ...

    def destroy_all_widgets(self) -> None:
        ...


class SetupPresenter:
    def __init__(self, setup_v: SetupView, main_presenter: MainPresenter) -> None:
        self.setup_v = setup_v
        self.main_presenter = main_presenter
 
    def handle_main_view_start(self, event=None) -> None:
        self.setup_v.destroy_all_widgets()
        self.main_presenter.handle_main_page_start()
    
    def run(self) -> None:
        self.setup_v.init_setup_page(self)
        self.setup_v.mainloop()
