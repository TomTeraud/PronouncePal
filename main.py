from audio_recorder import AudioRecorder
from app_gui import AudioRecorderGUI
from config import file_path, recording_duration
import openai
from utils.openai_utils import get_api_key
from callback_functions import transcribe_callback

# Try to get the API key from .env or prompt the user to enter it
openai.api_key = get_api_key()

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
