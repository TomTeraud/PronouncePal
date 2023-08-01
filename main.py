from audio_recorder_controler import AudioRecorderController
from app_gui import AudioRecorderGUI
from config import file_path, recording_duration
from db_init import create_tables
from database_handler import create_sample_from_text_file

def main():

    # Initialize the database and create tables if they don't exist
    create_tables()

    # # Populate the 'text_samples' table from the text file
    # create_sample_from_text_file()

    # Create an instance of AudioRecorder with the specified file path and recording duration
    recorder = AudioRecorderController(file_path, recording_duration)

    # Create an instance of AudioRecorderGUI with the AudioRecorder instance
    gui = AudioRecorderGUI(recorder)

    # Start the application by running the GUI event loop
    gui.run()

if __name__ == "__main__":
    main()
