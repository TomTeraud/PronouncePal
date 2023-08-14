import tkinter as tk
from tkinter import ttk
from gui.text_fields import SampleTextField, TranscribedTextField
from gui.button_manager import ButtonManager, LoadSampleButton, RecordButton
from gui.menu_bar import MenuBar


class AudioRecorderGUI(tk.Tk):
    def __init__(self, recorder, text_sample, trnscriber):
        super().__init__()
        self.text_sample = text_sample
        self.transcriber = trnscriber
        self.recorder = recorder

        self.title("Audio Recorder")

        self.setup_gui()

    def setup_gui(self):
        column = 0
        row = 0
        # Create parent widget, which will hold the contents of our user interface
        parent = ttk.Frame(self, borderwidth=20, relief="solid")
        parent.grid(column=column, row=row, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Create and place the SampleTextField
        self.sample_text_field = SampleTextField(parent, self.text_sample, column=column, row=row)
        self.sample_text_field.grid(column=column, row=row, sticky="nsew")

        # Create and place the TranscribedTextField
        column = 1
        self.transcribed_text_field = TranscribedTextField(parent, self.transcriber, column=column, row=row)
        self.transcribed_text_field.grid(column=column, row=row, sticky="nsew")


        self.button_manager = ButtonManager()
        # Create LoadSampleButton
        column = 0
        row = 1
        self.load_sample_button = LoadSampleButton(parent, self.text_sample, self.sample_text_field, row=row, column=column, button_manager=self.button_manager)

        
        # Create RecordButton
        column = 1
        row = 1
        self.record_button = RecordButton(parent, 
                                          self.text_sample, 
                                          self.transcriber, 
                                          self.recorder, 
                                          self.load_sample_button, 
                                          self.transcribed_text_field, 
                                          row=row, 
                                          column=column, 
                                          button_manager=self.button_manager)


        # Create and configure the MenuBar
        self.menu_bar = MenuBar(self, self.text_sample, self.sample_text_field, self.button_manager)
        self.config(menu=self.menu_bar)



        for child in parent.winfo_children(): 
            child.grid_configure(padx=2, pady=2)


        # Configure dynamic resizing
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
