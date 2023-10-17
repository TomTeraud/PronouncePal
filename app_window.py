import tkinter as tk
from tkinter import ttk

from text_samples.ts_main import TextSample
from title_page.buttons.tpb_controller import ButtonState as BS
from title_page.tp_initiator import TitlePageInitiator
from main_page.mp_initiator import MainPageInitiator
from menu_bar.mb_initiator import MenuInitiator



class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create an instance of TextSample to manage sample text
        self.text_sample = TextSample()
        
        self.title("PronouncePal")
        self.geometry("500x200")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.button_colors = {
            "default_bg": "#DCDAD5",
            "default_active_bg": "#EEEBE6",
            "selected_bg": "#92de85",
            "selected_active_bg": "#a5fa96"
        }
        self.start_new_widgets()

    def restart_all_widgets(self):
        self.destroy_all_widgets()
        self.start_new_widgets()
    

    def start_new_widgets(self):
        if BS.check_start_state():
            self.text_sample.update_sample()
            main_page = MainPageInitiator(self)
            main_page.grid(row=0, column=0, sticky="nsew")
        else:
            title_page = TitlePageInitiator(self)
            title_page.grid(row=0, column=0, sticky="nsew")

        self.menu_bar = MenuInitiator(self)
        self.config(menu=self.menu_bar)


        # # Configure grid for the main window
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def destroy_all_widgets(self):
        # Get a list of all widgets in the frame
        widgets = self.winfo_children()

        # Loop through the widgets and destroy each one
        for widget in widgets:
            widget.destroy()