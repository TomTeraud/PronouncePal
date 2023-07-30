from audio_recorder import AudioRecorder
from app_gui import AudioRecorderGUI
from config import file_path, recording_duration

if __name__ == "__main__":

    # Create an instance of AudioRecorder with the specified file path and recording duration
    recorder = AudioRecorder(file_path, recording_duration)

    # Create an instance of AudioRecorderGUI with the AudioRecorder instance
    gui = AudioRecorderGUI(recorder)

    # Start the application by running the GUI event loop
    gui.run()

