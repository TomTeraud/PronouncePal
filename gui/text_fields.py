import tkinter as tk
from utils.transcribe_audio import Transcriber

class SampleTextField(tk.Text):
    def __init__(self, parent, text_sample):
        super().__init__(parent, borderwidth=10, relief="solid")
        self.text_sample = text_sample

        # Call method to update the displayed text sample
        self.update_text_sample()

    def update_text_sample(self):
        # Get the current text sample from the text_sample object
        sample_text = self.text_sample.sample

        # Clear and update the Text widget for the text sample
        self.delete("1.0", tk.END)
        self.insert("1.0", sample_text)


class TranscribedTextField(tk.Text):
    def __init__(self, parent):
        super().__init__(parent, borderwidth=10, relief="solid")

    def update_transcribed_text(self):
        # Define a callback function to update the Text widget
        def update_callback(transcribed_text):
            self.delete("1.0", tk.END)
            self.insert("1.0", transcribed_text)
        
        # Call the class method and pass the callback
        Transcriber.transcribe_audio(callback=update_callback)