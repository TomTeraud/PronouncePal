from audio_recorder import AudioRecorder
from app_gui import AudioRecorderGUI
from config import file_path, recording_duration
from callback_functions import transcribe_callback


def main():
    # Create an instance of AudioRecorderGUI without AudioRecorder instance
    gui = AudioRecorderGUI(None)

    # Create an instance of AudioRecorder with the specified file path and recording duration
    recorder = AudioRecorder(file_path, recording_duration, callback=transcribe_callback, gui=gui)

    # Pass the recorder instance to the gui
    gui.recorder = recorder

    # Start the application by running the GUI event loop
    gui.run()

if __name__ == "__main__":
    main()
