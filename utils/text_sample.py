from database_handler import DatabaseHandler as DH
from difflib import SequenceMatcher


class TextSample:
    def __init__(self):
        # Initialize instance variables
        self.sample_exists = False
        self.word_count = None
        self.sec_to_read = None
        self.mill_sec_to_read = None
        self.sample = None
        self.sample_id = None
        self.avg_rating = None
        self.rating = None
        self.update_sample()

    def update_sample(self, one_word_sample=True):
        if one_word_sample:
            self.one_word_sample = True
            new_sample_text, new_sample_id = DH.get_random_word()
            self.get_avg_rating_word(new_sample_id)
        else:
            self.one_word_sample = False
            new_sample_text, new_sample_id = DH.get_random_sentence()
            self.get_avg_rating_sentence(new_sample_id)

        if new_sample_text:
            self.sample_exists = True
            self.sample = new_sample_text
            self.sample_id = new_sample_id
            self.update_char_count()
            self.calculate_duration()
        else:
            self.sample_exists = False
            self.sample = "No sample available. Hint: File/Add text file to database"
            print("Failed to obtain sample from get_random_sample()")

    def update_char_count(self):
        # Method to update the character count based on the current sample
        if self.sample is None:
            self.char_count = None
        else:
            self.char_count = len(self.sample)

    def calculate_duration(self):
        # Method to calculate the duration to read the text sample based on character count
        chars_per_minute = 300  # Assumed average reading speed in characters per minute
        if self.char_count is not None:
            self.sec_to_read = self.char_count / (chars_per_minute / 60)
            # Ensure the calculated duration is not less than 2 seconds
            self.sec_to_read = self.sec_to_read + 1.5
            self.mill_sec_to_read = int(self.sec_to_read * 1000)
        
    def get_avg_rating_word(self, id):
        self.avg_rating = DH.get_avg_word_rating(id)
        
    def get_avg_rating_sentence(self, id):
        self.avg_rating = DH.get_avg_sentence_rating(id)

    def add_rating_to_db(self):
        if self.one_word_sample:
            DH.update_avg_word_rating(self.sample_id, self.rating)
            # update avg-rating instance variable
            self.get_avg_rating_word(self.sample_id)
        else:
            DH.update_avg_sentence_rating(self.sample_id, self.rating)
            # update avg-rating instance variable
            self.get_avg_rating_sentence(self.sample_id)

    def preprocess_string(self, text):
    # Convert to lowercase and remove trailing dot and comma if present
        return text.lower().rstrip('.,')

    def calculate_similarity(self, string2):
        string1_lower = self.preprocess_string(self.sample)
        string2_lower = self.preprocess_string(string2)
        similarity_ratio = SequenceMatcher(None, string1_lower, string2_lower).ratio()
        self.rating = round(similarity_ratio * 100)
        print(f"calculated rating: {self.rating}")