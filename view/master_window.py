from tkinter import *
from tkinter import ttk

class MasterWindow:
    root = None
    mainframe = None
    def __init__(self):
        if MasterWindow.root is None:
            MasterWindow.root = Tk()
        if MasterWindow.mainframe is None:
            MasterWindow.mainframe = self.mainframe = ttk.Frame(self.root, padding="5 5 5 5", borderwidth="5", relief="solid")

        self.root = MasterWindow.root
        self.root.title("PronouncePal")
        self.root.geometry("300x300")
        self.column_row_configure(self.root, 1, 1)

        self.mainframe = MasterWindow.mainframe    
        self.mainframe.grid(column=0, row=0, sticky=(N, S, E, W))

    def column_row_configure(self, frame: Frame, num_columns: int, num_rows :int) ->None:
        for col in range(num_columns):
            frame.grid_columnconfigure(col, weight=1, minsize=20)
        for row in range(num_rows):
            frame.grid_rowconfigure(row, weight=1, minsize=30)
