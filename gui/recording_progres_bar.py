import tkinter as tk
from tkinter import ttk

class RecordingProgresBar(ttk.Progressbar):
    _STEP_PER_SECOND = 30
    _MAX_PROGRESS = 100

    def __init__(self, parent, text_sample):
        """
        Initialize the RecordingProgresBar.

        Args:
            parent (tk.Widget): The parent widget.
            text_sample (TextSample): The text sample object.
        """
        self.parent = parent
        self.text_sample = text_sample

        self._progress_var = tk.DoubleVar()
        self._progress_var.set(0)

        self._running = False
        self._update_rate = int(1000 / self._STEP_PER_SECOND)

        super().__init__(self.parent, mode="determinate", maximum=self._MAX_PROGRESS)
        self.configure(variable=self._progress_var)

    def set_duration(self):
        """
        Set the duration of the progress bar based on text_sample.
        """
        self.duration = self.text_sample.mill_sec_to_read
        self._step = self._MAX_PROGRESS / (self.duration / self._update_rate)

    def _update_progress(self):
        """
        Update the progress bar value and schedule the next update.
        """
        if self._running:
            current_value = self._progress_var.get()
            if current_value < self._MAX_PROGRESS:
                self._progress_var.set(current_value + self._step)
                self.parent.after(self._update_rate, self._update_progress)
            else:
                self._reset()

    def start_recording_bar_progress(self):
        """
        Start the recording progress.
        """
        if not self._running:
            self.set_duration()
            self._running = True
            self._update_progress()

    def _reset(self):
        """
        Reset the progress bar to 0 and stop the progress update process.
        """
        self._progress_var.set(0)
        self._running = False

    def reset(self):
        """
        Public method to reset the progress bar.
        """
        self._reset()
