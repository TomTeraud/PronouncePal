from tkinter import *

class ReadmeHandler:
    @staticmethod
    def show_readme(readme_content: str) -> None:
        # Create a new window to display the readme content
        readme_window = Toplevel()
        readme_window.title("Readme")
        readme_text = Text(readme_window, wrap=WORD)
        readme_text.grid(column=0, row=0, sticky=(N, S, E, W))

        # Insert the readme content into the Text widget
        readme_text.insert(END, readme_content)
        readme_text.config(state=DISABLED)  # Make it read-only
