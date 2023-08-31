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

        # Create the 'sentence' table
        cursor.execute('''CREATE TABLE IF NOT EXISTS sentence (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sentence TEXT
                        )''')

        # Create the 'rating' table for sentence
        cursor.execute('''CREATE TABLE IF NOT EXISTS sentence_rating (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sentence_id INTEGER,
                            rating INTEGER,
                            user_name TEXT,
                            FOREIGN KEY (sentence_id) REFERENCES sentence(id)
                        )''')
        
        # Create the 'rating' table for word
        cursor.execute('''CREATE TABLE IF NOT EXISTS word_rating (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            word_id INTEGER,
                            rating INTEGER,
                            user_name TEXT,
                            FOREIGN KEY (word_id) REFERENCES word(id)
                        )''')
        
        # Create the 'words' table
        cursor.execute('''CREATE TABLE IF NOT EXISTS word (
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
            cursor.execute('DELETE FROM sentence')

            # Delete all rows in 'sentences ratings' table
            cursor.execute('DELETE FROM sentence_rating')

            # Delete all rows in 'words' table
            cursor.execute('DELETE FROM word')

            # Delete all rows in 'words rating' table
            cursor.execute('DELETE FROM word_rating')
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
                        cursor.execute('INSERT INTO sentence (sentence) VALUES (?)', (stripped_sentence,))

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
            cursor.execute('SELECT sentence FROM sentence')
            sentences = cursor.fetchall()

            for sentence in sentences:
                words = sentence[0].split()  # Split sentence into words
                for word in words:
                    stripped_word = word.strip().lower()
                    stripped_word = ''.join(filter(str.isalpha, stripped_word))  # Remove non-alphabetic characters
                    if stripped_word and len(stripped_word) >= 3:  # Check word length
                        cursor.execute('INSERT INTO word (word) VALUES (?)', (stripped_word,))

            connection.commit()
        except Exception as e:
            connection.rollback()
            print("An error occurred while saving words from sentences.")
            print(e)
        finally:
            connection.close()

    @staticmethod
    def add_word_rating_to_db(word_id, rating):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('INSERT INTO word_rating (word_id, rating) VALUES (?, ?)', (word_id, rating))
            connection.commit()
        except Exception as e:
            connection.rollback()  # Roll back changes in case of an error
            print("An error occurred while adding a rating to the table.")
            print(e)
        finally:
            connection.close()

    @staticmethod
    def add_sentence_rating_to_db(sentence_id, rating):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('INSERT INTO sentence_rating (sentence_id, rating) VALUES (?, ?)', (sentence_id, rating))
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
                        'FROM sentence '
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
                        'FROM word '
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
            cursor.execute('SELECT AVG(rating) FROM sentence_rating WHERE sentence_id = ?', (sentence_id,))
            avg_rating = cursor.fetchone()[0]
            return avg_rating
        finally:
            connection.close()

    @classmethod
    def get_rating_for_word(cls, word_id):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT AVG(rating) FROM word_rating WHERE word_id = ?', (word_id,))
            avg_rating = cursor.fetchone()[0]
            return avg_rating
        finally:
            connection.close()