from tkinter import filedialog
from db.database_handler import DatabaseHandler as DH

class FileMenuHandler:
    @staticmethod
    def select_file():
        file_types = [("Text Files", "*.txt")]
        selected_file_path = filedialog.askopenfilename(filetypes=file_types)

        if selected_file_path:
            DH.get_and_save_sentences_from_text_file(selected_file_path)
            DH.save_words_from_sentences()


    def delete_samples_from_db(self):
        DH.delete_all_rows()
        self.update_ui()