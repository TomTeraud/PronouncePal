from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
from utils.audio_recorder import AudioRecorder
from utils.transcribe_audio import transcribe_audio
from gui import ContentFrame

class AudioToTextApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Audio to Text")

        self.recording_in_progress = False
        self.audio_file_path = "temp_audio.wav"  # Adjust the path as needed
        self.audio_recorder = AudioRecorder(self.audio_file_path)

        self.create_widgets()

    def create_widgets(self):
        # Create ContentFrame to hold the GUI elements
        self.content_frame = ContentFrame(self, self.start_recording)
        self.content_frame.grid(row=0, column=0, padx=10, pady=10)

    def start_recording(self):
        if not self.recording_in_progress:
            # Start recording
            self.audio_recorder.start_recording()

            # Disable the Start Recording button during recording
            self.content_frame.start_stop_button.config(text="Recording...", state=tk.DISABLED)

            # Schedule function call to stop the recording and transcribe audio after the specified duration
            self.after(int(self.audio_recorder.recording_duration * 1000), self.stop_and_transcribe)

            self.recording_in_progress = True

    def stop_and_transcribe(self):
        # Stop recording
        self.audio_recorder.stop_recording()
        self.recording_in_progress = False

        # Enable the Start Recording button after recording is stopped
        self.content_frame.start_stop_button.config(text="Start Recording", state=tk.NORMAL)

        # Transcribe the recorded audio
        transcript = transcribe_audio(self.audio_file_path)

        # Update the GUI text area with the transcript
        if transcript:
            self.content_frame.update_transcript(transcript)

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    app = AudioToTextApp()
    app.mainloop()
