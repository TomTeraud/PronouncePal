import tkinter as tk
from tkinter import ttk


class SampleTextField(tk.Text):
    def __init__(self, parent, text_sample):
        super().__init__(parent, wrap="word")
        self.text_sample = text_sample

        self.update_text_sample()

    def update_text_sample(self):
        sample_text = self.text_sample.sample
        self.delete("1.0", tk.END)
        self.insert("1.0", sample_text)

class PhonemicTextField(tk.Text):
    def __init__(self, parent, phoneme_sample):
        super().__init__(parent, wrap="word")
        self.phoneme_sample = phoneme_sample

        self.update_sample()

    def update_sample(self):
        phoneme_sample = self.phoneme_sample.phoneme
        self.delete("1.0", tk.END)
        self.insert("1.0", phoneme_sample)

class SampleTextFrame(ttk.Frame):
    def __init__(self, parent, text_sample):
        super().__init__(parent)
        self.text_sample = text_sample

        self.sample_text_field = SampleTextField(self, self.text_sample)
        self.sample_text_field.grid(row=0, column=0, sticky="nsew")

        self.phoneme_text_field = PhonemicTextField(self, self.text_sample)
        self.phoneme_text_field.grid(row=1, column=0, sticky="nsew")

        # Configure row and column weights to make the frame expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def update_text_sample(self):
        # Update the text sample in SampleTextField and PhonemicTextField
        self.sample_text_field.update_text_sample()
        self.phoneme_text_field.update_sample()

class TranscribedTextField(tk.Text):
    def __init__(self, parent):
        super().__init__(parent, borderwidth=4, relief="solid", wrap="word")

    def update_transcribed_text(self, transcribed_text):
        # Clear the existing content and insert new transcribed text
        self.delete("1.0", tk.END)
        self.insert("1.0", transcribed_text)
