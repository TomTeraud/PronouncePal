from typing import Protocol
from model.api_key_handler import OpenaiApiKeyHandler as OAKH

from model.helpers import resource_path
from model.database_handler import DatabaseInitializer as DBI, SentenceWordHandler as SWH
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


    def setup_action(self):
        # Business logic for setup action goes here
        print("Setup action in Model")

    def main_action(self):
        # Business logic for main action goes here
        print("Main action in Model")

    def load_data_for_new_page(self) -> None:
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
    
    def get_readme_text_for_menubar(self) -> str:
        readme_path = resource_path("README.md")
        # Read the contents of the readme.md file with UTF-8 encoding
        with open(readme_path, 'r', encoding='utf-8') as file:
            return file.read()

    def get_single_word_ratings(self) -> list[tuple]:
        return SWH.fetch_words_from_database()
    
    def get_sentence_ratings(self) -> list[tuple]:
        return SWH.fetch_sentences_from_database()
    
    def handle_sample_upload_with_given_path(self, path: str) -> bool:
        if SWH.populate_sentences_table(path) and SWH.populate_words_table():
            return True 
        else:
            return False

    def handle_personal_data_deletion(self) -> bool:
        return SWH.delete_all_rows()
    
    def store_valid_key(self, key) -> bool:
        return OAKH.write_key_in_env_file(key)
    
    def validate_openai_api_key(self, key: str) -> bool:
        return OAKH.validate_key(key)
    
    def check_key_status_in_os(self) -> bool:
        return OAKH.openai_api_key_status()