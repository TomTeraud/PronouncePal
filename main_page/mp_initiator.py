from tkinter import ttk
from main_page.text_fields.text_fields import *
from main_page.buttons.mpb_main import SentenceSampleButton, RecordButton, WordSampleButton
from main_page.buttons.mpb_controller import MainPageButtonController
from main_page.progress_bars.recording_progres_bar import RecordingProgresBar
from main_page.progress_bars.rating_bar import RatingBar

class MainPageInitiator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.progress_bar = RecordingProgresBar(self, parent)
        self.rating_bar = RatingBar(self, parent)
        
        self.sample_text_field = SampleTextField(self, parent)
        if self.parent.tp_phoneme_cb_state:
            self.phonemic_text_field = PhonemicTextField(self, parent)
        self.transcribed_text_field = TranscribedTextField(self)

        self.mpb_controller = MainPageButtonController()
        self.next_word_button = WordSampleButton(self, parent)
        self.next_sentence_button = SentenceSampleButton(self, parent)
        self.record_button = RecordButton(self)
        self.configure_layout()

    def configure_layout(self):
        self.progress_bar.grid(row=3, column=0, sticky="nsew", columnspan=5)
        self.rating_bar.grid(row=0, column=5, sticky="nsew", rowspan=3)
        # adjust grid based on phenomic_on
        if self.parent.tp_phoneme_cb_state:
            self.sample_text_field.grid(row=0, column=0, sticky="nsew", columnspan=2)
            self.phonemic_text_field.grid(row=1, column=0, sticky="nsew", columnspan=2)
        else: 
            self.sample_text_field.grid(row=0, column=0, sticky="nsew", columnspan=2, rowspan=2)
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
