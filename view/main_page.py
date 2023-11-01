from tkinter import *
from tkinter import ttk
from typing import Protocol


class Presenter(Protocol):

    def handle_new_word_loading(self, event=None) -> None:
        ...

    def handle_new_sentence_loading(self, event=None) -> None:
        ...

    def handle_recording_start(self, event=None) -> None:
        ...

    def handle_avg_rating_receiving(self, event=None) -> int:
        ...

class PronouncePal(Protocol):
    frame = ttk.Frame



class MainPagesWidgets():
    _MAX_PROGRESS = 100

    def __init__(self, parent:PronouncePal, presenter:Presenter) -> None:
        self.frame = parent.frame
        self.create_main_page_widgets()
        self.place_widgets_on_grid()
        self.setup_widgets_items(presenter)


    def create_main_page_widgets(self):
        self.new_word_button = ttk.Button(self.frame)
        self.new_sentence_button = ttk.Button(self.frame)
        self.rec_start_button = ttk.Button(self.frame)
        self.sample_text_field = Text(self.frame, height=10, width=30, wrap="word")
        self.transcribed_text_field = Text(self.frame, height=10, width=30, wrap="word")
        self.rating_bar = ttk.Progressbar(self.frame, mode="determinate", maximum=self._MAX_PROGRESS, orient="vertical")

    def set_button_names(self, state: int, time: float = None) -> None:
        names = {
            "word": ("Load new word", "recording", "transcribing"),
            "sentence": ("Load new sentence", "recording", "transcribing"),
            "record": ("Start recording", "recording", "transcribing"),
        }
        
        # Update the "record" button text by formatting the string
        if time is not None:
            names["record"] = (f"Start recording {time} seconds", "recording", "transcribing")

        self.new_word_button.config(text=names["word"][state])
        self.new_sentence_button.config(text=names["sentence"][state])
        self.rec_start_button.config(text=names["record"][state])


    def set_button_state(self, state: int) -> None:
        if state == 0:
            self.new_word_button.config(state=NORMAL)
            self.new_sentence_button.config(state=NORMAL)
            self.rec_start_button.config(state=NORMAL)
        elif state == 1:
            self.new_word_button.config(state=DISABLED)
            self.new_sentence_button.config(state=DISABLED)
            self.rec_start_button.config(state=DISABLED)     
            
    def place_widgets_on_grid(self):
        self.new_word_button.grid(row=1, column=0, sticky=NSEW)
        self.new_sentence_button.grid(row=1, column=1, sticky=NSEW)
        self.rec_start_button.grid(row=1, column=2, sticky=NSEW, columnspan=2)
        self.sample_text_field.grid(row=0, column=0, sticky=NSEW, columnspan=2)
        self.transcribed_text_field.grid(row=0, column=2, sticky=NSEW, columnspan=2)
        self.rating_bar.grid(row=0, column=5, sticky="nsew", rowspan=2)

    def setup_widgets_items(self, presenter:Presenter):
        self.new_word_button.bind("<Button-1>", presenter.handle_new_word_loading)
        self.new_sentence_button.bind("<Button-1>", presenter.handle_new_sentence_loading)
        self.rec_start_button.bind("<Button-1>", presenter.handle_recording_start)
        self.manage_rating_bar_item(presenter)

    def manage_rating_bar_item(self, presenter:Presenter):
        self._progress_var = DoubleVar()
        self.rating_bar.configure(variable=self._progress_var)
        self.update_rating_bar_base_value()

    def update_rating_bar_base_value(self, rating:int = 0):
        self._progress_var.set(rating)

    def update_transcribed_text_field(self, sample:str):
        self.clear_transcribed_text_field()
        self.transcribed_text_field.insert("1.0", sample)        

    def update_text_field(self, sample: str) -> None:
        self.clear_sample_text_field()
        self.clear_transcribed_text_field()
        self.sample_text_field.insert("1.0", sample)

    def clear_transcribed_text_field(self) -> None:
        self.transcribed_text_field.delete("1.0", END)

    def clear_sample_text_field(self) -> None:
        self.sample_text_field.delete("1.0", END)
