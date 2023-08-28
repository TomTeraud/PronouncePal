from db.database_handler import DatabaseHandler as DH
import random

class TextSample:
    def __init__(self):
        # Initialize instance variables
        self.sample_exists = False  # Flag to indicate if a sample exists
        self.word_count = None  # Number of words in the sample
        self.sec_to_read = None  # Duration to read the sample in seconds
        self.mill_sec_to_read = None  # Duration to read the sample in milliseconds
        self.sample = None
        self.avg_sample_rating = None
        self.update_sample()
        
    def update_sample(self, one_word_sample=True):
        # Method to retrieve a new random sample and update the 'sample' attribute
        rating = random.randint(0, 100)
        if one_word_sample:
            new_sample_text, new_sample_id = DH.get_random_word()
            DH.add_word_rating(new_sample_id, rating)
            avg_rating = DH.get_rating_for_word(new_sample_id)
        else:
            new_sample_text, new_sample_id = DH.get_random_sentence()
            DH.add_sentence_rating(new_sample_id, rating)
            avg_rating = DH.get_rating_for_sentence(new_sample_id)

        if new_sample_text:
            self.sample_exists = True
            self.sample = new_sample_text
            self.avg_sample_rating = avg_rating
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