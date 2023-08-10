import tkinter as tk
from tkinter import ttk

class ButtonManager(tk.Frame):
    def __init__(self, parent, text_sample, text_field_instance):
        super().__init__(parent, borderwidth=10, relief="solid")
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance

        # Create the "Click Me" button and associate it with the on_button_click method
        self.click_button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.click_button.grid(column=3, row=3)

        # Call the update_button_state method initially to set the button state
        self.update_button_state()

    def on_button_click(self):
        # Update the text sample and the displayed text in the text field
        self.text_sample.update_sample()
        self.text_field_instance.update_text_sample()

        # Update the button state after updating the sample
        self.update_button_state()

    def update_button_state(self):
        if self.text_sample.sample_exists:
            self.click_button.config(state=tk.NORMAL)  # Enable the button
        else:
            self.click_button.config(state=tk.DISABLED)  # Disable the button
