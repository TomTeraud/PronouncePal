import tkinter as tk
from tkinter import ttk, messagebox
from utils.api_handler import OpenaiApiKeyHandler as OAKH

class OpenAiApiKeyManager(ttk.Button):
    def __init__(self, parent, ctrl):
        super().__init__(parent, text="Add API key", command=self.manage_key)
        self.ctrl = ctrl
        self.ctrl.set_button("openai_key", self)
        self.update_button_state()

    def manage_key(self):
        if OAKH.ask_for_key():
            # Set the OpenAI API key status and update buttons
            self.ctrl.set_openai_api_key_status(True)
            self.ctrl.update_buttons()

    def update_button_state(self):
        # Disable the button if the API key is set
        if self.ctrl.get_openai_api_key_status():
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class OpenAiSelector(ttk.Button):
    def __init__(self, parent, ctrl, style, colors):
        super().__init__(parent, text="OpenAI", style='Openai.TButton', command=self.select_openai)
        self.ctrl = ctrl
        self.style = style
        self.colors = colors
        self.ctrl.set_button("openai", self)
        self.update_button_state()
        self.set_color()

    def select_openai(self):
        self.set_color(self.ctrl.openai_selected)
        self.ctrl.openai_triggered()

    def set_color(self, selected_state=True):
        if selected_state:
            default_bg_color = self.colors["default_bg"]
            active_bg_color = self.colors["default_active_bg"]
        else:
            default_bg_color = self.colors["selected_bg"]
            active_bg_color = self.colors["selected_active_bg"]

        # Configure the style for the button
        self.style.configure("Openai.TButton", background=default_bg_color)
        self.style.map('Openai.TButton', background=[('active', active_bg_color)])

    def update_button_state(self):
        if self.ctrl.openai_api_key_ready is False or self.ctrl.openai_locked:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class AlternativeSelector(ttk.Button):
    def __init__(self, parent, ctrl, style, colors):
        super().__init__(parent, text="Alternative (under development)", style="Alt.TButton", command=self.selected_alter)
        self.ctrl = ctrl
        self.style = style
        self.colors = colors
        self.ctrl.set_button("alternative", self)
        self.update_button_state()
        self.set_color()

    def selected_alter(self):
        self.set_color(self.ctrl.alternative_selected)
        self.ctrl.alternative_triggered()

    def set_color(self, selected_state=True):
        if selected_state:
            default_bg_color = self.colors["default_bg"]
            active_bg_color = self.colors["default_active_bg"]
        else:
            default_bg_color = self.colors["selected_bg"]
            active_bg_color = self.colors["selected_active_bg"]

        # Configure the style for the button
        self.style.configure("Alt.TButton", background=default_bg_color)
        self.style.map('Alt.TButton', background=[('active', active_bg_color)])

    def update_button_state(self):
        if self.ctrl.alternative_locked:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class MainPageStarter(ttk.Button):
    def __init__(self, parent, ctrl, restart_all_widgets):
        super().__init__(parent, text="Start!", command=self.start_main_page)
        self.ctrl = ctrl
        self.restart_all_widgets = restart_all_widgets
        self.ctrl.set_button("main_page", self)
        self.update_button_state()

    def start_main_page(self):
        if self.ctrl.openai_selected:
            self.restart_all_widgets(True)
        else:
            messagebox.showinfo("Info", "An alternative transcriber is under development")

    def update_button_state(self):
        if self.ctrl.ready_to_start:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)