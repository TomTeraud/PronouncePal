from tkinter import filedialog, messagebox, simpledialog
from database_handler import DatabaseHandler as DH
from title_page_controler import ButtonState as BS

class FileMenuHandler:
    @classmethod
    def handle_text_file_upload_with_args(cls, text_sample, text_field_instance, button_manager):
        if cls.select_file():
            cls.update_gui(text_sample, text_field_instance, button_manager)

    @classmethod
    def handle_text_samples_delete_with_args(cls, text_sample, text_field_instance, button_manager):
        result = cls.delete_samples_from_db()
        if result:
            cls.update_gui(text_sample, text_field_instance, button_manager)
    
    @staticmethod
    def handle_change_transcriber(arg):
        BS.ready_to_start = False
        arg.destroy_all_widgets()
        arg.start_main_frame_and_widgets()

    @classmethod
    def select_file(cls):
        file_types = [("Text Files", "*.txt")]
        selected_file_path = filedialog.askopenfilename(filetypes=file_types)

        if selected_file_path:
            DH.populate_sentences_table_from_text_file(selected_file_path)
            DH.populate_words_table_from_sentences_table()
            messagebox.showinfo("Success", "Text file uploaded successfully!")
            return True  # Return True to indicate success
        else:
            return False  # Return False to indicate failure

    @classmethod
    def delete_samples_from_db(cls):
        confirmation_text = "DELETE"  # Confirmation text required from the user
        user_input = simpledialog.askstring("Confirm Deletion", "Type 'DELETE' to confirm deletion:")
        if user_input == confirmation_text:
            DH.delete_all_rows()
            return True  # Return True to indicate success
        else:
            messagebox.showinfo("Info", "Deletion was not confirmed.")
            return False
    
    @classmethod
    def update_gui(cls, text_sample, text_field_instance, button_manager):
        print("gui updated")
        text_sample.update_sample()
        text_field_instance.update_text_sample()
        button_manager.update_buttons()