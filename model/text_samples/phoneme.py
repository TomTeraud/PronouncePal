import nltk


class Phoneme:
    @classmethod
    def get_phonemes(cls, sample_text):
        # Initialize the CMU Pronouncing Dictionary
        pronouncing_dict = nltk.corpus.cmudict.dict()
        if sample_text.lower() in pronouncing_dict:
            phonemes = pronouncing_dict[sample_text.lower()][0]
            # Create a string of phonemes enclosed in slashes
            return ' '.join(f'/{p}/' for p in phonemes)
        else:
            return 'None'