import tkinter as tk
from tkinter import filedialog
from db.database_handler import create_sample_from_text_file

class MenuBar(tk.Menu):
    def __init__(self, parent, text_sample, text_field_instance, button_manager):
        super().__init__(parent)
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance
        self.button_manager = button_manager

        self.create_menus()

    def create_menus(self):
        # Create "File" and "Edit" menus
        menu_file = tk.Menu(self)
        menu_edit = tk.Menu(self)
        self.add_cascade(menu=menu_file, label='File')
        self.add_cascade(menu=menu_edit, label='Edit')

        # Add options to the "Edit" menu
        menu_edit.add_command(label="Add text file to library", command=self.select_file)

    def select_file(self):
        # Define the file types filter to only allow .txt files
        file_types = [("Text Files", "*.txt")]

        # Open a file selection window and store the selected file path
        selected_file_path = filedialog.askopenfilename(filetypes=file_types)

        if selected_file_path:
            # Populate the database with the selected text file
            create_sample_from_text_file(selected_file_path)

            # Update both buttons and text field
            self.text_sample.update_sample()
            self.text_field_instance.update_text_sample()
            self.button_manager.update_buttons()
