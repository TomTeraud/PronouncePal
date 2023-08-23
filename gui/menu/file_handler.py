from tkinter import filedialog, messagebox
from db.database_handler import DatabaseHandler as DH

class FileMenuHandler:
    @staticmethod
    def select_file():
        file_types = [("Text Files", "*.txt")]
        selected_file_path = filedialog.askopenfilename(filetypes=file_types)

        if selected_file_path:
            DH.get_and_save_sentences_from_text_file(selected_file_path)
            DH.save_words_from_sentences()
            messagebox.showinfo("Success", "Text file uploaded successfully!")
            return True  # Return True to indicate success
        else:
            return False  # Return False to indicate failure

    @staticmethod
    def delete_samples_from_db():
        try:
            DH.delete_all_rows()
            messagebox.showinfo("Success", "All text samples deleted successfully!")
            return True  # Return True to indicate success
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting text samples: {str(e)}")
            return False  # Return False to indicate failure
