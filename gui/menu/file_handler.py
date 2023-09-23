from tkinter import filedialog, messagebox, simpledialog
from database_handler import DatabaseHandler as DH

class FileMenuHandler:
    @staticmethod
    def select_file():
        file_types = [("Text Files", "*.txt")]
        selected_file_path = filedialog.askopenfilename(filetypes=file_types)

        if selected_file_path:
            DH.populate_sentences_table_from_text_file(selected_file_path)
            DH.populate_words_table_from_sentences_table()
            messagebox.showinfo("Success", "Text file uploaded successfully!")
            return True  # Return True to indicate success
        else:
            return False  # Return False to indicate failure

    @staticmethod
    def delete_samples_from_db():
        confirmation_text = "DELETE"  # Confirmation text required from the user
        user_input = simpledialog.askstring("Confirm Deletion", "Type 'DELETE' to confirm deletion:")
        if user_input == confirmation_text:
            DH.delete_all_rows()
            return True  # Return True to indicate success
        else:
            messagebox.showinfo("Info", "Deletion was not confirmed.")
            return False