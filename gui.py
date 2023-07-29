import tkinter as tk
from tkinter import ttk

class StartStopButton(ttk.Button):
    def __init__(self, parent, start_recording_func):
        super().__init__(parent, text="Start Recording", command=start_recording_func)

class TranscriptTextArea(tk.Text):
    def __init__(self, parent):
        super().__init__(parent, width=50, height=10)

    def update_transcript(self, transcript):
        self.delete(1.0, tk.END)  # Clear existing text
        self.insert(tk.END, f"Transcript: {transcript}")

class ContentFrame(ttk.Frame):
    def __init__(self, parent, start_recording_func):
        super().__init__(parent)

        # Create Start Recording button
        self.start_stop_button = StartStopButton(self, start_recording_func)
        self.start_stop_button.grid(row=1, column=1)

        # Create text area for displaying transcript
        self.transcript_text = TranscriptTextArea(self)
        self.transcript_text.grid(row=1, column=2)

    def update_transcript(self, transcript):
        self.transcript_text.update_transcript(transcript)
