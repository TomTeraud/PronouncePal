import tkinter as tk
import openai
from tkinter import ttk, messagebox
from utils.audio_recorder_controller import AudioRecorderController as ARC
from utils.audio_transcribers import OpenaiTranscriber


class WordSampleButton(ttk.Button):
    def __init__(self, parent, g_parent):
        super().__init__(parent, text="Load word", command=self.load_sample)
        self.g_parent = g_parent
        self.parent = parent
        self.mpbc = parent.mpb_controller
        self.mpbc.set_button("word", self)
        self.rating_bar = parent.rating_bar
        self.text_sample = parent.parent.text_sample
        self.transcribed_text_field = parent.transcribed_text_field
        self.sample_text_field = parent.sample_text_field
        self.update_button_state()

    def load_sample(self):
        # Load sample text and update button state
        self.text_sample.update_sample()
        self.rating_bar.update_rating(self.text_sample.avg_rating)
        self.transcribed_text_field.update_transcribed_text("")
        self.sample_text_field.update_text_sample()
        self.mpbc.update_buttons()
        if self.g_parent.tp_phoneme_cb_state:
            self.parent.phonemic_text_field.update_sample()
    
    def update_button_state(self):
        if self.mpbc.is_recording or self.mpbc.is_transcribing or self.text_sample.sample_exists == False:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class SentenceSampleButton(ttk.Button):
    def __init__(self, parent, g_parent):
        super().__init__(parent, text="Load sentence", command=self.load_sample)
        self.g_parent = g_parent
        self.parent = parent
        self.mpbc = parent.mpb_controller
        self.mpbc.set_button("sentence", self)
        self.rating_bar = parent.rating_bar
        self.text_sample = parent.parent.text_sample
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
        self.mpbc.update_buttons()
        if self.g_parent.tp_phoneme_cb_state:
            self.parent.phonemic_text_field.update_sample()

    def update_button_state(self):
        if self.mpbc.is_recording or self.mpbc.is_transcribing or self.text_sample.sample_exists == False:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

class RecordButton(ttk.Button):
    def __init__(self, parent):
        super().__init__(parent, text="Start recording", command=self.start_recording)
        self.progress_bar = parent.progress_bar
        self.rating_bar = parent.rating_bar
        self.mpbc = parent.mpb_controller
        self.mpbc.set_button("record", self)

        self.text_sample = parent.parent.text_sample
        self.transcribed_text_field = parent.transcribed_text_field

        self.update_button_state()

    def start_recording(self):
        if ARC.check_microphone():
            # Start recording and update button states
            self.mpbc.set_recording_status(True)
            self.progress_bar.start_recording_bar_progress()
            ARC.start_recording(self.text_sample, self.start_audio_file_transcription)
        else:
            msg ="No recording davices found!"
            self.error(msg)

    def start_audio_file_transcription(self):
        # Start transcribing audio, update transcribed text, and button states
        self.mpbc.set_transcribing_status(True)
        self.mpbc.set_recording_status(False)
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
        self.mpbc.set_transcribing_status(False)

    def error(self, error):
        messagebox.showerror("Error", error)
    
    def update_button_state(self):
        if self.mpbc.is_recording or self.mpbc.is_transcribing or self.text_sample.sample_exists == False:
            self.config(state=tk.DISABLED)
            if self.mpbc.is_recording:
                self.config(text="Recording...")
            elif self.mpbc.is_transcribing:
                self.config(text="Transcribing...")            
            else:
                self.config(text="No text sample")            
        else:
            self.config(text=f"Start recording ({self.text_sample.sec_to_read} seconds)", state=tk.NORMAL)