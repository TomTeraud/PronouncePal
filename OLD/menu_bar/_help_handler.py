import tkinter as tk
from OLD.helpers import resource_path

class HelpMenuHandler:
    @staticmethod
    def show_readme():
        readme_path = resource_path("README.md")

        # Read the contents of the readme.md file with UTF-8 encoding
        with open(readme_path, 'r', encoding='utf-8') as file:
            readme_content = file.read()

        # Create a new window to display the readme content
        readme_window = tk.Toplevel()
        readme_window.title("Readme")
        readme_text = tk.Text(readme_window, wrap=tk.WORD)
        readme_text.pack(fill=tk.BOTH, expand=True)

        # Insert the readme content into the Text widget
        readme_text.insert(tk.END, readme_content)
        readme_text.config(state=tk.DISABLED)  # Make it read-only
