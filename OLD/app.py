import tkinter as tk
from tkinter import ttk

from text_samples.ts_main import TextSample
from title_page.tp_initiator import TitlePageInitiator
from main_page.mp_initiator import MainPageInitiator
from menu_bar.mb_initiator import MenuInitiator



class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PronouncePal")
        self.geometry("500x200")
        
        self.ready_state = False
        self.tp_phoneme_cb_state = False        
        self.start_new_widgets()

    def restart_all_widgets(self, state):
        self.ready_state = state
        self.destroy_all_widgets()
        self.start_new_widgets()
    
    def start_new_widgets(self):
        if not self.ready_state:
            self.title_page = TitlePageInitiator(self, self.get_phoneme_state, self.set_phoneme_state, self.restart_all_widgets)
            self.title_page.grid(row=0, column=0, sticky="nsew")
        else:
            self.text_sample = TextSample(self.tp_phoneme_cb_state)
            self.text_sample.update_sample()
            self.main_page = MainPageInitiator(self)
            self.main_page.grid(row=0, column=0, sticky="nsew")

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

    def get_phoneme_state(self):
        return self.tp_phoneme_cb_state
    
    def set_phoneme_state(self, state):
        self.tp_phoneme_cb_state = state

