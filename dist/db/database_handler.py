import sqlite3
import random
import config

class DatabaseHandler:
    def __init__(self):
        self.connection = sqlite3.connect(config.DATABASE)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    @classmethod
    def create_tables(cls):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        # Create the 'sentences' table
        cursor.execute('''CREATE TABLE IF NOT EXISTS sentences (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sentence TEXT
                        )''')

        # Create the 'ratings' table
        cursor.execute('''CREATE TABLE IF NOT EXISTS ratings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sentence_id INTEGER,
                            rating INTEGER,
                            user_name TEXT,
                            FOREIGN KEY (sentence_id) REFERENCES sentences(id)
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

            # Delete all rows in 'ratings' table
            cursor.execute('DELETE FROM ratings')

            # Delete all rows in 'words' table
            cursor.execute('DELETE FROM words')

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


    def add_rating(self, sentence_id, rating, user_name):
        self.cursor.execute('INSERT INTO ratings (sentence_id, rating, user_name) VALUES (?, ?, ?)', (sentence_id, rating, user_name))
        self.connection.commit()

    def get_all_samples(self):
        self.cursor.execute('SELECT * FROM sentences')
        samples = self.cursor.fetchall()
        return samples

    @classmethod
    def get_random_sample(cls):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT COUNT(*) FROM sentences')
            total_samples = cursor.fetchone()[0]

            if total_samples == 0:
                return None

            random_index = random.randint(0, total_samples - 1)

            cursor.execute('SELECT * FROM sentences LIMIT 1 OFFSET ?', (random_index,))
            random_sample = cursor.fetchone()

            return random_sample[1]
        finally:
            connection.close()

    @classmethod
    def get_random_sample_word(cls):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT COUNT(*) FROM words')
            total_words = cursor.fetchone()[0]

            if total_words == 0:
                return None

            random_index = random.randint(0, total_words - 1)

            cursor.execute('SELECT * FROM words LIMIT 1 OFFSET ?', (random_index,))
            random_word = cursor.fetchone()

            return random_word[1]
        finally:
            connection.close()

    def get_ratings_by_sentence(self, sentence_id):
        self.cursor.execute('SELECT * FROM ratings WHERE sentence_id = ?', (sentence_id,))
        ratings = self.cursor.fetchall()
        return ratings