from tkinter import *
from tkinter import ttk
from typing import Protocol

from view.master_view import MasterView

class MainPresenter(Protocol):
    def handle_main_button_click(self, event=None) -> None:
        ...

class MainView(MasterView):
    def __init__(self):
        super().__init__()

    def create_main_widgets(self, presenter: MainPresenter) -> None:
        label = ttk.Label(self.mainframe, text="Main page")
        label.grid(column=0, row=0, sticky=(N, S, E, W))
        main_button = ttk.Button(self.mainframe, text="Main button")
        main_button.grid(column=0, row=1, sticky=(N, S, E, W))
        main_button.config(command=presenter.handle_main_button_click)
    
    # def init_main_page(self, presenter: Presenter) -> None:
    #     self.column_row_configure(self.mainframe, 5, 3)
    #     self.create_main_page_widgets(self.mainframe)
    #     self.place_widgets_on_grid()
    #     self.make_main_widgets_items(presenter)
    #     self.add_main_menus()

    # def create_main_page_widgets(self, frame) -> None:
    #     self.new_word_button = ttk.Button(frame)
    #     self.new_sentence_button = ttk.Button(frame)
    #     self.rec_start_button = ttk.Button(frame)
    #     self.sample_text_field = Text(frame, height=10, width=30, wrap="word")
    #     self.transcribed_text_field = Text(frame, height=10, width=30, wrap="word")
    #     self.rating_bar = ttk.Progressbar(frame, mode="determinate", maximum=100, orient="vertical")
    #     self.recording_bar = RPB(frame)

    # def set_button_names(self, state: int, time: float = None) -> None:
    #     rec, trn = "recording" , "transcribing"
    #     names = {
    #         "word": ("Load new word", f"{rec}", f"{trn}"),
    #         "sentence": ("Load new sentence", f"{rec}", f"{trn}"),
    #         "record": ("Start recording", f"{rec}", f"{trn}"),
    #     }
    #     if time is not None:
    #         names["record"] = (f"Start recording {time} seconds", f"{rec}", f"{trn}")

    #     self.new_word_button.config(text=names["word"][state])
    #     self.new_sentence_button.config(text=names["sentence"][state])
    #     self.rec_start_button.config(text=names["record"][state])

    # def set_buttons_state(self, state: int) -> None:
    #     if state == 0:
    #         self.new_word_button.config(state=NORMAL)
    #         self.new_sentence_button.config(state=NORMAL)
    #         self.rec_start_button.config(state=NORMAL)
    #     elif state == 1:
    #         self.new_word_button.config(state=DISABLED)
    #         self.new_sentence_button.config(state=DISABLED)
    #         self.rec_start_button.config(state=DISABLED)     
            
    # def place_widgets_on_grid(self) -> None:
    #     self.new_word_button.grid(row=1, column=0, sticky=NSEW)
    #     self.new_sentence_button.grid(row=1, column=1, sticky=NSEW)
    #     self.rec_start_button.grid(row=1, column=2, sticky=NSEW, columnspan=2)
    #     self.sample_text_field.grid(row=0, column=0, sticky=NSEW, columnspan=2)
    #     self.transcribed_text_field.grid(row=0, column=2, sticky=NSEW, columnspan=2)
    #     self.rating_bar.grid(row=0, column=4, sticky="nsew", rowspan=2)
    #     self.recording_bar.grid(row=2, column=0, sticky="nsew", columnspan=5)

    # def make_main_widgets_items(self, presenter:Presenter) -> None:
    #     self.new_word_button.bind("<Button-1>", presenter.handle_new_word_loading)
    #     self.new_sentence_button.bind("<Button-1>", presenter.handle_new_sentence_loading)
    #     self.rec_start_button.bind("<Button-1>", presenter.handle_recording_start)
    #     self.manage_rating_bar_item()

    # def manage_rating_bar_item(self) -> None:
    #     self._rating_progress_var = DoubleVar()
    #     self.rating_bar.configure(variable=self._rating_progress_var)
    #     self.update_rating_bar_base_value()

    # def update_rating_bar_base_value(self, rating:int = 0) -> None:
    #     self._rating_progress_var.set(rating)

    # def update_transcribed_text_field(self, sample:str) -> None:
    #     self.clear_transcribed_text_field()
    #     self.transcribed_text_field.insert("1.0", sample)        

    # def update_text_field(self, sample: str) -> None:
    #     self.clear_sample_text_field()
    #     self.clear_transcribed_text_field()
    #     self.sample_text_field.insert("1.0", sample)

    # def clear_transcribed_text_field(self) -> None:
    #     self.transcribed_text_field.delete("1.0", END)

    # def clear_sample_text_field(self) -> None:
    #     self.sample_text_field.delete("1.0", END)

    # def recording_bar_start(self, time: float) -> None:
    #     self.recording_bar.start_recording_bar_progress(time)

    # def add_main_menus(self) -> None:
    #     ...
    #     # self.setup_menu = Menu(self.menubar)
    #     # self.menubar.add_cascade(menu=self.setup_menu, label='Setup')
        