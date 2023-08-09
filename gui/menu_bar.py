import tkinter as tk
from tkinter import filedialog
from db.database_handler import create_sample_from_text_file

class MenuBar(tk.Menu):
    def __init__(self, parent, text_sample):
        super().__init__(parent)
        self.text_sample = text_sample
        self.update_sample = text_sample.update_sample
        self.sample_exists = text_sample.sample_exists
        # Adding menu
        menu_file = tk.Menu(self)
        menu_edit = tk.Menu(self)
        self.add_cascade(menu=menu_file, label='File')
        self.add_cascade(menu=menu_edit, label='Edit')

        # Add options to the File menu (if any)
        # ...

        # Add options to the Edit menu
        menu_edit.add_command(label="Add text file to library", command=self.select_file)

    def select_file(self):
        # Define the file types filter to only allow .txt files
        file_types = [("Text Files", "*.txt")]

        # Open a file selection window and store the selected file path in the variable
        self.selected_file_path = filedialog.askopenfilename(filetypes=file_types)

        if self.selected_file_path:
            print("Selected file:", self.selected_file_path)
            # Populate db
            create_sample_from_text_file(self.selected_file_path)
            self.text_sample.update_sample()
