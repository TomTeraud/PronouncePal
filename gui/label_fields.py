from tkinter import ttk

class MainSetupLabel(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="Welcome! Please select transcriber", anchor="center")