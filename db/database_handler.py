import sqlite3
import random
import config

def create_sample_from_text_file(selected_file_path):
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    try:
        with open(selected_file_path, 'r') as file:
            sentences = file.readlines()
            for sentence in sentences:
                stripped_sentence = sentence.strip()
                if stripped_sentence:  # Check if the sentence is not empty
                    cursor.execute('INSERT INTO text_samples (sentence) VALUES (?)', (stripped_sentence,))

        # Commit the changes and close the connection
        connection.commit()
    except Exception as e:
        connection.rollback()  # Rollback changes if an exception occurs
        print("An error occurred while reading the text file or inserting into the database.")
        print(e)
    finally:
        connection.close()


def add_rating(sentence_id, rating, user_name):
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    # Insert the rating into the 'ratings' table with the corresponding sentence_id
    cursor.execute('INSERT INTO ratings (sentence_id, rating, user_name) VALUES (?, ?, ?)', (sentence_id, rating, user_name))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

def get_all_samples():
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    # Fetch all rows from the 'text_samples' table
    cursor.execute('SELECT * FROM text_samples')
    samples = cursor.fetchall()

    # Close the connection
    connection.close()

    return samples

def get_random_sample():
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    # Get the total count of rows in the 'text_samples' table
    cursor.execute('SELECT COUNT(*) FROM text_samples')
    total_samples = cursor.fetchone()[0]

    if total_samples == 0:
        return None  # Return None if there are no samples in the table

    # Generate a random index within the range of total samples
    random_index = random.randint(0, total_samples - 1)

    # Fetch the random row from the 'text_samples' table
    cursor.execute('SELECT * FROM text_samples LIMIT 1 OFFSET ?', (random_index,))
    random_sample = cursor.fetchone()

    # Close the connection
    connection.close()

    return random_sample

def get_ratings_by_sentence(sentence_id):
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    # Fetch ratings for a specific sentence_id from the 'ratings' table
    cursor.execute('SELECT * FROM ratings WHERE sentence_id = ?', (sentence_id,))
    ratings = cursor.fetchall()

    # Close the connection
    connection.close()

    return ratings