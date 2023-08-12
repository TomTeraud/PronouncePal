import tkinter as tk
from tkinter import ttk
from utils.transcribe_audio import transcribe_audio  # Import the module containing the transcribe_audio function


class ButtonManager(tk.Frame):
    def __init__(self, parent, text_sample, text_field_instance, recorder):
        super().__init__(parent, borderwidth=10, relief="solid")
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance
        self.recorder = recorder

        self.load_sample_button = LoadSampleButton(self, self, self.text_sample, self.text_field_instance)  # Pass button_manager as well
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
        super().__init__(parent, text="Start recording", command=self.toggle_recording)
        self.text_sample = text_sample
        self.recorder = recorder
        self.is_recording = False
        self.load_sample_button = load_sample_button  # Reference to the LoadSampleButton instance

        self.update_button_state()

    def toggle_recording(self):
        # Toggle recording logic here
        ...

    def update_button_state(self):
        self.sample_exists = self.text_sample.sample_exists

        # Disable the button if sample does not exist
        print("Trigger this, if new sample loaded!!!!!!!!!!!!!!!!!!!!")
        if not self.load_sample_button.sample_exists:
            self.config(state=tk.DISABLED)
        else:
            self.config(state=tk.NORMAL)

        if self.sample_exists:
            self.recording_duration = self.text_sample.sec_to_read
            self.config(text="Start recording for {:.1f} seconds".format(self.recording_duration))
        else:
            self.config(text="Sample unavailable")
