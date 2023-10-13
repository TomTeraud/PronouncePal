import tkinter as tk
from tkinter import ttk

from title_page.controler import ButtonState as BS
from title_page.tp_initiator import TitlePageInitiator
from main_page.mp_initiator import MainPageInitiator



class AppWindow(tk.Tk):
    def __init__(self, text_sample):
        super().__init__()
        self.text_sample = text_sample
        
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
        self.start_main_frame_and_widgets()
    

    def start_main_frame_and_widgets(self):

        title_page = TitlePageInitiator(self, self.text_sample)
        title_page.grid(row=0, column=0, sticky="nsew")

        if BS.check_start_state():
            # Create Main Page
            main_page = MainPageInitiator(self, self.text_sample)
            main_page.grid(row=0, column=0, sticky="nsew")


        # Configure grid for the main window
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def destroy_all_widgets(self):
        # Get a list of all widgets in the frame
        widgets = self.winfo_children()

        # Loop through the widgets and destroy each one
        for widget in widgets:
            widget.destroy()