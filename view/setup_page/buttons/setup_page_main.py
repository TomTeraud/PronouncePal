from tkinter import *
from tkinter import ttk, messagebox, simpledialog

class OpenAiApiKeyManager(ttk.Button):
    def __init__(self, frame):
        super().__init__(frame, text="Add API key")
    
    # Disable the button if the API key is set
    def update_button_state(self, state: bool) -> None:
        if state:
            self.config(state=NORMAL)
        else:
            self.config(state=DISABLED)

    @staticmethod
    def ask_for_key() -> str:
        return simpledialog.askstring("Input", "Enter your API key:")

    @staticmethod
    def show_message_to_user(state: bool) -> None:
        if state:
            messagebox.showinfo("Success", "API key set successfully!")
        else:
            messagebox.showerror("Error", "Invalid API key")


class OpenAiSelector(ttk.Button):
    def __init__(self, frame):
        super().__init__(frame, text="OpenAI", style='Openai.TButton')
        # self.ctrl = ctrl
        # self.style = style
        # self.colors = colors
        # self.ctrl.set_button("openai", self)
        # self.update_button_state()
        # self.set_color()

    def update_button_state(self, state: bool) -> None:
        if state:
            self.config(state=NORMAL)
        else:
            self.config(state=DISABLED)

    # def select_openai(self):
    #     self.set_color(self.ctrl.openai_selected)
    #     self.ctrl.openai_triggered()

    # def set_color(self, selected_state=True):
    #     if selected_state:
    #         default_bg_color = self.colors["default_bg"]
    #         active_bg_color = self.colors["default_active_bg"]
    #     else:
    #         default_bg_color = self.colors["selected_bg"]
    #         active_bg_color = self.colors["selected_active_bg"]

    #     # Configure the style for the button
    #     self.style.configure("Openai.TButton", background=default_bg_color)
    #     self.style.map('Openai.TButton', background=[('active', active_bg_color)])

class AlternativeSelector(ttk.Button):
    def __init__(self, frame):
        super().__init__(frame, text="Alternative (under development)", style="Alt.TButton")
    #     self.ctrl = ctrl
    #     self.style = style
    #     self.colors = colors
    #     self.ctrl.set_button("alternative", self)
    #     self.update_button_state()
    #     self.set_color()

    def update_button_state(self, state: bool) -> None:
        if state:
            self.config(state=NORMAL)
        else:
            self.config(state=DISABLED)

    # def selected_alter(self):
    #     self.set_color(self.ctrl.alternative_selected)
    #     self.ctrl.alternative_triggered()

    # def set_color(self, selected_state=True):
    #     if selected_state:
    #         default_bg_color = self.colors["default_bg"]
    #         active_bg_color = self.colors["default_active_bg"]
    #     else:
    #         default_bg_color = self.colors["selected_bg"]
    #         active_bg_color = self.colors["selected_active_bg"]

    #     # Configure the style for the button
    #     self.style.configure("Alt.TButton", background=default_bg_color)
    #     self.style.map('Alt.TButton', background=[('active', active_bg_color)])

class MainPageStarter(ttk.Button):
    def __init__(self, frame):
        super().__init__(frame, text="Start!")
    #     self.ctrl = ctrl
    #     self.restart_all_widgets = restart_all_widgets
    #     self.ctrl.set_button("main_page", self)
    #     self.update_button_state()

    # def start_main_page(self):
    #     if self.ctrl.openai_selected:
    #         self.restart_all_widgets(True)
    #     else:
    #         messagebox.showinfo("Info", "An alternative transcriber is under development")

    def update_button_state(self, state) -> None:
        if state:
            self.config(state=NORMAL)
        else:
            self.config(state=DISABLED)