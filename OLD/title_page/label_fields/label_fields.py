from tkinter import ttk
import tkinter.font as tkFont

class WelcomeSelTransc(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="Welcome! Please select transcriber", anchor="center")
        
        # Create a custom font with bold style
        bold_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
        
        # Apply the custom font to the label
        self.config(font=bold_font)


class OtherSetings(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="Other setings", anchor="center")

        # Create a custom font with bold style
        bold_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        
        # Apply the custom font to the label
        self.config(font=bold_font)