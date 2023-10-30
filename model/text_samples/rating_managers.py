from model.database_handler import SentenceWordHandler as SWH

class RatingManager:
    def add_rating_to_db(self, text_sample):
        pass

class WordRating(RatingManager):
    def add_rating_to_db(self, text_sample):
        SWH.update_avg_word_rating(text_sample.sample_id, text_sample.rating)
        text_sample.avg_rating = SWH.get_avg_word_rating(text_sample.sample_id)

class SentenceRating(RatingManager):
    def add_rating_to_db(self, text_sample):
        SWH.update_avg_sentence_rating(text_sample.sample_id, text_sample.rating)
        text_sample.avg_rating = SWH.get_avg_sentence_rating(text_sample.sample_id)