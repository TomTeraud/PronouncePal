import openai
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
from utils.audio_utils import AudioRecorder
from utils.api_utils import get_api_key

class AudioToTextApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Audio to Text")
        self.api_key = get_api_key()

        self.recording_in_progress = False
        self.audio_file_path = None
        self.audio_recorder = None

        self.create_widgets()

    def create_widgets(self):
        # Create Start Recording button
        self.start_stop_button = tk.Button(self, text="Start Recording", command=self.start_recording)
        self.start_stop_button.pack()

        # Create text area for displaying transcript
        self.transcript_text = tk.Text(self, width=50, height=10)
        self.transcript_text.pack()

    def start_recording(self):
        if not self.recording_in_progress:
            # Start recording
            self.audio_file_path = "temp_audio.wav"  # Adjust the path as needed
            self.audio_recorder = AudioRecorder(self.audio_file_path)
            self.audio_recorder.start_recording()

            # Disable the Start Recording button during recording
            self.start_stop_button.config(text="Recording...", state=tk.DISABLED)

            # Schedule function call to stop the recording and transcribe audio after the specified duration
            self.after(int(self.audio_recorder.recording_duration * 1000), self.stop_and_transcribe)

            self.recording_in_progress = True

    def stop_and_transcribe(self):
        # Stop recording
        self.audio_recorder.stop_recording()
        self.recording_in_progress = False

        # Enable the Start Recording button after recording is stopped
        self.start_stop_button.config(text="Start Recording", state=tk.NORMAL)

        # Transcribe the recorded audio
        self.transcribe_audio()

    def transcribe_audio(self):
        # Rest of the transcribe_audio() function
        if not self.api_key:
            # Display an error message if the API key is not found
            messagebox.showerror("Error", "OpenAI API key not found. Please set the OPENAI_API_KEY in the .env file.")
            return

        if self.audio_file_path is None:
            # Display an error message if the audio file is not found
            messagebox.showerror("Error", "No audio file found.")
            return

        # Set the OpenAI API key
        openai.api_key = self.api_key

        with open(self.audio_file_path, "rb") as audio_file:
            engine_id = "whisper-1"  # Replace with your engine ID
            response = openai.Audio.transcribe(engine_id, audio_file)

        # Extract the transcribed text from the JSON response
        transcript = response["text"]

        # Update the GUI text area with the transcript
        self.transcript_text.delete(1.0, tk.END)  # Clear existing text
        self.transcript_text.insert(tk.END, f"Transcript: {transcript}")

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    app = AudioToTextApp()
    app.mainloop()