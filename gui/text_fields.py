import tkinter as tk
from tkinter import ttk

class TextField(tk.Frame):
    def __init__(self, parent, text_sample):
        super().__init__(parent, borderwidth=10, relief="solid")
        self.text_sample = text_sample

        # Create a Text widget to display the text sample
        self.text_widget = tk.Text(self)
        self.text_widget.grid(row=0, column=0, sticky="nsew")

        # Call method to update the displayed text sample
        self.update_text_sample()

    def update_text_sample(self):
        # Get the current text sample from the text_sample object
        sample_text = self.text_sample.sample

        # Clear the Text widget and insert the new text sample
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", sample_text)