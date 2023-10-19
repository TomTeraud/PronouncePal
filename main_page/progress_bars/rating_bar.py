import tkinter as tk
from tkinter import ttk

class RatingBar(ttk.Progressbar):
    _MAX_PROGRESS = 100

    def __init__(self, parent, grand_parent):
        self.text_sample = grand_parent.text_sample
        self.parent = parent

        self._progress_var = tk.DoubleVar()
        self.rating = self.text_sample.avg_rating if self.text_sample.avg_rating is not None else 0
        self._progress_var.set(self.rating)

        super().__init__(self.parent, mode="determinate", maximum=self._MAX_PROGRESS, orient="vertical")
        self.configure(variable=self._progress_var)

    def update_rating(self, new_rating):
        self.rating = new_rating if new_rating is not None else 0
        self._progress_var.set(self.rating)