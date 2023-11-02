import tkinter as tk
from tkinter import ttk
import time

class RecordingProgresBar(ttk.Progressbar):
    _TICKS_PER_SECOUND = 30
    _MAX_PROGRESS = 60.0

    def __init__(self, parent_frame):
        self._progress_var = tk.DoubleVar()
        super().__init__(parent_frame, mode="determinate", maximum=self._MAX_PROGRESS)

        self.parent_frame = parent_frame
        self._progress_var.set(0)
        self.time_delay_ms = 1000 // self._TICKS_PER_SECOUND
        self._running = False

        self.configure(variable=self._progress_var)

    def start_recording_bar_progress(self, duration: float) -> None:
        if not self._running:
            self.duration = duration
            self.start_time = time.time()
            self._running = True
            self._update_progress()


    def _update_progress(self):
        """
        Update the progress bar value and schedule the next update.
        """
        if self._running:
            elapsed_time = time.time() - self.start_time
            if elapsed_time < self.duration:
                progress = (elapsed_time / self.duration) * self._MAX_PROGRESS
                self._progress_var.set(progress)
                self.parent_frame.after(self.time_delay_ms, self._update_progress)
            else:
                self._reset()

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
