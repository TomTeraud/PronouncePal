from tkinter import filedialog, messagebox, simpledialog
from database_handler import SentenceWordHandler as SWH

class FileMenuHandler:
    @classmethod
    def handle_text_file_upload_with_args(cls, grand_parent):
        if cls.select_file():
            grand_parent.restart_all_widgets(True)

    @classmethod
    def select_file(cls):
        file_types = [("Text Files", "*.txt")]
        selected_file_path = filedialog.askopenfilename(filetypes=file_types)

        if selected_file_path:
            SWH.populate_sentences_table(selected_file_path)
            SWH.populate_words_table()
            messagebox.showinfo("Success", "Text file uploaded successfully!")
            return True  # Return True to indicate success
        else:
            return False  # Return False to indicate failure


    @classmethod
    def handle_text_samples_delete_with_args(cls, grand_parent):
        if cls.delete_samples_from_db():
            # Delete the object using the 'del' statement
            del grand_parent.text_sample
            grand_parent.restart_all_widgets(True)
    
    @classmethod
    def delete_samples_from_db(cls):
        confirmation_text = "DELETE"  # Confirmation text required from the user
        user_input = simpledialog.askstring("Confirm Deletion", "Type 'DELETE' to confirm deletion:")
        if user_input == confirmation_text:
            SWH.delete_all_rows()
            return True  # Return True to indicate success
        else:
            messagebox.showinfo("Info", "Deletion was not confirmed.")
            return False
        

    @staticmethod
    def change_transcriber_return_to_tp(grand_parent):
        grand_parent.restart_all_widgets(False)