import tkinter as tk
from tkinter import ttk
import sqlite3
import config


class RatingMenuHandler:
    @classmethod
    def show_ratings(cls, data, title):
        data_len = len(data)
        # Create a new top-level window
        root = tk.Toplevel()
        root.title(title)

        # Create a frame for displaying the data and page number
        frame = ttk.Frame(root)
        frame.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Pagination settings
        # Determin number of items per page
        if title == "Words Ratings":
            page_size = 10  
        else:
            page_size = 4
        current_page = 1  # Current page index
        
        # Function to update the frame with data for the current page
        def update_frame():
            start_index = (current_page - 1) * page_size
            end_index = current_page * page_size

            for widget in frame.winfo_children():
                widget.grid_forget()

            for index, (text, rating) in enumerate(data[start_index:end_index], start=start_index):
                text_bg_color = "white" if index % 2 == 0 else "light gray"
                rating_bg_color = "light gray" if index % 2 == 0 else "white"


                text_label = ttk.Label(frame, text=text, background=text_bg_color)
                rating_label = ttk.Label(frame, text=rating, background=rating_bg_color,padding=(10, 10, 10, 0))

                text_label.grid(column=0, row=index % page_size, sticky=(tk.N, tk.W, tk.E, tk.S))
                rating_label.grid(column=1, row=index % page_size, sticky=(tk.N, tk.W, tk.E, tk.S))

            # Update the page number label
            page_label.config(text=f"Page {current_page}")

        # Function to go to the previous page
        def prev_page():
            nonlocal current_page
            if current_page > 1:
                current_page -= 1
                update_frame()

        # Function to go to the next page
        def next_page():
            nonlocal current_page
            max_pages = (data_len + page_size - 1) // page_size
            if current_page < max_pages:
                current_page += 1
                update_frame()

        # Function to go to the first page
        def first_page():
            nonlocal current_page
            if current_page > 1:
                current_page = 1
                update_frame()

        # Function to go to the last page
        def last_page():
            nonlocal current_page
            max_pages = (data_len + page_size - 1) // page_size
            if current_page < max_pages:
                current_page = max_pages
                update_frame()


        # Create frame for paginate buttons
        button_frame = ttk.Frame(root)
        button_frame.grid(row=1, column=0, sticky=tk.W)

        # Create "First," "Previous," "Next," and "Last" buttons for pagination
        first_button = ttk.Button(button_frame, text="First", command=first_page)
        prev_button = ttk.Button(button_frame, text="Previous", command=prev_page)
        next_button = ttk.Button(button_frame, text="Next", command=next_page)
        last_button = ttk.Button(button_frame, text="Last", command=last_page)

        first_button.grid(row=1, column=0, sticky=tk.W)
        prev_button.grid(row=1, column=1, sticky=tk.W)
        next_button.grid(row=1, column=3, sticky=tk.E)
        last_button.grid(row=1, column=4, sticky=tk.E)

        # Create a label to display the current page number
        page_label = ttk.Label(button_frame, text=f"Page {current_page}")
        page_label.grid(row=1, column=2)

        # Update the frame with data for the initial page
        update_frame()

        # Configure row and column weights to make the frame resize properly
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

    @classmethod
    def show_words_ratings(cls):
        # Fetch word ratings from the database
        words_rating_tuples = cls.fetch_words_from_database()
        cls.show_ratings(words_rating_tuples, "Words Ratings")

    @classmethod
    def show_sentences_ratings(cls):
        # Fetch sentences from the database
        sentences = cls.fetch_sentences_from_database()
        cls.show_ratings(sentences, "Sentences Ratings")

    @staticmethod
    def fetch_words_from_database():
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT word, word_avg_rating FROM word')
            words = cursor.fetchall()
            return words
        finally:
            connection.close()

    @staticmethod
    def fetch_sentences_from_database():
        connection = sqlite3.connect(config.DATABASE)
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT sentence, sentence_avg_rating FROM sentence')
            sentences = cursor.fetchall()
            return sentences
        finally:
            connection.close()
