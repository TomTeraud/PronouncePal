import tkinter as tk
from tkinter import ttk, messagebox
from utils.api_handler import OpenaiApiKeyHandler as OAKH


class OpenAiApiKeyManager(ttk.Button):  
    def __init__(self, parent):
        super().__init__(parent, text="Add API key", command=self.manage_key)
        self.tpbc = parent.tpb_controller
        self.tpbc.set_button("openai_key", self)
        self.update_button_state()

    def manage_key(self):
        if OAKH.ask_for_key():
            self.tpbc.openai_api_key_ready = True
            self.tpbc.update_buttons()
            

    def update_button_state(self):
        if self.tpbc.openai_api_key_ready:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class OpenAiSelector(ttk.Button):  
    def __init__(self, parent, grand_parent):
        super().__init__(parent, text="OpenAI", style='Openai.TButton', command=self.select_openai)
        self.grand_parent = grand_parent
        self.tpbc = parent.tpb_controller
        self.tpbc.set_button("openai", self)
        self.update_button_state()

    def select_openai(self):
        self.set_color(self.tpbc.openai_selected)
        self.tpbc.openai_triggered()

    def set_color(self, selected_state):
        g_p_style = self.grand_parent.style
        g_p_colors = self.grand_parent.button_colors
        
        if selected_state:
            default_bg_color = g_p_colors["default_bg"]
            active_bg_color = g_p_colors["default_active_bg"]
        else:
            default_bg_color = g_p_colors["selected_bg"]
            active_bg_color = g_p_colors["selected_active_bg"]

        g_p_style.configure("Openai.TButton", background=default_bg_color)
        g_p_style.map('Openai.TButton', background=[('active', active_bg_color)])

    def update_button_state(self):
        if self.tpbc.openai_api_key_ready == False or self.tpbc.openai_locked:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)
 
class AlternativeSelector(ttk.Button):
    def __init__(self, parent, grand_parent):
        super().__init__(parent, text="Alternative (under development)", style="Alt.TButton", command=self.selected_alter)
        self.tpbc = parent.tpb_controller
        self.grand_parent = grand_parent
        self.tpbc.set_button("alternative", self)
        self.update_button_state()

    def selected_alter(self):
        self.set_color(self.tpbc.alternative_selected)
        self.tpbc.alternative_triggered()

    def set_color(self, selected_state):
        g_p_style = self.grand_parent.style
        g_p_colors = self.grand_parent.button_colors
        
        if selected_state:
            default_bg_color = g_p_colors["default_bg"]
            active_bg_color = g_p_colors["default_active_bg"]
        else:
            default_bg_color = g_p_colors["selected_bg"]
            active_bg_color = g_p_colors["selected_active_bg"]

        g_p_style.configure("Alt.TButton", background=default_bg_color)
        g_p_style.map('Alt.TButton', background=[('active', active_bg_color)])

    def update_button_state(self):
        if self.tpbc.alternative_locked:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class MainPageStarter(ttk.Button):  
    def __init__(self, parent, grand_parent):
        super().__init__(parent, text="Start!", command=self.start_main_page)
        self.tpbc = parent.tpb_controller
        self.grand_parent = grand_parent
        self.tpbc.set_button("main_page", self)
        self.update_button_state()

    def start_main_page(self):
        if self.tpbc.openai_selected:
            self.grand_parent.restart_all_widgets(True)
        else:
            messagebox.showinfo("Info", "An alternative transcriber is under development")

    def update_button_state(self):
        if self.tpbc.ready_to_start:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)