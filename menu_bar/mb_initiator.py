import tkinter as tk
from menu_bar._file_handler import FileMenuHandler as FMH
from menu_bar._help_handler import HelpMenuHandler as HMH
from menu_bar._rating_handler import RatingMenuHandler as RMH


class MenuInitiator(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.create_menus()

    def create_menus(self):
        if self.parent.ready_state:
            self.create_file_menu() # Skip this if on titlepage
        self.create_rating_menu()
        self.create_help_menu()

    def create_file_menu(self):
        menu_file = tk.Menu(self)
        self.add_cascade(menu=menu_file, label='File')
        
        menu_file.add_command(
            label="Add text file to database",
            command=lambda: FMH.handle_text_file_upload_with_args(self.parent))

        menu_file.add_command(
            label="Delete all text samples from database", 
            command=lambda:FMH.handle_text_samples_delete_with_args(self.parent))
        
        menu_file.add_command(
            label="Change transcriber", 
            command=lambda:FMH.change_transcriber_return_to_tp(self.parent))

    def create_rating_menu(self):
        menu_rating = tk.Menu(self)
        self.add_cascade(menu=menu_rating, label='Ratings')
        menu_rating.add_command(label="Sentences ratings", command=RMH.show_sentences_ratings)
        menu_rating.add_command(label="Words ratings", command=RMH.show_words_ratings)

    def create_help_menu(self):
        menu_help = tk.Menu(self)
        self.add_cascade(menu=menu_help, label='Help')
        menu_help.add_command(label="Readme", command=HMH.show_readme)
