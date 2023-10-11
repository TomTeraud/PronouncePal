import sqlite3
import re
import config
from sqlite3 import IntegrityError
from helpers import resource_path


class DatabaseConnection:
    @staticmethod
    def get_connection():
        try:
            connection = sqlite3.connect(config.DATABASE)
            return connection
        except sqlite3.Error as e:
            print("Error while opening a database connection:", e)
            return None

    @staticmethod
    def close_connection(connection):
        if connection:
            try:
                connection.close()
            except sqlite3.Error as e:
                print("Error while closing the database connection:", e)


class DatabaseInitializer(DatabaseConnection):
    @staticmethod
    def create_tables():
        try:
            with DatabaseInitializer.get_connection() as connection:
                if connection:
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
                else:
                    print("Failed to obtain a database connection.")

        except sqlite3.Error as e:
            print("Error while creating tables:", e)
        finally:
            DatabaseInitializer.populate_database_if_empty()

    @staticmethod
    def is_sentence_table_empty():
        with DatabaseInitializer.get_connection() as connection:
            if connection:
                cursor = connection.cursor()
                cursor.execute('SELECT COUNT(*) FROM sentence')
                count = cursor.fetchone()[0]
                return count == 0
            else:
                print("Failed to obtain a database connection.")
                return False  # Return False to indicate the check couldn't be performed

    @staticmethod
    def populate_database_if_empty():
        if DatabaseInitializer.is_sentence_table_empty():
            # Database is empty, so populate it
            SentenceWordHandler.populate_sentences_table(resource_path(config.PLACEHOLDER_PATH))
            SentenceWordHandler.populate_words_table()


