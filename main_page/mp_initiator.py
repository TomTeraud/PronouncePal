import tkinter as tk
from tkinter import ttk
from menu_bar.mb_initiator import MenuInitiator
from main_page.text_fields.text_fields import SampleTextFrame, TranscribedTextField
from main_page.buttons.button_manager import ButtonManager, SentenceSampleButton, RecordButton, WordSampleButton
from main_page.progress_bars.recording_progres_bar import RecordingProgresBar
from main_page.progress_bars.rating_bar import RatingBar

class MainPageInitiator(tk.Frame):
    def __init__(self, parent, text_sample):
        super().__init__(parent)
        self.text_sample = text_sample
        self.progress_bar = RecordingProgresBar(parent, self.text_sample)
        self.rating_bar = RatingBar(parent, self.text_sample)
        self.sample_text_field = SampleTextFrame(parent, self.text_sample)
        self.transcribed_text_field = TranscribedTextField(parent)
        self.button_manager = ButtonManager()
        self.load_word_sample_button = WordSampleButton(
            parent, self.text_sample, self.transcribed_text_field,
            self.sample_text_field, self.button_manager, self.rating_bar,
        )
        self.load_sample_button = SentenceSampleButton(
            parent, self.text_sample, self.transcribed_text_field, 
            self.sample_text_field, self.button_manager, self.rating_bar,
        )
        self.record_button = RecordButton(
            parent, self.text_sample, self.transcribed_text_field,
            self.button_manager, self.progress_bar, self.rating_bar,
        )
        self.menu_bar = MenuInitiator(parent, self.text_sample, self.sample_text_field, self.button_manager)
        self.configure_layout()

    def configure_layout(self):
        self.progress_bar.grid(row=2, column=0, sticky="nsew", columnspan=4)
        self.rating_bar.grid(row=0, column=5, sticky="nsew", rowspan=3)
        self.sample_text_field.grid(row=0, column=0, sticky="nsew", columnspan=2)
        self.transcribed_text_field.grid(row=0, column=2, sticky="nsew", columnspan=2)
        self.load_word_sample_button.grid(row=1, column=0, sticky="nsew")
        self.load_sample_button.grid(row=1, column=1, sticky="nsew")
        self.record_button.grid(row=1, column=2, sticky="nsew", columnspan=2)
        self.setup_column_configure(5)
        self.setup_row_configure(3)

    def setup_column_configure(self, num_columns):
        for col in range(num_columns):
            self.columnconfigure(col, weight=1)

    def setup_row_configure(self, num_rows):
        for row in range(num_rows):
            self.rowconfigure(row, weight=1, minsize=30)
