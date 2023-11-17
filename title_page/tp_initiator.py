from tkinter import ttk
from title_page.buttons.tpb_main import OpenAiApiKeyManager, OpenAiSelector, AlternativeSelector, MainPageStarter
from title_page.label_fields.label_fields import WelcomeSelTransc, OtherSetings
from title_page.buttons.tpb_controller import TitlePageButtonController
from title_page.checkbuttons.tpc_main import PhonemeEnabler


class TitlePageInitiator(ttk.Frame):
    def __init__(self, parent, get_phoneme_state, set_phoneme_state, restart_all_widgets):
        super().__init__(parent)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.button_colors = {
            "default_bg": "#DCDAD5",
            "default_active_bg": "#EEEBE6",
            "selected_bg": "#92de85",
            "selected_active_bg": "#a5fa96"
        }

        self.main_setup_label = WelcomeSelTransc(self)
        self.other_setings_label = OtherSetings(self)
        self.phoneme_enabler = PhonemeEnabler(self, get_phoneme_state, set_phoneme_state)
        self.controller = TitlePageButtonController()
        # Create buttons
        self.openai_api_key_manager = OpenAiApiKeyManager(self, self.controller)
        self.openai_selector = OpenAiSelector(self, self.controller, self.style, self.button_colors)
        self.alternative_selector = AlternativeSelector(self, self.controller, self.style, self.button_colors)
        self.main_page_starter = MainPageStarter(self, self.controller, restart_all_widgets)
        self.setup_layout()


    def setup_layout(self):
        self.main_setup_label.grid(row=0, column=0, sticky="nsew", columnspan=2)
        self.openai_api_key_manager.grid(row=1, column=1, sticky="nsew")
        self.openai_selector.grid(row=1, column=0, sticky="nsew")
        self.alternative_selector.grid(row=2, column=0, sticky="nsew")
        self.other_setings_label.grid(row=3, column=0, sticky="nsew", columnspan=2)
        self.phoneme_enabler.grid(row=4, column=0, sticky="nsew")
        self.main_page_starter.grid(row=5, column=0, sticky="nsew", columnspan=2)