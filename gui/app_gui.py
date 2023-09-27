import tkinter as tk
from tkinter import ttk
from gui.text_fields import SampleTextFrame, TranscribedTextField
from gui.button_manager import ButtonManager, SentenceSampleButton, RecordButton, WordSampleButton
from gui.menu.menu_bar import MenuBar
from gui.recording_progres_bar import RecordingProgresBar
from gui.rating_bar import RatingBar

class AudioRecorderGUI(tk.Tk):
    def __init__(self, text_sample):
        super().__init__()
        self.text_sample = text_sample

        self.title("PronouncePal")
        self.geometry("600x200")
        self.setup_gui()

    def setup_gui(self):
        parent = ttk.Frame(self)
        parent.grid(sticky=(tk.N, tk.W, tk.E, tk.S))

        # Create the RecordingProgresBar widget, duration comes from text_sample
        self.progress_bar = RecordingProgresBar(parent, self.text_sample)
        self.progress_bar.grid(row=2, column=0, sticky="nsew", columnspan=4)

        self.rating_bar = RatingBar(parent, self.text_sample)
        self.rating_bar.grid(row=0, column=5, sticky="nsew", rowspan=3)

        self.sample_text_field = SampleTextFrame(parent, self.text_sample)
        self.sample_text_field.grid(row=0, column=0, sticky="nsew", columnspan=2)

        self.transcribed_text_field = TranscribedTextField(parent)
        self.transcribed_text_field.grid(row=0, column=2, sticky="nsew", columnspan=2)

        self.button_manager = ButtonManager()

        self.load_word_sample_button = WordSampleButton(
            parent,
            self.text_sample,
            self.transcribed_text_field,
            self.sample_text_field,
            self.button_manager,
            self.rating_bar,
        )
        self.load_word_sample_button.grid(row=1, column=0, sticky="nsew")

        self.load_sample_button = SentenceSampleButton(
            parent,
            self.text_sample,
            self.transcribed_text_field,
            self.sample_text_field,
            self.button_manager,
            self.rating_bar,
        )
        self.load_sample_button.grid(row=1, column=1, sticky="nsew")

        self.record_button = RecordButton(
            parent,
            self.text_sample,
            self.transcribed_text_field,
            self.button_manager,
            self.progress_bar,
            self.rating_bar,
        )
        self.record_button.grid(row=1, column=2, sticky="nsew", columnspan=2)

        self.menu_bar = MenuBar(self, self.text_sample, self.sample_text_field, self.button_manager)
        self.config(menu=self.menu_bar)

        # Apply columnconfigure to each column
        for col in range(5):
            parent.columnconfigure(col, weight=1)

        # Apply rowconfigure to each row
        for row in range(3):
            parent.rowconfigure(row, weight=1, minsize=30)

        for child in parent.winfo_children():
            child.grid_configure(padx=2, pady=2)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
