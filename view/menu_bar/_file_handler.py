from tkinter import filedialog, messagebox, simpledialog

class FileMenuHandler:

    @staticmethod
    def get_path() -> str:
        file_types = [("Text Files", "*.txt")]
        return filedialog.askopenfilename(filetypes=file_types)
    
    @staticmethod
    def message_file_upload_status(status: bool) -> None:
        if status:
            messagebox.showinfo("Success", "Text file uploaded successfully!")
        else:
            messagebox.showinfo("Info", "File upload error")

    @staticmethod
    def confirmation() -> bool:
        confirmation_text = "DELETE"  # Confirmation text required from the user
        user_input = simpledialog.askstring("Confirm Deletion", "Type 'DELETE' to confirm deletion:")
        if user_input == confirmation_text:
            return True
        else:
            return False

    @staticmethod
    def message_data_deletion_status(status: bool) -> None:
        if status:
            messagebox.showinfo("Success", "Deletion was successful.")
        else:
            messagebox.showinfo("Info", "Deletion was not confirmed.")
        