import nltk
from difflib import SequenceMatcher
from config import CHARS_PER_MINUTE, MIN_DURATION
from text_samples.sample_managers import WordSample, SentenceSample
from text_samples.rating_managers import WordRating, SentenceRating

class TextSample:
    def __init__(self):
        self.sample_exists = False
        self.sample = None
        self.sample_id = None
        self.avg_rating = None
        self.phoneme = None
        self.rating = None
        self.char_count = None
        self.one_word = True
        self.update_sample()

    def update_sample(self, one_word_sample=True):
        # Instantiate the sample manager based on the type of sample
        sample_manager = WordSample() if one_word_sample else SentenceSample()
        sample_manager.update_sample(self)
        self.calculate_duration()

    def add_rating_to_db(self):
        if self.one_word:
            rating_manager = WordRating()
        else:
            rating_manager = SentenceRating()

        rating_manager.add_rating_to_db(self)

    def update_char_count(self):
        if self.sample is None:
            self.char_count = None
        else:
            self.char_count = len(self.sample)

    def calculate_duration(self):
        if self.char_count is not None:
            # Calculate the duration to read the sample text based on the character count
            self.sec_to_read = self.char_count / (CHARS_PER_MINUTE / 60)
            self.sec_to_read = self.sec_to_read + MIN_DURATION
            self.mill_sec_to_read = int(self.sec_to_read * 1000)

    def preprocess_string(self, text):
        # Preprocess a string by converting it to lowercase and removing trailing dots and commas
        return text.lower().rstrip('.,')

    def calculate_similarity(self, string2):
        string1_lower = self.preprocess_string(self.sample)
        string2_lower = self.preprocess_string(string2)
        # Calculate the similarity ratio between two strings
        similarity_ratio = SequenceMatcher(None, string1_lower, string2_lower).ratio()
        self.rating = round(similarity_ratio * 100)

    def get_phonemes(self, sample_text):
        # Initialize the CMU Pronouncing Dictionary
        pronouncing_dict = nltk.corpus.cmudict.dict()
        if sample_text.lower() in pronouncing_dict:
            phonemes = pronouncing_dict[sample_text.lower()][0]
            # Create a string of phonemes enclosed in slashes
            self.phoneme = ' '.join(f'/{p}/' for p in phonemes)
        else:
            self.phoneme = 'None'
