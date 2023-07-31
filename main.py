from audio_recorder_controler import AudioRecorderController
from app_gui import AudioRecorderGUI
from config import file_path, recording_duration

def main():
    # Create an instance of AudioRecorder with the specified file path and recording duration
    recorder = AudioRecorderController(file_path, recording_duration)

    # Create an instance of AudioRecorderGUI with the AudioRecorder instance
    gui = AudioRecorderGUI(recorder)

    # Start the application by running the GUI event loop
    gui.run()

if __name__ == "__main__":
    main()
