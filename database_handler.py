import sqlite3
import re
import config
from helpers import resource_path

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
                            sentence TEXT,
                            sentence_avg_rating INTEGER
                        )''')
              
        # Create the 'words' table
        cursor.execute('''CREATE TABLE IF NOT EXISTS word (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            word TEXT,
                            word_avg_rating INTEGER
                        )''')

        connection.commit()
        connection.close()
        DatabaseHandler.populate_database_if_empty()

    @staticmethod
    def populate_database_if_empty():
        if DatabaseHandler.is_sentence_table_empty():
            # Database is empty, so populate it
            DatabaseHandler.populate_sentences_table_from_text_file(resource_path("placeholder.txt"))
            DatabaseHandler.populate_words_table_from_sentences_table()

    @staticmethod
    def is_sentence_table_empty():
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()
        # Execute a SQL query to count the rows in the 'sentence' table
        cursor.execute('SELECT COUNT(*) FROM sentence')
        # Fetch the count result (it's a single value)
        count = cursor.fetchone()[0]
        connection.close()
        # Return True if the table is empty (count is 0), otherwise False
        return count == 0

    @classmethod
    def populate_sentences_table_from_text_file(cls, selected_file_path):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            with open(selected_file_path, 'r') as file:
                text = file.read()
                sentences = re.split(r'(?<=[.!?])\s+', text)

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
    def populate_words_table_from_sentences_table(cls):
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

    @classmethod
    def delete_all_rows(cls):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            # Delete all rows in 'sentences' table
            cursor.execute('DELETE FROM sentence')

            # Delete all rows in 'words' table
            cursor.execute('DELETE FROM word')
            connection.commit()

        except Exception as e:
            connection.rollback()
            print("An error occurred while deleting rows from the tables.")
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
    def update_avg_sentence_rating(cls, sentence_id, new_rating):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT sentence_avg_rating FROM sentence WHERE id = ?', (sentence_id,))
            old_avg_rating = cursor.fetchone()

            if old_avg_rating[0]:
                old_avg_rating = old_avg_rating[0]  # Extract the value from the result tuple
                calculated_avg_rating = ((old_avg_rating + new_rating) / 2)
                cursor.execute('UPDATE sentence SET sentence_avg_rating = ? WHERE id = ?', (calculated_avg_rating, sentence_id))
            else:
                cursor.execute('UPDATE sentence SET sentence_avg_rating = ? WHERE id = ?', (new_rating, sentence_id))
            connection.commit()

        except Exception as e:
            connection.rollback()  # Roll back changes in case of an error
            print("An error occurred while updating the rating.")
            print(e)
        finally:
            connection.close()

    @classmethod
    def get_avg_sentence_rating(cls, sentence_id):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT sentence_avg_rating FROM sentence WHERE id = ?', (sentence_id,))
            avg_rating = cursor.fetchone()[0]
            return avg_rating
        finally:
            connection.close()

    @staticmethod
    def update_avg_word_rating(word_id, new_rating):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()
        print(word_id, new_rating)

        try:
            cursor.execute('SELECT word_avg_rating FROM word WHERE id = ?', (word_id,))
            old_avg_rating = cursor.fetchone()

            if old_avg_rating[0]:
                old_avg_rating = old_avg_rating[0]  # Extract the value from the result tuple
                calculated_avg_rating = ((old_avg_rating + new_rating) / 2)
                cursor.execute('UPDATE word SET word_avg_rating = ? WHERE id = ?', (calculated_avg_rating, word_id))
            else:
                cursor.execute('UPDATE word SET word_avg_rating = ? WHERE id = ?', (new_rating, word_id))
            
            connection.commit()
        except Exception as e:
            connection.rollback()  # Roll back changes in case of an error
            print("An error occurred while adding a rating to the table.")
            print(e)
        finally:
            connection.close()

    @classmethod
    def get_avg_word_rating(cls, word_id):
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT word_avg_rating FROM word WHERE id = ?', (word_id,))
            avg_rating = cursor.fetchone()[0]
            return avg_rating
        finally:
            connection.close()