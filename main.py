from utils.audio_recorder_controler import AudioRecorderController
from utils.transcribe_audio import Transcriber
from db.db_init import create_tables
from utils.text_sample import TextSample
from gui.app_gui import AudioRecorderGUI




def main():
    # Initialize the database and create tables if they don't exist
    create_tables()

    # Create text sample object
    text_sample = TextSample()

    transcriber = Transcriber()

    # Create an instance of AudioRecorder with the specified file path, recording duration, and text_sample
    recorder = AudioRecorderController(text_sample)

    # Create an instance of AudioRecorderGUI with the AudioRecorder instance and text_sample
    gui = AudioRecorderGUI(recorder, text_sample, transcriber)

    # Start the application by running the GUI event loop
    gui.mainloop()

if __name__ == "__main__":
    main()
