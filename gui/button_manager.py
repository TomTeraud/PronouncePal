import tkinter as tk
from tkinter import ttk, messagebox
from utils.audio_recorder_controler import AudioRecorderController as ARC
from utils.transcribe_audio import Transcriber
from utils.api_handler import ApiHandler as ah
from app_setup import SetupManager as sm
import openai
import os


class ButtonManager:
    def __init__(self):
        self.load_sample_button = None
        self.load_word_sample_button = None
        self.record_button = None
        self.is_recording = False
        self.is_transcribing = False
        self.is_api_key_set = self.check_api_key_set()

    def set_load_sample_button(self, load_sample_button):
        self.load_sample_button = load_sample_button

    def set_load_word_sample_button(self, load_word_sample_button):
        self.load_word_sample_button = load_word_sample_button

    def set_record_button(self, record_button):
        self.record_button = record_button

    def start_recording(self):
        self.is_recording = True
        self.update_buttons()

    def stop_recording(self):
        self.is_recording = False
        self.update_buttons()

    def start_transcribing(self):
        self.is_transcribing = True
        self.update_buttons()

    def stop_transcribing(self):
        self.is_transcribing = False
        self.update_buttons()

    def set_api_key_status(self, is_set):
        self.is_api_key_set = is_set
        self.update_buttons()

    def check_api_key_set(self):
        api_key = os.environ.get("OPENAI_API_KEY")
        return api_key is not None

    def update_buttons(self):
        # Update button states based on recording, transcribing, and API key status
        if self.load_sample_button:
            self.load_sample_button.update_button_state()
        if self.load_word_sample_button:
            self.load_word_sample_button.update_button_state()
        if self.record_button:
            self.record_button.update_button_state()

class WordSampleButton(ttk.Button):
    def __init__(self, parent, text_sample, transcribed_text_field, text_field_instance, button_manager, rating_bar):
        super().__init__(parent, text="Load word", command=self.load_sample)
        self.button_manager = button_manager
        self.button_manager.set_load_word_sample_button(self)
        self.rating_bar = rating_bar
        self.text_sample = text_sample
        self.transcribed_text_field = transcribed_text_field
        self.text_field_instance = text_field_instance
        self.update_button_state()

    def load_sample(self):
        # Load sample text and update button state
        self.text_sample.update_sample()
        new_rating = self.text_sample.avg_rating
        self.rating_bar.update_rating(new_rating)
        self.transcribed_text_field.update_transcribed_text("")
        self.text_field_instance.update_text_sample()
        self.button_manager.update_buttons()

    def update_button_state(self):
        # Disable the button if no sample, recording, or API key is not set
        self.sample_exists = self.text_sample.sample_exists
        if not self.sample_exists or self.button_manager.is_recording or self.button_manager.is_transcribing or not self.button_manager.is_api_key_set:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class SentenceSampleButton(ttk.Button):
    def __init__(self, parent, text_sample, transcribed_text_field, text_field_instance, button_manager, rating_bar):
        super().__init__(parent, text="Load sentence", command=self.load_sample)
        self.button_manager = button_manager
        self.button_manager.set_load_sample_button(self)
        self.rating_bar = rating_bar
        self.text_sample = text_sample
        self.transcribed_text_field = transcribed_text_field
        self.text_field_instance = text_field_instance
        self.update_button_state()

    def load_sample(self):
        # Load sample text and update button state
        self.text_sample.update_sample(one_word_sample=False)
        new_rating = self.text_sample.avg_rating
        self.rating_bar.update_rating(new_rating)
        self.transcribed_text_field.update_transcribed_text("")
        self.text_field_instance.update_text_sample()
        self.button_manager.update_buttons()

    def update_button_state(self):
        # Disable the button if no sample, recording, or API key is not set
        self.sample_exists = self.text_sample.sample_exists
        if not self.sample_exists or self.button_manager.is_recording or self.button_manager.is_transcribing or not self.button_manager.is_api_key_set:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class RecordButton(ttk.Button):
    def __init__(self, parent, text_sample, transcribed_text_field, button_manager, progress_bar, rating_bar):
        super().__init__(parent, text="Start recording", command=self.start_recording)
        self.progress_bar = progress_bar
        self.rating_bar =rating_bar
        self.button_manager = button_manager
        self.button_manager.set_record_button(self)

        self.text_sample = text_sample
        self.transcribed_text_field = transcribed_text_field

        self.update_button_state()

    def start_recording(self):
        if ARC.check_microphone():
            # Start recording and update button states
            self.button_manager.start_recording()
            self.progress_bar.start_recording_bar_progress()
            ARC.start_recording(self.text_sample, self.start_audio_file_transcription)
        else:
            msg ="No recording davices found!"
            self.error(msg)

    def start_audio_file_transcription(self):
        # Start transcribing audio, update transcribed text, and button states
        self.button_manager.start_transcribing()
        self.button_manager.stop_recording()
        result = Transcriber.transcribe_audio()
        if isinstance(result, openai.error.RateLimitError):
            # Handle rate limit error
            msg = "Rate limit exceeded"
            self.transcribed_text_field.update_transcribed_text(msg)
            self.error(msg)

        elif isinstance(result, openai.error.OpenAIError):
            # Handle other OpenAI errors
            msg = "An OpenAI error occurred"
            self.transcribed_text_field.update_transcribed_text(msg)
            self.error(msg)
        else:
            # Process the transcribed text
            self.transcribed_text_field.update_transcribed_text(result)
            # Calculate rating from sample text and transcribed text
            self.text_sample.calculate_similarity(result)
            self.text_sample.add_rating_to_db()
            # Update rating bar
            self.rating_bar.update_rating(self.text_sample.avg_rating)
        self.button_manager.stop_transcribing()

    def error(self, error):
        messagebox.showerror("Error", error)
    
    def update_button_state(self):
        # Update button state based on sample, recording, transcribing, and API key status
        if not self.text_sample.sample_exists or self.button_manager.is_recording or self.button_manager.is_transcribing or not self.button_manager.is_api_key_set:
            self.config(state=tk.DISABLED)
            if not self.text_sample.sample_exists:
                self.config(text="No sample")
            elif self.button_manager.is_recording:
                self.config(text="Recording...")
            elif self.button_manager.is_transcribing:
                self.config(text="Transcribing...")
            else:
                self.config(text="setup API key first")
        else:
            self.config(text=f"Start recording ({self.text_sample.sec_to_read} seconds)", state=tk.NORMAL)

