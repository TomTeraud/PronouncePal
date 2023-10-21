import tkinter as tk
from tkinter import ttk


class PhonemeEnabler(ttk.Checkbutton):
    def __init__(self, parent, g_parent):
        # Create a Tkinter variable to store the state of the checkbox
        self.checkbox_state = tk.BooleanVar(value=g_parent.tp_phoneme_cb_state)
        self.g_parent = g_parent
        super().__init__(parent, text="Enable phoneme", command=self.on_checkbox_change, variable=self.checkbox_state,)

    # Function to handle the checkbox state change
    def on_checkbox_change(self):
        self.g_parent.phoneme_enabler_state_update(self.checkbox_state.get())
        