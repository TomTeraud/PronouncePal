from db.database_handler import DatabaseHandler as DH
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
            self.update_word_count()
            self.calculate_duration()
        else:
            self.sample_exists = False
            self.sample = "No sample available. Hint: File/Add text file to database"
            print("Failed to obtain sample from get_random_sample()")

    def update_word_count(self):
        # Method to update the word count based on the current sample
        if self.sample is None:
            self.word_count = None
        else:
            # Split the sample text into words using spaces and update the word_count
            self.word_count = len(self.sample.split())

    def calculate_duration(self):
        # Method to calculate the duration to read the text sample based on word count
        words_per_minute = 120  # Assumed average reading speed in words per minute
        if self.word_count is not None:
            self.sec_to_read = self.word_count / (words_per_minute / 60)
            # Ensure the calculated duration is not less than 2 seconds
            self.sec_to_read = max(self.sec_to_read, 2)
            self.mill_sec_to_read = int(self.sec_to_read * 1000)
        
    def get_avg_rating_word(self, id):
        self.avg_rating = DH.get_rating_for_word(id)
        
    def get_avg_rating_sentence(self, id):
        self.avg_rating = DH.get_rating_for_sentence(id)
    
    def calculate_similarity(self, string2):
        string1_lower = self.sample.lower()
        string2_lower = string2.lower()
        similarity_ratio = SequenceMatcher(None, string1_lower, string2_lower).ratio()
        self.rating = round(similarity_ratio * 100)
        print(f"calculated rating: {self.rating}")

    def add_rating_to_db(self):
        if self.one_word_sample:
            DH.add_word_rating_to_db(self.sample_id, self.rating)
            # update avg-rating instance variable
            self.get_avg_rating_word(self.sample_id)
        else:
            DH.add_sentence_rating_to_db(self.sample_id, self.rating)
            # update avg-rating instance variable
            self.get_avg_rating_sentence(self.sample_id)