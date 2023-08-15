from utils.audio_recorder_controler import AudioRecorderController
from utils.transcribe_audio import Transcriber
from db.db_init import create_tables
from utils.text_sample import TextSample
from gui.app_gui import AudioRecorderGUI

def initialize_app():
    """
    Initialize the essential components of the application: database, text sample, and transcriber.
    Returns:
        Tuple: A tuple containing the initialized text sample, audio recorder, and transcriber.
    """
    create_tables()  # Initialize the database and create tables if they don't exist
    text_sample = TextSample()  # Create an instance of TextSample to manage sample text
    transcriber = Transcriber()  # Create an instance of Transcriber to handle audio transcription
    recorder = AudioRecorderController(text_sample)  # Create an instance of AudioRecorderController for recording
    return text_sample, recorder, transcriber

def main():
    # Initialize the application components: text sample, recorder, and transcriber
    text_sample, recorder, transcriber = initialize_app()

    # Create the main GUI window using initialized components
    gui = AudioRecorderGUI(recorder, text_sample, transcriber)

    # Start the application by running the GUI event loop
    gui.mainloop()

if __name__ == "__main__":
    main()
