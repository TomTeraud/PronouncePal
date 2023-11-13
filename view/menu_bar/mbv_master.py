from tkinter import *
from tkinter import Menu
from typing import Protocol

from view.master_view import MasterView



class MenuBarPresenter(Protocol):
        
    def open_file(self, event=None):
        ...
    def save_file(self, event=None):
        ...
    def handle_readme_clicked(self, event=None):
        ...

class MenuBarView(MasterView):
    def __init__(self):
        super().__init__()
        self.menubar = Menu(self)
        self.config(menu=self.menubar)

    def setup_page_menubar(self, presenter: MenuBarPresenter) -> None:
        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=presenter.open_file)
        file_menu.add_command(label="Save", command=presenter.save_file)
        file_menu.add_command(label="Readme", command=presenter.handle_readme_clicked)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        
    def main_page_menubar(self, presenter) -> None:
        demo_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Ratings", menu=demo_menu)

    def show_readme(self, readme_content: str) -> None:
        # Create a new window to display the readme content
        readme_window = Toplevel()
        readme_window.title("Readme")
        readme_text = Text(readme_window, wrap=WORD)
        readme_text.grid(column=0, row=0, sticky=(N, S, E, W))

        # Insert the readme content into the Text widget
        readme_text.insert(END, readme_content)
        readme_text.config(state=DISABLED)  # Make it read-only