class SentenceWordHandler(DatabaseConnection):
    @staticmethod
    def populate_sentences_table(selected_file_path):
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()

                    # Read the file using a context manager
                    with open(selected_file_path, 'r') as file:
                        text = file.read()

                    # Remove newlines and other unwanted characters
                    cleaned_text = text.replace('\n', ' ').replace('\r', '')

                    # Split the cleaned text into sentences using regex
                    sentences = re.split(r'(?<=[.!?])\s+', cleaned_text)

                    # Use executemany to insert multiple sentences at once
                    stripped_sentences = [(sentence.strip(),) for sentence in sentences if sentence.strip()]
                    if stripped_sentences:
                        try:
                            cursor.executemany('INSERT INTO sentence (sentence) VALUES (?)', stripped_sentences)
                            connection.commit()  # Commit here if no exceptions occurred
                        except sqlite3.Error as e:
                            connection.rollback()
                            print("An error occurred during insert:", e)

                else:
                    print("Failed to obtain a database connection.")

        except sqlite3.Error as e:
            print("An error occurred while reading the text file or inserting into the database.")
            print(e)
        except FileNotFoundError:
            print(f"File not found at path: {selected_file_path}")
        except IntegrityError as ie:
            print("Integrity error occurred. Possibly a duplicate sentence insertion.")
        except Exception as ex:
            print("An unexpected error occurred.")
            print(ex)

    @staticmethod
    def populate_words_table():
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()

                    cursor.execute('SELECT sentence FROM sentence')
                    sentences = cursor.fetchall()

                    # Create a set to keep track of unique words
                    unique_words = set()

                    for sentence in sentences:
                        words = sentence[0].split()  # Split sentence into words
                        for word in words:
                            stripped_word = word.strip().lower()
                            stripped_word = ''.join(filter(str.isalpha, stripped_word))  # Remove non-alphabetic characters
                            if stripped_word and len(stripped_word) >= 3 and stripped_word not in unique_words:
                                cursor.execute('INSERT INTO word (word) VALUES (?)', (stripped_word,))
                                unique_words.add(stripped_word)  # Add the word to the set

                    connection.commit()
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while saving words from sentences.")
            print(e)

    @staticmethod
    def delete_all_rows():
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()

                    # Delete all rows in 'sentences' table
                    cursor.execute('DELETE FROM sentence')

                    # Delete all rows in 'words' table
                    cursor.execute('DELETE FROM word')
                    connection.commit()
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while deleting rows from the tables.")
            print(e)

    @staticmethod
    def get_random_sentence():
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()
                    cursor.execute('SELECT id, sentence '
                                'FROM sentence '
                                'ORDER BY RANDOM() '
                                'LIMIT 1')
                    random_sample = cursor.fetchone()
                    if random_sample:
                        return random_sample[1], random_sample[0]  # Return sentence and sentence ID
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while fetching a random sentence.")
            print(e)

    @staticmethod
    def get_random_word():
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()
                    cursor.execute('SELECT id, word '
                                'FROM word '
                                'ORDER BY RANDOM() '
                                'LIMIT 1')
                    random_word = cursor.fetchone()
                    if random_word:
                        return random_word[1], random_word[0]  # Return word and word ID
                    else:
                        return None, None  # Return None if no word is found
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while fetching a random word.")
            print(e)

    @staticmethod
    def fetch_sentences_from_database():
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()
                    cursor.execute('SELECT sentence, sentence_avg_rating FROM sentence')
                    sentences = cursor.fetchall()
                    return sentences
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while fetching sentences from the database.")
            print(e)

    @staticmethod
    def fetch_words_from_database():
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()
                    cursor.execute('SELECT word, word_avg_rating FROM word')
                    words = cursor.fetchall()
                    return words
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while fetching words from the database.")
            print(e)

    @staticmethod
    def get_avg_word_rating(word_id):
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()
                    cursor.execute('SELECT word_avg_rating FROM word WHERE id = ?', (word_id,))
                    result = cursor.fetchone()

                    if result is not None:
                        avg_rating = result[0]
                    else:
                        avg_rating = 0.0  # Set a default value when no result is found

                    return avg_rating
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while fetching the average word rating.")
            print(e)

    @staticmethod
    def get_avg_sentence_rating(sentence_id):
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()
                    cursor.execute('SELECT sentence_avg_rating FROM sentence WHERE id = ?', (sentence_id,))
                    avg_rating = cursor.fetchone()[0]
                    return avg_rating
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while fetching the average sentence rating.")
            print(e)

    @staticmethod
    def update_avg_word_rating(word_id, new_rating):
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()

                    cursor.execute('SELECT word_avg_rating FROM word WHERE id = ?', (word_id,))
                    old_avg_rating = cursor.fetchone()

                    if old_avg_rating and old_avg_rating[0]:
                        old_avg_rating = old_avg_rating[0]  # Extract the value from the result tuple
                        calculated_avg_rating = ((old_avg_rating + new_rating) / 2)
                        cursor.execute('UPDATE word SET word_avg_rating = ? WHERE id = ?', (calculated_avg_rating, word_id))
                    else:
                        cursor.execute('UPDATE word SET word_avg_rating = ? WHERE id = ?', (new_rating, word_id))

                    connection.commit()
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while updating the word rating.")
            print(e)

    @staticmethod
    def update_avg_sentence_rating(sentence_id, new_rating):
        try:
            with SentenceWordHandler.get_connection() as connection:
                if connection:
                    cursor = connection.cursor()

                    cursor.execute('SELECT sentence_avg_rating FROM sentence WHERE id = ?', (sentence_id,))
                    old_avg_rating = cursor.fetchone()

                    if old_avg_rating and old_avg_rating[0]:
                        old_avg_rating = old_avg_rating[0]  # Extract the value from the result tuple
                        calculated_avg_rating = ((old_avg_rating + new_rating) / 2)
                        cursor.execute('UPDATE sentence SET sentence_avg_rating = ? WHERE id = ?', (calculated_avg_rating, sentence_id))
                    else:
                        cursor.execute('UPDATE sentence SET sentence_avg_rating = ? WHERE id = ?', (new_rating, sentence_id))

                    connection.commit()
                else:
                    print("Failed to obtain a database connection.")
        except sqlite3.Error as e:
            print("An error occurred while updating the sentence rating.")
            print(e)
