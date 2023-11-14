from tkinter import *
from tkinter import ttk
import model.config as config
from view.view_custom_fun import column_row_configure


class RatingMenuHandler:
    @classmethod
    def show_words_ratings(cls, words_rating_tuples: list[tuple]) -> None:
        cls.show_ratings(words_rating_tuples, "Words Ratings")

    @classmethod
    def show_sentences_ratings(cls, sentences: list[tuple]) -> None:
        cls.show_ratings(sentences, "Sentences Ratings")

    @classmethod
    def show_ratings(cls, data, title):
        data_len = len(data)
        word_lines = config.LPP_WORD
        sentence_lines = config.LPP_SENTENCE
        
        # Create a new top-level window
        root = Toplevel()
        root.title(title)
        column_row_configure(root, 1, 1)

        # Create a frame for displaying the data and page number
        frame = ttk.Frame(root)
        frame.grid(row=0, column=0, sticky=NSEW)

        # Pagination settings
        # Determin number of items per page
        if title == "Words Ratings":
            page_size = word_lines  
        else:
            page_size = sentence_lines
        current_page = 1  # Current page index
        column_row_configure(frame, 1, page_size)
        
        # Function to update the frame with data for the current page
        def update_frame():
            start_index = (current_page - 1) * page_size
            end_index = current_page * page_size

            for widget in frame.winfo_children():
                widget.grid_forget()

            for index, (text, rating) in enumerate(data[start_index:end_index], start=start_index):
                text_bg_color = "white" if index % 2 == 0 else "light gray"
                rating_bg_color = "light gray" if index % 2 == 0 else "white"

                text_label = ttk.Label(frame, text=text, background=text_bg_color, wraplength=300)
                rating_label = ttk.Label(frame, text=rating, background=rating_bg_color,padding=(10, 10, 10, 0))

                text_label.grid(column=0, row=index % page_size, sticky=NSEW)
                rating_label.grid(column=1, row=index % page_size, sticky=NSEW)

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
        button_frame.grid(row=1, column=0, sticky=NSEW)
        column_row_configure(button_frame, 5, 1)

        # Create "First," "Previous," "Next," and "Last" buttons for pagination
        first_button = ttk.Button(button_frame, text="First", command=first_page)
        prev_button = ttk.Button(button_frame, text="Previous", command=prev_page)
        next_button = ttk.Button(button_frame, text="Next", command=next_page)
        last_button = ttk.Button(button_frame, text="Last", command=last_page)

        first_button.grid(row=0, column=0, sticky=NSEW)
        prev_button.grid(row=0, column=1, sticky=NSEW)
        next_button.grid(row=0, column=3, sticky=NSEW)
        last_button.grid(row=0, column=4, sticky=NSEW)

        # Create a label to display the current page number
        page_label = ttk.Label(button_frame, text=f"Page {current_page}")
        page_label.grid(row=0, column=2)

        # Update the frame with data for the initial page
        update_frame()

