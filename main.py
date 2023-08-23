from db.database_handler import DatabaseHandler
from utils.text_sample import TextSample
from gui.app_gui import AudioRecorderGUI
from dotenv import load_dotenv
def main():
    # laod env variables from .env
    load_dotenv()
    
    # Initialize the database and create tables if they don't exist
    DatabaseHandler.create_tables()
    
    # Create an instance of TextSample to manage sample text
    text_sample = TextSample()  

    # Create the main GUI window using initialized components
    gui = AudioRecorderGUI(text_sample)

    # Start the application by running the GUI event loop
    gui.mainloop()

if __name__ == "__main__":
    main()
