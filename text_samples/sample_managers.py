from database_handler import SentenceWordHandler as SWH


class SampleManager:
    def update_sample(self, text_sample):
        pass

class WordSample(SampleManager):
    def update_sample(self, text_sample):
        new_sample_text, new_sample_id = SWH.get_random_word()
        if new_sample_text:
            text_sample.one_word = True
            text_sample.sample_exists = True
            text_sample.sample = new_sample_text
            text_sample.sample_id = new_sample_id
            text_sample.update_char_count()
            text_sample.avg_rating = SWH.get_avg_word_rating(new_sample_id)
        else:
            # text_sample.sample = "No sample available. Hint: File/Add text file to database"
            print("Failed to obtain sample from get_random_word()")

class SentenceSample(SampleManager):
    def update_sample(self, text_sample):
        new_sample_text, new_sample_id = SWH.get_random_sentence()
        if new_sample_text:
            text_sample.one_word = False
            text_sample.sample_exists = True
            text_sample.sample = new_sample_text
            text_sample.sample_id = new_sample_id
            text_sample.update_char_count()
            text_sample.avg_rating = SWH.get_avg_sentence_rating(new_sample_id)
        else:
            text_sample.sample = "No sample available. Hint: File/Add text file to database"
            print("Failed to obtain sample from get_random_sentence()")