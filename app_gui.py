import tkinter as tk
from tkinter import ttk

class AudioRecorderGUI:
    def __init__(self, recorder):
        # Initialize the AudioRecorderGUI with an instance of AudioRecorder
        self.recorder = recorder

        # Create the Tkinter root window
        self.root = tk.Tk()
        self.root.title("Audio Recorder")

        # Create a mainframe to hold the widgets
        parent = ttk.Frame(self.root, padding="3 3 12 12")
        parent.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Create a StringVar to display transcribed value later when it is generated
        self.text_var = tk.StringVar()
        self.text_var.set("...")

        # Add widgets here using grid with different row and column values
        self.record_button = ttk.Button(parent, text="Record", command=self.start_recording)
        self.record_button.grid(row=0, column=1)
        self.label = ttk.Label(parent, text='Record audio for 2 sec:').grid(row=0, column=0)
        self.label = ttk.Label(parent, text="Transcribed text:").grid(row=1, column=0)
        self.label = ttk.Label(parent, textvariable=self.text_var).grid(row=1, column=1)

        # Apply padding to all widgets inside the mainframe
        for child in parent.winfo_children():
            child.grid_configure(padx=5, pady=5)

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
            print("Recording finished.")
        else:
            print("Recording was not in progress.")

    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()
