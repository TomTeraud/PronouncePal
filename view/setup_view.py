from tkinter import *
from tkinter import ttk
from typing import Protocol
from view.master_window import MasterWindow

class Presenter(Protocol):
    def handle_main_view_start(self, event=None) -> None:
        ...

class SetupView(MasterWindow):
    def __init__(self):
        super().__init__()

    def mainloop(self) -> None:
        self.root.mainloop()

    def init_setup_page(self, presenter: Presenter) -> None:
        self.column_row_configure(self.mainframe, 2, 3)
        self.setup_widgets_items(presenter)

    def setup_widgets_items(self, presenter:Presenter) -> None:

        label = ttk.Label(self.mainframe, text="SETUP PAGE!")
        button1 = ttk.Button(self.mainframe, text="Button 1")
        button2 = ttk.Button(self.mainframe, text="Button 2")
        button3 = ttk.Button(self.mainframe, text="Start")

        # Place buttons in specific grid cells
        label.grid(row=0, column=0, sticky=(N, S, E, W), columnspan="2")
        button1.grid(row=1, column=0, sticky=(N, S, E, W))
        button2.grid(row=1, column=1, sticky=(N, S, E, W))
        button3.grid(row=2, column=0, sticky=(N, S, E, W), columnspan=2)

        button3.bind("<Button-1>", presenter.handle_main_view_start)

    def destroy_all_widgets(self) -> None:
        # Get a list of all widgets in the frame
        widgets = self.mainframe.winfo_children()

        # Loop through the widgets and destroy each one
        for widget in widgets:
            widget.destroy()