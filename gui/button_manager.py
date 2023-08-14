import tkinter as tk
from tkinter import ttk
from utils.transcribe_audio import Transcriber  # Import the module containing the transcribe_audio function


class ButtonManager():
    def __init__(self):
        self.load_sample_button = None
        self.record_button = None
        self.is_recording = False
        self.is_transcribing = False

    def set_load_sample_button(self, load_sample_button):
        self.load_sample_button = load_sample_button

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

    def update_buttons(self):
        if self.load_sample_button:
            self.load_sample_button.update_button_state()
        if self.record_button:
            self.record_button.update_button_state()




class LoadSampleButton(ttk.Button):
    def __init__(self, parent, text_sample, text_field_instance, row, column, button_manager):
        super().__init__(parent, text="Load sample text", command=self.load_sample)
        self.button_manager = button_manager
        self.button_manager.set_load_sample_button(self)

        self.text_sample = text_sample
        self.text_field_instance = text_field_instance

        self.grid(row=row, column=column, sticky="nsew")

        self.update_button_state()

    def load_sample(self):
        # Update the text sample and the displayed text in the text field
        self.text_sample.update_sample()
        self.text_field_instance.update_text_sample()

        # Update the button state after updating the sample
        self.button_manager.update_buttons()

    def update_button_state(self):
        # Disable the button if sample does not exist or if recording is ongoing
        self.sample_exists = self.text_sample.sample_exists
        if not self.sample_exists  or self.button_manager.is_recording:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)


class RecordButton(ttk.Button):
    def __init__(self, parent, text_sample, transcriber, recorder, load_sample_button, transcribed_text_field, row, column, button_manager):
        super().__init__(parent, text="Start recording", command=self.start_recording)
        self.button_manager = button_manager
        self.button_manager.set_record_button(self)
        self.transcriber = transcriber
        self.grid(row=row, column=column, sticky="nsew")

        self.text_sample = text_sample
        self.recorder = recorder
        self.load_sample_button = load_sample_button  # Reference to the LoadSampleButton instance
        self.transcribed_text_field = transcribed_text_field
        self.recorder.set_callback(self.start_audio_file_transcription)

        # Create an instance of Transcriber
        # self.transcriber = Transcriber()
        self.transcriber.set_callback(self.update_button_state)

        self.update_button_state()

    def start_recording(self):
        # Start recording logic here
        self.button_manager.start_recording()
        self.recorder.start_recording()


    def start_audio_file_transcription(self):
        self.button_manager.start_transcribing()
        self.button_manager.stop_recording()
        self.transcriber.transcribe_audio()
        self.transcribed_text_field.update_transcribed_text()
        self.button_manager.stop_transcribing()

    def update_button_state(self):
        # Update the button state logic here
        if not self.text_sample.sample_exists or self.button_manager.is_recording or self.button_manager.is_transcribing:
            self.config(state=tk.DISABLED)
            if not self.text_sample.sample_exists:
                self.config(text="No sample")
            elif self.button_manager.is_recording:
                self.config(text="Recording...")
            else:
                self.config(text="Transcribing...")
        else:
            self.config(text="Start recording", state=tk.NORMAL)