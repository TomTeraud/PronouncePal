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
        self.rating = 50
        self.one_word_type = True
        self.sec_to_read = None

    def load_new_word(self):
        self.manage_new_sample_data(SWH.get_random_word())
        self.sample_exists = True
        self.one_word_type = True
        self.manage_phoname()

    def load_new_sentence(self) -> str:
        self.manage_new_sample_data(SWH.get_random_sentence())
        self.sample_exists = True
        self.one_word_type = False
        self.manage_phoname()
    
    def get_sample_text(self) -> str:
        return self.sample
    
    def manage_phoname(self) -> None:
        if self.phonome_state:
            if self.one_word_type:
                self.phoneme = Phoneme.get_phonemes(self.sample)
            else:
                self.phoneme = ""
    
    def manage_new_sample_data(self, sample: tuple) -> None:
        self.sample_id = sample[0]
        self.sample = sample[1]
        self.avg_rating = sample[2]
        self.sec_to_read = self.calculate_duration(sample[1])

        
    def calculate_duration(self, sample: str) -> float:
        # Calculate the duration to read the sample text based on the character count
        char_count = len(sample)
        sec_to_read = char_count / (CHARS_PER_MINUTE / 60)
        return sec_to_read + MIN_DURATION
        
    def preprocess_string(self, text: str) -> str:
        # Preprocess a string by converting it to lowercase and removing trailing dots and commas
        return text.lower().rstrip('.,')

    def calculate_similarity(self, string2: str) -> None:
        string1_lower = self.preprocess_string(self.sample)
        string2_lower = self.preprocess_string(string2)
        # Calculate the similarity ratio between two strings
        similarity_ratio = SequenceMatcher(None, string1_lower, string2_lower).ratio()
        self.rating = round(similarity_ratio * 100)

    def update_avg_rating(self, id: int, rating:int) -> int:
        if self.one_word_type:
            return SWH.update_avg_word_rating(id, rating)
        else:
            return SWH.update_avg_sentence_rating(id, rating)
