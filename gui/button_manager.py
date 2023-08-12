import tkinter as tk
from tkinter import ttk
from utils.transcribe_audio import Transcriber  # Import the module containing the transcribe_audio function


class ButtonManager(tk.Frame):
    def __init__(self, parent, text_sample, text_field_instance, recorder):
        super().__init__(parent, borderwidth=10, relief="solid")
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance
        self.recorder = recorder

        self.load_sample_button = LoadSampleButton(self, self, self.text_sample, self.text_field_instance)  # Pass button_manager as well(self)
        self.record_button = RecordButton(self, self.text_sample, self.recorder, self.load_sample_button)  # Pass load_sample_button

        self.load_sample_button.grid(column=0, row=0)
        self.record_button.grid(column=0, row=1)

    def update_button_state_in_manager(self):
        self.load_sample_button.update_button_state()
        self.record_button.update_button_state()

    # Call this method whenever an event that should trigger button updates occurs
    # For example, after loading a new sample
    def handle_event(self):
        self.update_button_state_in_manager()


class LoadSampleButton(ttk.Button):
    def __init__(self, parent, button_manager, text_sample, text_field_instance):
        super().__init__(parent, text="Load new sample", command=self.load_sample)
        self.button_manager = button_manager  # Reference to the ButtonManager instance
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance

        # Update initial state of the button
        self.update_button_state()

    def load_sample(self):
        # Update the text sample and the displayed text in the text field
        self.text_sample.update_sample()
        self.text_field_instance.update_text_sample()

        # Update the button state after updating the sample
        self.update_button_state()

        # Trigger button manager's update from here
        self.button_manager.handle_event()

    def update_button_state(self):
        # Disable the button if sample does not exist
        self.sample_exists = self.text_sample.sample_exists
        if not self.sample_exists:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)


class RecordButton(ttk.Button):
    def __init__(self, parent, text_sample, recorder, load_sample_button):
        super().__init__(parent, text="Start recording", command=self.start_recording)
        self.text_sample = text_sample
        self.recorder = recorder
        self.is_recording = False
        self.is_transcribing = False
        self.load_sample_button = load_sample_button  # Reference to the LoadSampleButton instance
        self.recorder.set_callback(self.start_audio_file_transcription)
        
        # Create an instance of Transcriber
        self.transcriber = Transcriber()
        self.transcriber.set_callback(self.update_button_state)

        self.update_button_state()

    def start_recording(self):
        # Start recording logic here
        self.is_recording = True
        self.update_button_state()
        self.recorder.start_recording()

    def start_audio_file_transcription(self):
        self.is_recording = False
        self.is_transcribing = True
        self.update_button_state()
        self.transcriber.transcribe_audio()
        self.is_transcribing = False
        self.update_button_state()

    def update_button_state(self):
        # Update the button state logic here
        if not self.text_sample.sample_exists or self.is_recording or self.is_transcribing:
            self.config(state=tk.DISABLED)
            if not self.text_sample.sample_exists:
                self.config(text="No sample")    
            elif self.is_recording:
                self.config(text="Recording...")
            else:
                self.config(text="Transcribing...")

        else:
            self.config(text="Start recording", state=tk.NORMAL)
