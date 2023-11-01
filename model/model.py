from typing import Protocol
from dotenv import load_dotenv

from model.database_handler import DatabaseInitializer as DBI
from model.text_samples.ts_main import TextSample
from model.audio_recorder_controller import AudioRecorderController as ARC
from model.audio_transcribers import OpenaiTranscriber as OT

class Presenter(Protocol):

    def handle_audio_transcribing(self) -> None:
        ...

class Model:
    def __init__(self) -> None:
        DBI.create_tables()
        self.setup_page_needed = False
        self.phoneme_state = False
        self.load_data_for_new_page()

    def load_data_for_new_page(self) -> None:
        load_dotenv()
        if self.setup_page_needed:
            self.load_setup_page_data()
        else:
            self.load_main_page_data()

    def load_setup_page_data(self):
        # Check api key status
        # Save api key
        # Manage setup_page button state
        # manage setupPpage_needed value
        # manage phoneme_state value
        ...

    def load_main_page_data(self) -> None:
        self.text_sample = TextSample(self.phoneme_state)
        self.audio_recorder_controller = ARC(self.text_sample)

    def get_word_text(self) -> str:
        self.text_sample.load_new_word()
        return self.text_sample.get_sample_text()

    def get_sentence_text(self) -> str:
        self.text_sample.load_new_sentence()
        return self.text_sample.get_sample_text()

    def get_reading_time(self) -> float:
        return self.text_sample.sec_to_read

    def get_setup_page_status(self) -> bool:
        return self.setup_page_needed
    
    def get_avg_rating(self)-> int:
        rating = self.text_sample.avg_rating
        if rating is None:
            return 0
        else:
            return rating
        
    def start_audio_recording(self, presenter:Presenter):
        self.audio_recorder_controller.start_recording(self.text_sample, presenter.handle_audio_transcribing)

    def start_audio_transcribing(self) -> str:
        return OT.transcribe_audio()