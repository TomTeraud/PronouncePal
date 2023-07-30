from utils.transcribe_audio import transcribe_audio

def transcribe_callback(gui):
    transcript = transcribe_audio(gui.recorder.file_path)  # Use gui.recorder.file_path to access the file path
    if transcript is not None:
        gui.text_var.set(transcript)  # Update the GUI label with the transcribed text
        print("Transcription:", transcript)
    else:
        print("Transcription failed.")
