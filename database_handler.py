import sqlite3
import config

def create_sample_from_text_file():
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    # Read sentences from the text file and insert them into the 'text_samples' table
    with open(config.TEXT_FILE, 'r') as file:
        sentences = file.readlines()
        for sentence in sentences:
            cursor.execute('INSERT INTO text_samples (sentence) VALUES (?)', (sentence.strip(),))

    # Commit the changes and close the connection
    connection.commit()
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

def get_ratings_by_sentence(sentence_id):
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    # Fetch ratings for a specific sentence_id from the 'ratings' table
    cursor.execute('SELECT * FROM ratings WHERE sentence_id = ?', (sentence_id,))
    ratings = cursor.fetchall()

    # Close the connection
    connection.close()

    return ratings