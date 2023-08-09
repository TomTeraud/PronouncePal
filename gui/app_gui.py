import tkinter as tk
from tkinter import ttk
from gui.text_fields import TextField
from gui.button_manager import ButtonManager
from gui.menu_bar import MenuBar


class AudioRecorderGUI(tk.Tk):
    def __init__(self, recorder, text_sample):
        super().__init__()

        self.recorder = recorder
        self.text_sample = text_sample

        self.title("Audio Recorder")
        
        self.setup_gui()

    def setup_gui(self):
        parent = ttk.Frame(self, borderwidth=30, relief="solid", width=200, height=100)
        parent.grid(sticky=(tk.N, tk.W, tk.E, tk.S))

        # Create and place the TextField
        self.text_field = TextField(parent, self.text_sample)
        self.text_field.grid(column=0, row=1)

        # Create and place the ButtonManager
        self.button_manager = ButtonManager(parent, self.text_sample, self.text_field)
        self.button_manager.grid(column=0, row=0)

        # Create and configure the MenuBar
        self.menu_bar = MenuBar(self, self.text_sample)
        self.config(menu=self.menu_bar)
        