from tkinter import ttk
from main_page.text_fields.text_fields import *
from main_page.buttons.button_manager import ButtonManager, SentenceSampleButton, RecordButton, WordSampleButton
from main_page.progress_bars.recording_progres_bar import RecordingProgresBar
from main_page.progress_bars.rating_bar import RatingBar

class MainPageInitiator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        print(self)
        self.text_sample = parent.text_sample
        self.progress_bar = RecordingProgresBar(self)
        self.rating_bar = RatingBar(self)
        self.sample_text_field = SampleTextField(self)
        self.phonemic_text_field = PhonemicTextField(self)
        self.transcribed_text_field = TranscribedTextField(self)
        self.button_manager = ButtonManager()
        self.next_word_button = WordSampleButton(self, parent)
        self.next_sentence_button = SentenceSampleButton(self, parent)
        self.record_button = RecordButton(self, parent)
        self.configure_layout()



    def configure_layout(self):
        self.progress_bar.grid(row=3, column=0, sticky="nsew", columnspan=5)
        self.rating_bar.grid(row=0, column=5, sticky="nsew", rowspan=3)
        self.sample_text_field.grid(row=0, column=0, sticky="nsew", columnspan=2)
        self.phonemic_text_field.grid(row=1, column=0, sticky="nsew", columnspan=2)
        self.transcribed_text_field.grid(row=0, column=2, sticky="nsew", columnspan=2, rowspan=2)
        self.next_word_button.grid(row=2, column=0, sticky="nsew")
        self.next_sentence_button.grid(row=2, column=1, sticky="nsew")
        self.record_button.grid(row=2, column=2, sticky="nsew", columnspan=2)
        self.setup_column_configure(5)
        self.setup_row_configure(4)

    def setup_column_configure(self, num_columns):
        for col in range(num_columns):
            self.grid_columnconfigure(col, weight=1)

    def setup_row_configure(self, num_rows):
        for row in range(num_rows):
            self.grid_rowconfigure(row, weight=1, minsize=30)