class ApiKeySetupButtonOpenAi(ttk.Button):  
    def __init__(self, parent, argi):
        super().__init__(parent, text="Add API key", command=self.manage_api_key)
        self.argi = argi
    
    def manage_api_key(self):
        if ah.ask_for_openai_key():
            # Call setup_gui_widgets to reload the GUI
            self.argi.destroy_all_widgets()
            self.argi.start_main_frame_and_widgets()

class SelectOpenAiButton(ttk.Button):  
    def __init__(self, parent, argi):
        super().__init__(parent, text="OpenAI", command=self.select_open_ai)
        self.argi = argi

        if sm.openai_key_set and sm.alternative_api_selected is False:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)

        style = ttk.Style()
        if sm.openai_api_selected:
            style.configure("OpenAi.TButton", background="green")
        else:
            style.configure("OpenAi.TButton", background="gray90")
        self.config(style="OpenAi.TButton")        
    
    def select_open_ai(self):
        sm.toggle_openai_api_selected()
        self.argi.destroy_all_widgets()
        self.argi.start_main_frame_and_widgets()


class SelectAlternativeButton(ttk.Button):  
    def __init__(self, parent, argi):
        super().__init__(parent, text="Alternative (in developement)", command=self.select_alternative)
        self.argi = argi

        if sm.alternative_api_set and sm.openai_api_selected is False:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)

        style = ttk.Style()
        if sm.alternative_api_selected:
            style.configure("Alternative.TButton", background="green")
        else:
            style.configure("Alternative.TButton", background="gray90")
        self.config(style="Alternative.TButton")        
    
    def select_alternative(self):
        sm.toggle_alternative_selected()
        self.argi.destroy_all_widgets()
        self.argi.start_main_frame_and_widgets()



class StartMainGuiButton(ttk.Button):  
    def __init__(self, parent, argi):
        super().__init__(parent, text="Start!", command=self.start_main_gui)
        self.argi = argi
        if sm.openai_api_selected or sm.alternative_api_selected:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)
    
    def start_main_gui(self):
        if sm.openai_api_selected:
            sm.transcriber_selected = True
        else:
            messagebox.showinfo("Info", "An alternative transcriber is under development")
        self.argi.destroy_all_widgets()
        self.argi.start_main_frame_and_widgets()