from tkinter import Frame

def column_row_configure(frame: Frame, num_columns: int, num_rows: int) -> None:
    # Reset the column configuration
    for col in range(frame.grid_size()[0]):
        frame.grid_columnconfigure(col, weight=0, minsize=0)
    
    # Reset the row configuration
    for row in range(frame.grid_size()[1]):
        frame.grid_rowconfigure(row, weight=0, minsize=0)

    # Apply the new configuration
    for col in range(num_columns):
        frame.grid_columnconfigure(col, weight=1, minsize=20)
    
    for row in range(num_rows):
        frame.grid_rowconfigure(row, weight=1, minsize=30)
