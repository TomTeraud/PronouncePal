import tkinter as tk
from tkinter import ttk
from utils.transcribe_audio import transcribe_audio
from database_handler import get_random_sample
from menu_bar import MenuBar

class AudioRecorderGUI:
    def __init__(self, recorder):
        # Initialize the AudioRecorderGUI with an instance of class AudioRecorderController
        self.recorder = recorder

        # Create the Tkinter root window
        self.root = tk.Tk()
        self.root.title("Audio Recorder")

        # Create the menu bar
        menubar = MenuBar(self.root, self)
        self.root['menu'] = menubar

        # Create a mainframe to hold the widgets
        parent = ttk.Frame(self.root, padding="5")
        parent.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Add widgets here using grid with different row and column values
        # Record button.
        self.record_button = ttk.Button(parent, text="Record", command=self.start_recording)
        self.record_button.grid(row=0, column=1)

        # New text sample button
        self.get_new_sample = ttk.Button(parent, text="New text sampe", command=self.next_sampe)
        self.get_new_sample.grid(row=0, column=0)

        self.label = ttk.Label(parent, text='Record audio for 2 sec')
        self.label.grid(row=0, column=1, sticky="E")
        
        # Create text field widgets
        # Widget for text to read
        self.read_text = tk.Text(parent, wrap=tk.WORD)
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
            # Start recording using the AudioRecorder instance
            self.recorder.start_recording()
            # Disable the "Record" button during recording
            self.record_button.config(state=tk.DISABLED)
            # Schedule the stop_recording method to be called after the specified recording duration
            self.root.after(int(self.recorder.recording_duration * 1000), self.stop_recording)

    def stop_recording(self):
        # Check if the recorder is currently recording
        if self.recorder.is_recording():
            # Stop recording using the AudioRecorder instance
            self.recorder.stop_recording()
            # Enable the "Record" button after recording is finished
            self.record_button.config(state=tk.NORMAL)
            # Set the transcribed_text to the transcribed text from the audio file
            self.transcribed_text = transcribe_audio(self.recorder.file_path)
            # Update the text in the Text widget
            self.trans_text.delete("1.0", tk.END)
            self.trans_text.insert(tk.END, self.transcribed_text)

        else:
            print("Recording was not in progress.")

    def next_sampe(self):
        self.read_text.delete("1.0", tk.END)
        self.read_text.insert(tk.END, get_random_sample())


    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()
