from tkinter import BooleanVar, ttk

class PhonemeEnabler(ttk.Checkbutton):
    def __init__(self, frame):
        self._state = False
        # Create a Tkinter variable to store the state of the checkbox
        self.checkbox_state = BooleanVar(value=self._state)
        super().__init__(frame, text="Enable phoneme", variable=self.checkbox_state)
        
    # Function to handle the checkbox state change
    def on_checkbox_change(self, status: bool) -> None:
        self._state = status
        # Update the checkbox state value
        self.checkbox_state.set(self._state)
