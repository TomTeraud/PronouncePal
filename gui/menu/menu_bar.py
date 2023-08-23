import tkinter as tk
from gui.menu.file_handler import FileMenuHandler
from gui.menu.api_handler import ApiMenuHandler

class MenuBar(tk.Menu):
    def __init__(self, parent, text_sample, text_field_instance, button_manager):
        super().__init__(parent)
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance
        self.button_manager = button_manager

        self.create_menus()

    def create_menus(self):
        self.create_file_menu()
        self.create_api_menu()

    def create_file_menu(self):
        menu_file = tk.Menu(self)
        self.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label="Add text file to database", command=FileMenuHandler.select_file)
        # Add other file menu items as needed

    def create_api_menu(self):
        menu_api = tk.Menu(self)
        self.add_cascade(menu=menu_api, label='API')
        menu_api.add_command(label="Set your chatGPT API key", command=self.handle_api_key_result)

    def handle_api_key_result(self):
        result = ApiMenuHandler.get_api_key()
        if result:
            self.button_manager.set_api_key_status(result)
            self.update_ui()

    def update_ui(self):
        self.text_sample.update_sample()
        self.text_field_instance.update_text_sample()
        self.button_manager.update_buttons()