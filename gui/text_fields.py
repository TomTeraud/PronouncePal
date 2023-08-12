import tkinter as tk

class TextField(tk.Frame):
    def __init__(self, parent, text_sample):
        super().__init__(parent, borderwidth=10, relief="solid")
        self.text_sample = text_sample

        # Create a Text widget to display the text sample
        self.sample_text_widget = tk.Text(self)
        self.sample_text_widget.grid(row=0, column=0, sticky="nsew")

        # Create a Text widget to display the transcribed text
        self.transcribed_text_widget = tk.Text(self)
        self.transcribed_text_widget.grid(row=1, column=0, sticky="nsew")

        # Call method to update the displayed text sample
        self.update_text_sample()

    def update_text_sample(self):
        # Get the current text sample from the text_sample object
        sample_text = self.text_sample.sample

        # Clear and update the Text widget for the text sample
        self.sample_text_widget.delete("1.0", tk.END)
        self.sample_text_widget.insert("1.0", sample_text)

    def update_transcribed_text(self, transcribed_text):
        # Clear and update the Text widget for the transcribed text
        self.transcribed_text_widget.delete("1.0", tk.END)
        self.transcribed_text_widget.insert("1.0", transcribed_text)
