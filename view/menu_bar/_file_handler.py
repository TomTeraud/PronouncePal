from tkinter import filedialog, messagebox, simpledialog

class FileMenuHandler:

    @staticmethod
    def get_path() -> str:
        file_types = [("Text Files", "*.txt")]
        return filedialog.askopenfilename(filetypes=file_types)
    
    @staticmethod
    def message_file_upload_status(status:bool) -> None:
        if status:
            messagebox.showinfo("Success", "Text file uploaded successfully!")
        else:
            messagebox.showinfo("Info", "File upload error")


    # @classmethod
    # def handle_text_samples_delete_with_args(cls, grand_parent):
    #     if cls.delete_samples_from_db():
    #         # Delete the object using the 'del' statement
    #         del grand_parent.text_sample
    #         grand_parent.restart_all_widgets(True)
    
    # @classmethod
    # def delete_samples_from_db(cls):
    #     confirmation_text = "DELETE"  # Confirmation text required from the user
    #     user_input = simpledialog.askstring("Confirm Deletion", "Type 'DELETE' to confirm deletion:")
    #     if user_input == confirmation_text:
    #         SWH.delete_all_rows()
    #         return True  # Return True to indicate success
    #     else:
    #         messagebox.showinfo("Info", "Deletion was not confirmed.")
    #         return False
        

    # @staticmethod
    # def change_transcriber_return_to_tp(grand_parent):
    #     grand_parent.restart_all_widgets(False)