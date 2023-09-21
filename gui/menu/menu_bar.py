import tkinter as tk
from gui.menu.file_handler import FileMenuHandler
from gui.menu.api_handler import ApiMenuHandler
from helpers import resource_path


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
        self.create_help_menu()

    def create_file_menu(self):
        menu_file = tk.Menu(self)
        self.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label="Add text file to database", command=self.handle_text_file_upload)
        menu_file.add_command(label="Delete all text samples from database", command=self.handle_text_samples_delete)
        # Add other file menu items as needed

    def handle_text_file_upload(self):
        result = FileMenuHandler.select_file()
        if result:
            self.update_gui()

    def handle_text_samples_delete(self):
        result = FileMenuHandler.delete_samples_from_db()
        if result:
            self.update_gui()        

    def create_api_menu(self):
        menu_api = tk.Menu(self)
        self.add_cascade(menu=menu_api, label='API')
        menu_api.add_command(label="Set your chatGPT API key", command=self.handle_api_key_result)

    def handle_api_key_result(self):
        result = ApiMenuHandler.get_api_key()
        if result:
            self.button_manager.set_api_key_status(result)
            self.update_gui()

    def create_help_menu(self):
        menu_help = tk.Menu(self)
        self.add_cascade(menu=menu_help, label='Help')
        menu_help.add_command(label="Readme", command=self.show_readme)

    def show_readme(self):
        
        readme_path = resource_path("README.md")

        # Read the contents of the readme.md file with UTF-8 encoding
        with open(readme_path, 'r', encoding='utf-8') as file:
            readme_content = file.read()

        # Create a new window to display the readme content
        readme_window = tk.Toplevel(self)
        readme_window.title("Readme")
        readme_text = tk.Text(readme_window, wrap=tk.WORD)
        readme_text.pack(fill=tk.BOTH, expand=True)

        # Insert the readme content into the Text widget
        readme_text.insert(tk.END, readme_content)
        readme_text.config(state=tk.DISABLED)  # Make it read-only

    def update_gui(self):
        self.text_sample.update_sample()
        self.text_field_instance.update_text_sample()
        self.button_manager.update_buttons()