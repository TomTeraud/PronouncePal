import tkinter as tk
from tkinter import ttk

class PhonemeEnabler(ttk.Checkbutton):
    def __init__(self, parent, get_state, set_state):
        self.get_state = get_state
        self.set_state = set_state
        self._state = self.get_state()
        # Create a Tkinter variable to store the state of the checkbox
        self.checkbox_state = tk.BooleanVar(value=self._state)
        super().__init__(parent, text="Enable phoneme", command=self.on_checkbox_change, variable=self.checkbox_state)
        
    # Function to handle the checkbox state change
    def on_checkbox_change(self):
        if self.get_state():
            self._state = False 
        else:
            self._state = True 
        # Update the checkbox state to the value returned by get_phoneme_state
        self.checkbox_state.set(self._state)
        # Update grand parent tp_phoneme_cb_state value
        self.set_state(self._state)