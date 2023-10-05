import tkinter as tk
from tkinter import ttk
from gui.text_fields import SampleTextFrame, TranscribedTextField
from gui.button_manager import ButtonManager, SentenceSampleButton, RecordButton, WordSampleButton
from gui.setup_button_manager import ApiKeySetupButtonOpenAi, SelectOpenAiButton, SelectAlternativeButton, StartMainGuiButton
from gui.menu.menu_bar import MenuBar
from gui.recording_progres_bar import RecordingProgresBar
from gui.rating_bar import RatingBar
from gui.label_fields import MainSetupLabel
from title_page_controler import ButtonState as BS


class AudioRecorderGUI(tk.Tk):
    def __init__(self, text_sample):
        super().__init__()
        self.text_sample = text_sample
        
        self.title("PronouncePal")
        self.geometry("450x200")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.button_colors = {
            "default_bg": "gray90",
            "default_active_bg": "gray95",
            "selected_bg": "#92de85",
            "selected_active_bg": "#a5fa96"
        }
        self.start_main_frame_and_widgets()
        
    def configure_button_style(self, style_name, colors):
        self.style.configure(style_name, background=colors["default_bg"])
        self.style.map(style_name, background=[('active', colors["default_active_bg"]), ('alternate', colors["selected_bg"]), ('active', colors["selected_active_bg"])])
    
    def destroy_all_widgets(self):
        # Get a list of all widgets in the frame
        widgets = self.winfo_children()

        # Loop through the widgets and destroy each one
        for widget in widgets:
            widget.destroy()

    def start_main_frame_and_widgets(self):

        # Configure and apply the button styles using the colors from the dictionary
        self.configure_button_style("Alt.TButton", self.button_colors)
        self.configure_button_style("Openai.TButton", self.button_colors)

        parent = ttk.Frame(self)
        parent.grid(sticky=(tk.N, tk.W, tk.E, tk.S))
        if BS.check_start_state():
            # Create main GUI components
            self.progress_bar = RecordingProgresBar(parent, self.text_sample)
            self.rating_bar = RatingBar(parent, self.text_sample)
            self.sample_text_field = SampleTextFrame(parent, self.text_sample)
            self.transcribed_text_field = TranscribedTextField(parent)
            self.button_manager = ButtonManager()
            self.load_word_sample_button = WordSampleButton(
                parent, self.text_sample, self.transcribed_text_field,
                self.sample_text_field, self.button_manager, self.rating_bar,
            )
            self.load_sample_button = SentenceSampleButton(
                parent, self.text_sample, self.transcribed_text_field, 
                self.sample_text_field, self.button_manager, self.rating_bar,
            )
            self.record_button = RecordButton(
                parent, self.text_sample, self.transcribed_text_field,
                self.button_manager, self.progress_bar, self.rating_bar,
            )
            self.menu_bar = MenuBar(self, self.text_sample, self.sample_text_field, self.button_manager)
            self.config(menu=self.menu_bar)

            # Grid layout for main components
            self.progress_bar.grid(row=2, column=0, sticky="nsew", columnspan=4)
            self.rating_bar.grid(row=0, column=5, sticky="nsew", rowspan=3)
            self.sample_text_field.grid(row=0, column=0, sticky="nsew", columnspan=2)
            self.transcribed_text_field.grid(row=0, column=2, sticky="nsew", columnspan=2)
            self.load_word_sample_button.grid(row=1, column=0, sticky="nsew")
            self.load_sample_button.grid(row=1, column=1, sticky="nsew")
            self.record_button.grid(row=1, column=2, sticky="nsew", columnspan=2)

            # Configure columns and rows
            self.setup_column_configure(parent, 5)
            self.setup_row_configure(parent, 3)
        else:
            # Create menu bar( only ratings and readme)
            self.menu_bar = MenuBar(self)
            self.config(menu=self.menu_bar)

            # Create setup labels
            self.setup_label = MainSetupLabel(parent)
            # Create setup buttons
            self.select_openai = SelectOpenAiButton(parent)
            self.select_alternative = SelectAlternativeButton(parent)
            self.api_key_setup = ApiKeySetupButtonOpenAi(parent)
            self.start_main_gui = StartMainGuiButton(parent, self)
 
            # Set references between instances
            self.select_openai.select_alternative = self.select_alternative
            self.select_openai.start_main_gui = self.start_main_gui
            self.select_alternative.select_openai = self.select_openai
            self.select_alternative.start_main_gui = self.start_main_gui
            self.api_key_setup.select_openai = self.select_openai
 
            # Grid layout
            self.setup_label.grid(row=0, column=0, sticky="nsew", columnspan=2)
            self.select_openai.grid(row=1, column=0, sticky="nsew")
            self.api_key_setup.grid(row=1, column=1, sticky="nsew")
            self.select_alternative.grid(row=2, column=0, sticky="nsew")
            self.start_main_gui.grid(row=3, column=0, sticky="nsew", columnspan=2)

            # Configure columns and rows
            self.setup_column_configure(parent, 2)
            self.setup_row_configure(parent, 3)

        # Add padding to child widgets
        for child in parent.winfo_children():
            child.grid_configure(padx=2, pady=2)

        # Configure grid for the main window
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    # Apply columnconfigure to each column
    def setup_column_configure(self, parent, num_columns):
        for col in range(num_columns):
            parent.columnconfigure(col, weight=1)
        
    # Apply rowconfigure to each row
    def setup_row_configure(self, parent, num_rows):
        for row in range(num_rows):
            parent.rowconfigure(row, weight=1, minsize=30)