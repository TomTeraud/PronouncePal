import tkinter as tk
from tkinter import ttk, messagebox
from utils.api_handler import OpenaiApiKeyHandler as OAKH
from gui.title_page.controler import ButtonState as BS


class ApiKeySetupButtonOpenAi(ttk.Button):  
    def __init__(self, parent):
        super().__init__(parent, text="Add API key", command=self.manage_api_key)

    def manage_api_key(self):
        if OAKH.ask_for_key():
            BS.openai_key_set = True
            if BS.alter_selected is False:
                self.select_openai.set_openai_state(False)

class SelectOpenAiButton(ttk.Button):  
    def __init__(self, parent):
        super().__init__(parent, text="OpenAI", style='Openai.TButton', command=self.openai_selected)
        BS.check_openai_key()
        self.set_openai_state(False)

    def openai_selected(self):
        self.result = BS.toggle_openai_selected()
        self.select_alternative.set_alter_state(self.result)
        self.start_main_gui.set_start_state(self.result)
        self.set_color(self.result)

    def set_color(self, selected_state):
        parent_style = self.master.master.style
        colors = self.master.master.button_colors
        
        if selected_state:
            default_bg_color = colors["selected_bg"]
            active_bg_color = colors["selected_active_bg"]
        else:
            default_bg_color = colors["default_bg"]
            active_bg_color = colors["default_active_bg"]

        parent_style.configure("Openai.TButton", background=default_bg_color)
        parent_style.map('Openai.TButton', background=[('active', active_bg_color)])

    def set_openai_state(self, state):
        if state is False and BS.openai_key_set:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)

class SelectAlternativeButton(ttk.Button):
    def __init__(self, parent):
        super().__init__(parent, text="Alternative (under development)", style="Alt.TButton", command=self.alter_selected)

    def alter_selected(self):
        self.result = BS.toggle_alter_selected()
        self.select_openai.set_openai_state(self.result)
        self.start_main_gui.set_start_state(self.result)
        self.set_color(self.result)

    def set_color(self, selected_state):
        parent_style = self.master.master.style
        colors = self.master.master.button_colors
        
        if selected_state:
            default_bg_color = colors["selected_bg"]
            active_bg_color = colors["selected_active_bg"]
        else:
            default_bg_color = colors["default_bg"]
            active_bg_color = colors["default_active_bg"]

        parent_style.configure("Alt.TButton", background=default_bg_color)
        parent_style.map('Alt.TButton', background=[('active', active_bg_color)])

    def set_alter_state(self, state):
        if state is False:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)

class StartMainGuiButton(ttk.Button):  
    def __init__(self, parent, argi):
        super().__init__(parent, text="Start!", command=self.start_main_gui)
        self.argi = argi
        self.set_start_state(False)

    def start_main_gui(self):
        if BS.openai_selected:
            BS.ready_to_start = True
            self.argi.destroy_all_widgets()
            self.argi.start_main_frame_and_widgets()
        else:
            messagebox.showinfo("Info", "An alternative transcriber is under development")

    def set_start_state(self, state):
        if state:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)