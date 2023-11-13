from tkinter import *
from tkinter import ttk
from view.view_custom_fun import column_row_configure

class MasterView(Tk):
    def __init__(self):
        super().__init__()
        self.title("PronouncePal")
        self.geometry("300x200")
        column_row_configure(self, 1, 1)
        self.mainframe = ttk.Frame(self, borderwidth=3, relief="solid")
        self.mainframe.grid(column=0, row=0, sticky=(N, S, E, W))

