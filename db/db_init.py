import sqlite3
import config

def create_tables():
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    # Create the 'text_samples' table
    cursor.execute('''CREATE TABLE IF NOT EXISTS text_samples (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sentence TEXT
                    )''')

    # Create the 'ratings' table
    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sentence_id INTEGER,
                        rating INTEGER,
                        user_name TEXT,
                        FOREIGN KEY (sentence_id) REFERENCES text_samples(id)
                    )''')

    # Commit the changes and close the connection
    connection.commit()
    connection.close()
