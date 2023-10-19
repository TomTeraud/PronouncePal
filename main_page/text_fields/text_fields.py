import tkinter as tk

class SampleTextField(tk.Text):
    def __init__(self, parent, grand_parent):
        super().__init__(parent, wrap="word")
        self.text_sample = grand_parent.text_sample

        self.update_text_sample()

    def update_text_sample(self):
        sample_text = self.text_sample.sample
        if sample_text:
            self.delete("1.0", tk.END)
            self.insert("1.0", sample_text)

class PhonemicTextField(tk.Text):
    def __init__(self, parent, grand_parent):
        super().__init__(parent, wrap="word")
        self.text_sample = grand_parent.text_sample

        self.update_sample()

    def update_sample(self):
        sample_text = self.text_sample.sample
        if sample_text:
            phoneme_sample = self.text_sample.phoneme
            self.delete("1.0", tk.END)
            self.insert("1.0", phoneme_sample)

class TranscribedTextField(tk.Text):
    def __init__(self, parent):
        super().__init__(parent, wrap="word")

    def update_transcribed_text(self, transcribed_text):
        self.delete("1.0", tk.END)
        self.insert("1.0", transcribed_text)
