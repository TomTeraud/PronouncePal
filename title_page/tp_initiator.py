from tkinter import ttk
from title_page.buttons.tpb_main import OpenAiApiKeyManager, OpenAiSelector, AlternativeSelector, MainPageStarter
from title_page.label_fields.label_fields import MainSetupLabel
from title_page.buttons.tpb_controller import TitlePageButtonController


class TitlePageInitiator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_label = MainSetupLabel(self)
        self.configure_button_style("Alt.TButton")
        self.configure_button_style("Openai.TButton")
        self.tpb_controller = TitlePageButtonController()
        # Create buttons
        self.openai_api_key_manager = OpenAiApiKeyManager(self)
        self.openai_selector = OpenAiSelector(self, parent)
        self.alternative_selector = AlternativeSelector(self, parent)
        self.main_page_starter = MainPageStarter(self, parent)
        self.setup_layout()

    def configure_button_style(self, style_name):
        button_colors = {
            "default_bg": "#DCDAD5",
            "default_active_bg": "#EEEBE6",
            "selected_bg": "#92de85",
            "selected_active_bg": "#a5fa96"
        }
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(style_name, background=button_colors["default_bg"])
        style.map(style_name, background=[('active', button_colors["default_active_bg"]), ('alternate', button_colors["selected_bg"]), ('active', button_colors["selected_active_bg"])])

    def setup_layout(self):
        self.setup_label.grid(row=0, column=0, sticky="nsew", columnspan=2)
        self.openai_api_key_manager.grid(row=1, column=1, sticky="nsew")
        self.openai_selector.grid(row=1, column=0, sticky="nsew")
        self.alternative_selector.grid(row=2, column=0, sticky="nsew")
        self.main_page_starter.grid(row=3, column=0, sticky="nsew", columnspan=2)
        self.setup_column_configure(2)
        self.setup_row_configure(3)

    def setup_column_configure(self, num_columns):
        for col in range(num_columns):
            self.columnconfigure(col, weight=1)

    def setup_row_configure(self, num_rows):
        for row in range(num_rows):
            self.rowconfigure(row, weight=1, minsize=30)