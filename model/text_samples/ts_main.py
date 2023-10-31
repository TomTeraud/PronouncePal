from difflib import SequenceMatcher
from model.config import CHARS_PER_MINUTE, MIN_DURATION

from model.database_handler import SentenceWordHandler as SWH
from model.text_samples.phoneme import Phoneme


class TextSample:
    def __init__(self, phoneme_state):
        self.phonome_state = phoneme_state
        self.sample_exists = False
        self.sample = None
        self.sample_id = None
        self.avg_rating = None
        self.rating = None
        self.char_count = None
        self.one_word_type = True
        self.sec_to_read = None
        self.get_single_word()


    def get_single_word(self) -> str:
        new_sample_text, new_sample_id = SWH.get_random_word()
        if new_sample_text:
            self.sample_exists = True
            self.one_word_type = True
            self.sample = new_sample_text
            self.sample_id = new_sample_id
            self.avg_rating = SWH.get_avg_word_rating(new_sample_id)
        else:
            print("Failed to obtain sample from get_random_word()")
        self.manage_sample_parameters()
        self.manage_phoname()
        return self.sample

    def get_sentence(self) -> str:
        new_sample_text, new_sample_id = SWH.get_random_sentence()
        if new_sample_text:
            self.sample_exists = True
            self.one_word_type = False
            self.sample = new_sample_text
            self.sample_id = new_sample_id
            self.avg_rating = SWH.get_avg_sentence_rating(new_sample_id)
        else:
            print("Failed to obtain sample from get_random_word()")
        self.manage_sample_parameters()
        self.manage_phoname()
        return self.sample
    
    def manage_phoname(self) -> None:
        if self.phonome_state:
            if self.one_word_type:
                self.phoneme = Phoneme.get_phonemes(self.sample)
            else:
                self.phoneme = ""
    
    def manage_sample_parameters(self) -> None:
        self.update_char_count()
        self.calculate_duration()
        
    def update_char_count(self) -> None:
        if self.sample is None:
            self.char_count = None
        else:
            self.char_count = len(self.sample)

    def calculate_duration(self) -> None:
        if self.char_count is not None:
            # Calculate the duration to read the sample text based on the character count
            self.sec_to_read = self.char_count / (CHARS_PER_MINUTE / 60)
            self.sec_to_read = self.sec_to_read + MIN_DURATION
            self.mill_sec_to_read = int(self.sec_to_read * 1000)

    def preprocess_string(self, text: str) -> str:
        # Preprocess a string by converting it to lowercase and removing trailing dots and commas
        return text.lower().rstrip('.,')

    def calculate_similarity(self, string2: str) -> None:
        string1_lower = self.preprocess_string(self.sample)
        string2_lower = self.preprocess_string(string2)
        # Calculate the similarity ratio between two strings
        similarity_ratio = SequenceMatcher(None, string1_lower, string2_lower).ratio()
        self.rating = round(similarity_ratio * 100)

    def add_rating_to_db(self) -> None:
        if self.one_word_type:
            SWH.update_avg_word_rating(self.sample_id, self.rating)
        else:
            SWH.update_avg_sentence_rating(self.sample_id, self.rating)
            
    def update_avg_rating_value(self) -> None:
        if self.one_word_type:
            self.avg_rating = SWH.get_avg_word_rating(self.sample_id)
        else:
            self.avg_rating = SWH.get_avg_sentence_rating(self.sample_id)
