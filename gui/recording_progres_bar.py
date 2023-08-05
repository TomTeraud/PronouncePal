import tkinter as tk
from tkinter import ttk

class RecordingProgresBar:
    def __init__(self, master, duration):
        # Save the reference to the master (parent) widget
        self.master = master
        # Save duration in seconds
        self.duration = duration
        # Create a DoubleVar to control the progress bar value
        self._progress_var = tk.DoubleVar()
        self._progress_var.set(0)

        # Set up variables for managing the progress update process
        self._running = False
        self._steps_per_second = 30
        self._max = 100  # Set max to 100 for percentage-based progress
        self._update_rate = int(1000 / self._steps_per_second)
        self._step = self._max / (self.duration / self._update_rate)
        
        # Create the progress bar widget and associate it with the progress_var
        self._progress_bar = ttk.Progressbar(self.master, variable=self._progress_var, maximum=self._max)
        self._progress_bar.grid(row=2, column=0, sticky="NSEW")

    def start_recording_bar_progress(self):
        # Start the progress update process if it's not already running
        if not self._running:
            self._running = True
            self._update_recording_bar_progress()

    def _update_recording_bar_progress(self):
        # Update the progress bar value and schedule the next update
        if self._running:
            current_value = self._progress_var.get()
            if current_value < self._max:
                self._progress_var.set(current_value + self._step)
                # Continue updating progress until it reaches the maximum
                self.master.after(self._update_rate, self._update_recording_bar_progress)
            else:
                # Progress reaches the maximum, stop the progress update process
                self._reset()

    def _reset(self):
        # Reset the progress bar to 0 and stop the progress update process
        self._progress_var.set(0)
        self._running = False

    def reset(self):
        # Public method to reset the progress bar
        self._reset()
