import tkinter as tk
from tkinter import filedialog
from db.database_handler import DatabaseHandler as DH

class MenuBar(tk.Menu):
    def __init__(self, parent, text_sample, text_field_instance, button_manager):
        super().__init__(parent)
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance
        self.button_manager = button_manager

        self.create_menus()

    def create_menus(self):
        self.create_file_menu()
        self.create_edit_menu()

    def create_file_menu(self):
        menu_file = tk.Menu(self)
        self.add_cascade(menu=menu_file, label='File')

    def create_edit_menu(self):
        menu_edit = tk.Menu(self)
        self.add_cascade(menu=menu_edit, label='Edit')
        menu_edit.add_command(label="Add text file to database", command=self.select_file)
        menu_edit.add_command(label="Remove all text samples from database", command=self.delete_samples_from_db)

    def select_file(self):
        file_types = [("Text Files", "*.txt")]
        selected_file_path = filedialog.askopenfilename(filetypes=file_types)

        if selected_file_path:
            DH.get_and_save_sentences_from_text_file(selected_file_path)
            DH.save_words_from_sentences()
            self.update_ui()

    def delete_samples_from_db(self):
        DH.delete_all_rows()
        self.update_ui()

    def update_ui(self):
        self.text_sample.update_sample()
        self.text_field_instance.update_text_sample()
        self.button_manager.update_buttons()
