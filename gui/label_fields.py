from tkinter import ttk

class MainSetupLabel(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="Select transcriber", anchor="center")