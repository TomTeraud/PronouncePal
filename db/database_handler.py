import sqlite3
import config

class DatabaseHandler:
    def __init__(self):
        self.connection = sqlite3.connect(config.DATABASE)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    @staticmethod
    def create_tables():
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        # Create the 'sentences' table
        cursor.execute('''CREATE TABLE IF NOT EXISTS sentences (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sentence TEXT
                        )''')

        # Create the 'ratings' table for sentences
        cursor.execute('''CREATE TABLE IF NOT EXISTS sentence_ratings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sentence_id INTEGER,
                            rating INTEGER,
                            user_name TEXT,
                            FOREIGN KEY (sentence_id) REFERENCES sentences(id)
                        )''')
        
        # Create the 'ratings' table for words
        cursor.execute('''CREATE TABLE IF NOT EXISTS word_ratings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            word_id INTEGER,
                            rating INTEGER,
                            user_name TEXT,
                            FOREIGN KEY (word_id) REFERENCES words(id)
                        )''')
        
        # Create the 'words' table
        cursor.execute('''CREATE TABLE IF NOT EXISTS words (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            word TEXT
                        )''')

        connection.commit()
        connection.close()

    @classmethod
    def delete_all_rows(cls):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            # Delete all rows in 'sentences' table
            cursor.execute('DELETE FROM sentences')

            # Delete all rows in 'sentences ratings' table
            cursor.execute('DELETE FROM sentences_ratings')

            # Delete all rows in 'words' table
            cursor.execute('DELETE FROM words')

            # Delete all rows in 'words rating' table
            cursor.execute('DELETE FROM words_rating')
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("An error occurred while deleting rows from the tables.")
            print(e)
        finally:
            connection.close()

    @classmethod
    def get_and_save_sentences_from_text_file(cls, selected_file_path):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            with open(selected_file_path, 'r') as file:
                sentences = file.readlines()
                for sentence in sentences:
                    stripped_sentence = sentence.strip()
                    if stripped_sentence:  # Check if the sentence is not empty
                        cursor.execute('INSERT INTO sentences (sentence) VALUES (?)', (stripped_sentence,))

            connection.commit()
        except Exception as e:
            connection.rollback()
            print("An error occurred while reading the text file or inserting into the database.")
            print(e)
        finally:
            connection.close()

    @classmethod
    def save_words_from_sentences(cls):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT sentence FROM sentences')
            sentences = cursor.fetchall()

            for sentence in sentences:
                words = sentence[0].split()  # Split sentence into words
                for word in words:
                    stripped_word = word.strip().lower()
                    stripped_word = ''.join(filter(str.isalpha, stripped_word))  # Remove non-alphabetic characters
                    if stripped_word and len(stripped_word) >= 3:  # Check word length
                        cursor.execute('INSERT INTO words (word) VALUES (?)', (stripped_word,))

            connection.commit()
        except Exception as e:
            connection.rollback()
            print("An error occurred while saving words from sentences.")
            print(e)
        finally:
            connection.close()

    @staticmethod
    def add_word_rating(word_id, rating):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('INSERT INTO word_ratings (word_id, rating) VALUES (?, ?)', (word_id, rating))
            connection.commit()
        except Exception as e:
            connection.rollback()  # Roll back changes in case of an error
            print("An error occurred while adding a rating to the table.")
            print(e)
        finally:
            connection.close()

    @staticmethod
    def add_sentence_rating(sentence_id, rating):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('INSERT INTO sentence_ratings (sentence_id, rating) VALUES (?, ?)', (sentence_id, rating))
            connection.commit()
        except Exception as e:
            connection.rollback()  # Roll back changes in case of an error
            print("An error occurred while adding a rating to the table.")
            print(e)
        finally:
            connection.close()

    @classmethod
    def get_random_sentence(cls):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT id, sentence '
                        'FROM sentences '
                        'ORDER BY RANDOM() '
                        'LIMIT 1')
            random_sample = cursor.fetchone()

            return random_sample[1], random_sample[0]  # Return sentence and sentence ID
        finally:
            connection.close()

    @classmethod
    def get_random_word(cls):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT id, word '
                        'FROM words '
                        'ORDER BY RANDOM() '
                        'LIMIT 1')
            random_word = cursor.fetchone()

            if random_word:
                return random_word[1], random_word[0]  # Return word and word ID
            else:
                return None, None  # Return None if no word is found
        finally:
            connection.close()

    @classmethod
    def get_rating_for_sentence(cls, sentence_id):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT AVG(rating) FROM sentence_ratings WHERE sentence_id = ?', (sentence_id,))
            avg_rating = cursor.fetchone()[0]
            return avg_rating
        finally:
            connection.close()

    @classmethod
    def get_rating_for_word(cls, word_id):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT AVG(rating) FROM word_ratings WHERE word_id = ?', (word_id,))
            avg_rating = cursor.fetchone()[0]
            return avg_rating
        finally:
            connection.close()