from dotenv import load_dotenv

from database_handler import DatabaseInitializer
from text_samples._main import TextSample
from app_window import AppWindow


def main():
    # laod env variables from .env
    load_dotenv()
    
    # Initialize the database and create tables if they don't exist
    DatabaseInitializer.create_tables()
    
    # Create an instance of TextSample to manage sample text
    text_sample = TextSample()
    
    # Create the main GUI window using initialized components
    gui = AppWindow(text_sample)

    # Start the application by running the GUI event loop
    gui.mainloop()

if __name__ == "__main__":
    main()
