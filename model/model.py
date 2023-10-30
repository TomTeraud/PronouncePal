from model.database_handler import DatabaseInitializer as DBI, SentenceWordHandler as SWH
from model.text_samples.ts_main import TextSample
class Model:
    def __init__(self) -> None:
        DBI.create_tables()
        self.setup_page_needed = False
        self.phoneme_state = False
        self.load_data_for_new_page()

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

    def get_word_text(self) -> str:
        sample = self.text_sample.get_single_word()
        print(sample)
        return sample

    def get_sentence_text(self) -> str:
        sample = self.text_sample.get_sentence()
        print(sample)
        return sample

    def get_setup_page_status(self) -> bool:
        return self.setup_page_needed