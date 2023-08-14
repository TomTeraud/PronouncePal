import tkinter as tk

class SampleTextField(tk.Text):
    def __init__(self, parent, text_sample, column, row):
        super().__init__(parent, borderwidth=10, relief="solid")

        self.text_sample = text_sample

        # Configure column and row weights for resizing
        parent.columnconfigure(column, weight=1)
        parent.rowconfigure(row, weight=1)

        # Call method to update the displayed text sample
        self.update_text_sample()

    def update_text_sample(self):
        # Get the current text sample from the text_sample object
        sample_text = self.text_sample.sample

        # Clear and update the Text widget for the text sample
        self.delete("1.0", tk.END)
        self.insert("1.0", sample_text)



class TranscribedTextField(tk.Text):
    def __init__(self, parent, transcriber, column, row):
        super().__init__(parent, borderwidth=10, relief="solid")
        self.transcriber = transcriber
        # Configure column and row weights for resizing
        parent.columnconfigure(column, weight=1)
        parent.rowconfigure(row, weight=1)

    def update_transcribed_text(self):
        # Clear and update the Text widget for the transcribed text
        transcribed_text = self.transcriber.transcribed_text
        self.delete("1.0", tk.END)
        self.insert("1.0", transcribed_text)