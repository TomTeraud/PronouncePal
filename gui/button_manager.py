import tkinter as tk
from tkinter import ttk

class ButtonManager(tk.Frame):
    def __init__(self, parent, text_sample, text_field_instance):
        super().__init__(parent, borderwidth=10, relief="solid")
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance
        self.recording_duration = text_sample.sec_to_read
        self.is_recording = False

        # Create the "Load new sample" button and associate it with the load_sample method
        self.get_sample_button = ttk.Button(self, text="Load new sample", command=self.load_sample)
        self.get_sample_button.grid(column=0, row=0)

        # Create the "Start recording" button and associate it with the toggle_recording method
        self.record_button = ttk.Button(self, text="Start recording for {:.1f} seconds".format(self.recording_duration), command=self.toggle_recording)
        self.record_button.grid(column=1, row=0)

        # Call the update_button_state method initially to set the button state
        self.update_button_state()

    def load_sample(self):
        # Update the text sample and the displayed text in the text field
        self.text_sample.update_sample()
        self.text_field_instance.update_text_sample()

        # Update the recording duration based on the updated sec_to_read
        self.recording_duration = self.text_sample.sec_to_read

        # Update the button text for recording duration
        self.record_button.config(text="Start recording for {:.1f} seconds".format(self.recording_duration))

        # Update the button state after updating the sample
        self.update_button_state()

    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.record_button.config(text="Recording...")
            # Schedule a function to stop recording after the specified duration
            self.after(int(self.recording_duration * 1000), self.stop_recording)
        else:
            self.stop_recording()

        # Update the button state after toggling recording
        self.update_button_state()

    def stop_recording(self):
        self.is_recording = False
        self.record_button.config(text="Start recording for {:.1f} seconds".format(self.recording_duration))
        # Update the button state after stopping recording
        self.update_button_state()

    def update_button_state(self):
        if self.text_sample.sample_exists or self.is_recording:
            self.get_sample_button.config(state=tk.NORMAL if not self.is_recording else tk.DISABLED)
            self.record_button.config(state=tk.DISABLED if self.is_recording else tk.NORMAL)
        else:
            self.get_sample_button.config(state=tk.DISABLED)
            self.record_button.config(state=tk.DISABLED)