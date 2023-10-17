import tkinter as tk
from tkinter import ttk, messagebox
from utils.audio_recorder_controller import AudioRecorderController as ARC
from utils.audio_transcribers import OpenaiTranscriber
import openai

class WordSampleButton(ttk.Button):
    def __init__(self, parent):
        super().__init__(parent, text="Load word", command=self.load_sample)
        self.mp_button_controller = parent.mp_button_controller
        self.mp_button_controller.set_word_button(self)
        self.rating_bar = parent.rating_bar
        self.text_sample = parent.parent.text_sample
        self.transcribed_text_field = parent.transcribed_text_field
        self.text_field_instance = parent.sample_text_field
        self.phonemic_text_field = parent.phonemic_text_field
        self.update_button_state()

    def load_sample(self):
        # Load sample text and update button state
        self.text_sample.update_sample()
        new_rating = self.text_sample.avg_rating
        self.rating_bar.update_rating(new_rating)
        self.transcribed_text_field.update_transcribed_text("")
        self.text_field_instance.update_text_sample()
        self.phonemic_text_field.update_sample()
        self.mp_button_controller.update_buttons()

    def update_button_state(self):
        self.sample_exists = self.text_sample.sample_exists
        if not self.sample_exists or self.mp_button_controller.is_recording or self.mp_button_controller.is_transcribing:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class SentenceSampleButton(ttk.Button):
    def __init__(self, parent):
        super().__init__(parent, text="Load sentence", command=self.load_sample)
        self.mp_button_controller = parent.mp_button_controller
        self.mp_button_controller.set_sentence_button(self)
        self.rating_bar = parent.rating_bar
        self.text_sample = parent.parent.text_sample
        self.transcribed_text_field = parent.transcribed_text_field
        self.sample_text_field = parent.sample_text_field
        self.phonemic_text_field = parent.phonemic_text_field
        self.update_button_state()

    def load_sample(self):
        # Load sample text and update button state
        self.text_sample.update_sample(one_word_sample=False)
        new_rating = self.text_sample.avg_rating
        self.rating_bar.update_rating(new_rating)
        self.transcribed_text_field.update_transcribed_text("")
        self.sample_text_field.update_text_sample()
        self.phonemic_text_field.update_sample()
        self.mp_button_controller.update_buttons()

    def update_button_state(self):
        self.sample_exists = self.text_sample.sample_exists
        if not self.sample_exists or self.mp_button_controller.is_recording or self.mp_button_controller.is_transcribing:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class RecordButton(ttk.Button):
    def __init__(self, parent):
        super().__init__(parent, text="Start recording", command=self.start_recording)
        self.progress_bar = parent.progress_bar
        self.rating_bar = parent.rating_bar
        self.mp_button_controller = parent.mp_button_controller
        self.mp_button_controller.set_record_button(self)

        self.text_sample = parent.parent.text_sample
        self.transcribed_text_field = parent.transcribed_text_field

        self.update_button_state()

    def start_recording(self):
        if ARC.check_microphone():
            # Start recording and update button states
            self.mp_button_controller.start_recording()
            self.progress_bar.start_recording_bar_progress()
            ARC.start_recording(self.text_sample, self.start_audio_file_transcription)
        else:
            msg ="No recording davices found!"
            self.error(msg)

    def start_audio_file_transcription(self):
        # Start transcribing audio, update transcribed text, and button states
        self.mp_button_controller.start_transcribing()
        self.mp_button_controller.stop_recording()
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
        self.mp_button_controller.stop_transcribing()

    def error(self, error):
        messagebox.showerror("Error", error)
    
    def update_button_state(self):
        if not self.text_sample.sample_exists or self.mp_button_controller.is_recording or self.mp_button_controller.is_transcribing:
            self.config(state=tk.DISABLED)
            if not self.text_sample.sample_exists:
                self.config(text="No sample")
            elif self.mp_button_controller.is_recording:
                self.config(text="Recording...")
            else:
                self.config(text="Transcribing...")
        else:
            self.config(text=f"Start recording ({self.text_sample.sec_to_read} seconds)", state=tk.NORMAL)