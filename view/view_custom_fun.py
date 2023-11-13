from tkinter import *


def column_row_configure(frame: Frame, num_columns: int, num_rows :int) ->None:
    for col in range(num_columns):
        frame.grid_columnconfigure(col, weight=1, minsize=20)
    for row in range(num_rows):
        frame.grid_rowconfigure(row, weight=1, minsize=30)
