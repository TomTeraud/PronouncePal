import tkinter as tk
from tkinter import ttk

class ButtonManager(tk.Frame):
    def __init__(self, parent, text_sample, text_field_instance):
        super().__init__(parent, borderwidth=10, relief="solid")
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance

        # Create a button and associate it with a command
        self.click_button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.click_button.grid(column=3, row=3)

    def on_button_click(self):
        # Update the text sample and call the update_text_sample method of TextField
        self.text_sample.update_sample()
        self.text_field_instance.update_text_sample()
        print(f"Button Clicked! Text Sample: {self.text_sample.sample}")
