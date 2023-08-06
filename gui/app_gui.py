import tkinter as tk
from tkinter import ttk
import threading
from utils.transcribe_audio import transcribe_audio
from db.database_handler import get_random_sample
from gui.menu_bar import MenuBar
from gui.recording_progres_bar import RecordingProgresBar


class AudioRecorderGUI:
    def __init__(self, recorder):
        # Initialize the AudioRecorderGUI with an instance of class AudioRecorderController
        self.recorder = recorder
        
        # Get a random sample and set the recording duration
        self.get_random_sample()
        self.recorder.recording_duration = self.word_count
        
        # Store record duration in milliseconds
        self.mil_sec = int(self.recorder.recording_duration * 1000)
        
        # Create the Tkinter root window
        self.root = tk.Tk()
        self.root.title("Audio Recorder")

        # Create an instance of RecordingProgresBar and pass self.root as the parent widget
        self.recording_progres_bar = RecordingProgresBar(self.root, self.mil_sec)  # Pass self.root as the master

        # Create the menu bar
        menubar = MenuBar(self.root, self)
        self.root['menu'] = menubar

        # Create a mainframe to hold the widgets
        parent = ttk.Frame(self.root, padding="5")
        parent.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Record button.
        self.record_button = ttk.Button(parent, text="Record", command=self.start_recording)
        self.record_button.grid(row=0, column=1)

        # New text sample button
        self.get_new_sample = ttk.Button(parent, text="New text sample", command=self.next_sample)
        self.get_new_sample.grid(row=0, column=0)
        
        # Create text field widgets
        # Widget for text to read
        self.read_text = tk.Text(parent, wrap=tk.WORD)
        self.update_text_widget()
        self.read_text.grid(row=1, column=0, sticky="NSEW")
        
        # Widget for transcribed text
        self.trans_text = tk.Text(parent, wrap=tk.WORD)
        self.trans_text.grid(row=1, column=1, sticky="NSEW")

        # Set the row and column weights to make the Text widget fill the available space
        parent.rowconfigure(1, weight=1)
        parent.columnconfigure(1, weight=1)

        # Apply padding to all widgets inside the mainframe
        for child in parent.winfo_children():
            child.grid_configure(padx=1, pady=1)

    def start_recording(self):
        # Check if the recorder is not already recording
        if not self.recorder.is_recording():
            # Start recording using the AudioRecorderController instance
            self.recorder.start_recording()
            # Disable the "Record" buttons during recording
            self.record_button.config(state=tk.DISABLED, text="Recording")
            self.get_new_sample.config(state=tk.DISABLED, text="Recording")
            # Schedule the stop_recording method to be called after the specified recording duration
            self.root.after(self.mil_sec, self.stop_recording)
            # Start recording bar
            self.recording_progres_bar.start_recording_bar_progress()

    def stop_recording(self):
        # Check if the recorder is currently recording
        if self.recorder.is_recording():
            # Stop recording using the AudioRecorderController instance
            self.recorder.stop_recording()
            # Enable the "Record" button after recording is finished
            self.record_button.config(text="Transcribing")
            self.get_new_sample.config(text="Transcribing")

            # Start transcription in a separate thread
            threading.Thread(target=self.transcribe_audio_and_update_text).start()
        else:
            print("Recording was not in progress.")

    def transcribe_audio_and_update_text(self):
        # Transcribe audio and get the transcribed text
        self.transcribed_text = transcribe_audio(self.recorder.file_path)
        # Update the text in the Text widget
        if self.transcribed_text:
            # Check if the transcribed_text is not empty before inserting into the Text widget
            self.trans_text.delete("1.0", tk.END)
            self.trans_text.insert(tk.END, self.transcribed_text)
        else:
            print("Transcription failed: Empty transcribed_text.")
        
        # Enable the "Record" button after recording and transcribing finished
        self.record_button.config(state=tk.NORMAL, text="Record")
        self.get_new_sample.config(state=tk.NORMAL, text="New text sample")


    def next_sample(self):
        self.sample = self.get_random_sample()
        self.update_recording_duration()
        self.update_progress_bar_duration()
        self.update_text_widget()

    def get_random_sample(self):
        # Get the next random sample
        self.sample = get_random_sample()
        self.words = self.sample.split()
        self.word_count = len(self.words)
        return self.sample

    def update_recording_duration(self):
        # Set recording time calculated from word count
        self.recorder.recording_duration = len(self.words)

    def update_progress_bar_duration(self):
        # Update the progress bar's duration
        self.mil_sec = int(self.recorder.recording_duration * 1000)
        self.recording_progres_bar.set_duration(self.mil_sec)

    def update_text_widget(self):
        if self.sample is None:
            # TO DO!!! Setup placeholder text file.
            self.sample = "First, add text file to the database library. You can do it under the Edit menu bar."
        self.read_text.delete("1.0", tk.END)
        self.read_text.insert(tk.END, self.sample)

    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()
