import tkinter as tk
from tkinter import ttk
from title_page.buttons import ApiKeySetupButtonOpenAi, SelectOpenAiButton, SelectAlternativeButton, StartMainGuiButton
from title_page.label_fields import MainSetupLabel


class TitlePageInitiator(tk.Frame):
    def __init__(self, parent, text_sample):
        super().__init__(parent)
        self.text_sample = text_sample
        self.configure_button_style("Alt.TButton")
        self.configure_button_style("Openai.TButton")
        self.start_main_gui = StartMainGuiButton(self, parent)
        self.setup_label = MainSetupLabel(self)
        self.select_openai = SelectOpenAiButton(self)
        self.select_alternative = SelectAlternativeButton(self)
        self.api_key_setup = ApiKeySetupButtonOpenAi(self)
        self.setup_layout()

        # Set references between instances
        self.select_openai.select_alternative = self.select_alternative
        self.select_openai.start_main_gui = self.start_main_gui
        self.select_alternative.select_openai = self.select_openai
        self.select_alternative.start_main_gui = self.start_main_gui
        self.api_key_setup.select_openai = self.select_openai

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
        self.select_openai.grid(row=1, column=0, sticky="nsew")
        self.api_key_setup.grid(row=1, column=1, sticky="nsew")
        self.select_alternative.grid(row=2, column=0, sticky="nsew")
        self.start_main_gui.grid(row=3, column=0, sticky="nsew", columnspan=2)
        self.setup_column_configure(2)
        self.setup_row_configure(3)

    def setup_column_configure(self, num_columns):
        for col in range(num_columns):
            self.columnconfigure(col, weight=1)

    def setup_row_configure(self, num_rows):
        for row in range(num_rows):
            self.rowconfigure(row, weight=1, minsize=30)