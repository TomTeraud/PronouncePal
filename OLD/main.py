from dotenv import load_dotenv

from OLD.database_handler import DatabaseInitializer
from OLD.app import AppWindow


def main():
    # laod env variables from .env
    load_dotenv()
    
    # Initialize the database and create tables if they don't exist
    DatabaseInitializer.create_tables()
    
    # Create an instance of the AppWindow class
    gui = AppWindow()

    # Start the application by running the GUI event loop
    gui.mainloop()

if __name__ == "__main__":
    main()
