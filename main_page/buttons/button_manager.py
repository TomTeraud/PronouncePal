import tkinter as tk
from tkinter import ttk, messagebox
from utils.audio_recorder_controller import AudioRecorderController as ARC
from utils.audio_transcribers import OpenaiTranscriber
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
    def __init__(self, parent, grand_parent):
        super().__init__(parent, text="Load word", command=self.load_sample)
        self.button_manager = parent.button_manager
        self.button_manager.set_load_word_sample_button(self)
        self.rating_bar = parent.rating_bar
        self.text_sample = grand_parent.text_sample
        self.transcribed_text_field = parent.transcribed_text_field
        self.text_field_instance = parent.sample_text_field
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
    def __init__(self, parent, grand_parent):
        super().__init__(parent, text="Load sentence", command=self.load_sample)
        self.button_manager = parent.button_manager
        self.button_manager.set_load_sample_button(self)
        self.rating_bar = parent.rating_bar
        self.text_sample = grand_parent.text_sample
        self.transcribed_text_field = parent.transcribed_text_field
        self.sample_text_field = parent.sample_text_field
        self.update_button_state()

    def load_sample(self):
        # Load sample text and update button state
        self.text_sample.update_sample(one_word_sample=False)
        new_rating = self.text_sample.avg_rating
        self.rating_bar.update_rating(new_rating)
        self.transcribed_text_field.update_transcribed_text("")
        self.sample_text_field.update_text_sample()
        self.button_manager.update_buttons()

    def update_button_state(self):
        # Disable the button if no sample, recording, or API key is not set
        self.sample_exists = self.text_sample.sample_exists
        if not self.sample_exists or self.button_manager.is_recording or self.button_manager.is_transcribing or not self.button_manager.is_api_key_set:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class RecordButton(ttk.Button):
    def __init__(self, parent, grand_parent):
        super().__init__(parent, text="Start recording", command=self.start_recording)
        self.progress_bar = parent.progress_bar
        self.rating_bar =parent.rating_bar
        self.button_manager = parent.button_manager
        self.button_manager.set_record_button(self)

        self.text_sample = grand_parent.text_sample
        self.transcribed_text_field = parent.transcribed_text_field

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
        result = OpenaiTranscriber.transcribe_audio()
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