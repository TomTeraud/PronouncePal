from tkinter import *
from tkinter import ttk
from typing import Protocol
from view.master_view import MasterView
from view.setup_page.buttons.tpb_main import AlternativeSelector, MainPageStarter, OpenAiApiKeyManager, OpenAiSelector
from view.setup_page.checkbuttons.tpc_main import PhonemeEnabler
from view.setup_page.label_fields.label_fields import WelcomeSelTransc, OtherSetings

# from title_page.buttons.tpb_main import OpenAiApiKeyManager, OpenAiSelector, AlternativeSelector, MainPageStarter
# from title_page.label_fields.label_fields import WelcomeSelTransc, OtherSetings
# from title_page.buttons.tpb_controller import TitlePageButtonController
# from title_page.checkbuttons.tpc_main import PhonemeEnabler


class SetupPresenter(Protocol):
    def handle_main_page_start_button_click(self, event=None) -> None:
        ...

class SetupView(MasterView):
    def __init__(self, ):
        super().__init__()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.button_colors = {
            "default_bg": "#DCDAD5",
            "default_active_bg": "#EEEBE6",
            "selected_bg": "#92de85",
            "selected_active_bg": "#a5fa96"
        }

    def create_setup_widgets(self, presenter: SetupPresenter) -> None:
        self.manage_widgets_creation()
        self.manage_widgets_grid_position()
        self.manage_widgets_items(presenter)


    def manage_widgets_creation(self) -> None:
        self.main_setup_label = WelcomeSelTransc(self.mainframe)
        self.openai_selector = OpenAiSelector(self.mainframe)
        self.openai_api_key_manager = OpenAiApiKeyManager(self.mainframe)
        self.alternative_selector = AlternativeSelector(self.mainframe)
        self.other_setings_label = OtherSetings(self.mainframe)
        self.phoneme_enabler = PhonemeEnabler(self.mainframe)
        self.main_page_starter = MainPageStarter(self.mainframe)

    def manage_widgets_grid_position(self) -> None:
        self.main_setup_label.grid(column=0, row=0, sticky=NSEW, columnspan=2)
        self.openai_selector.grid(row=1, column=0, sticky=NSEW)
        self.openai_api_key_manager.grid(row=1, column=1, sticky=NSEW)
        self.alternative_selector.grid(row=2, column=0, sticky=NSEW)
        self.other_setings_label.grid(row=3, column=0, sticky=NSEW, columnspan=2)
        self.phoneme_enabler.grid(row=4, column=0, sticky=NSEW)
        self.main_page_starter.grid(row=5, column=0, sticky=NSEW, columnspan=2)

    def manage_widgets_items(self, presenter: SetupPresenter) -> None:
        self.main_page_starter.config(command=presenter.handle_main_page_start_button_click)
        ...
