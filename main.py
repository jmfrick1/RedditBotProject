import tkinter as tk
from RedditBotGUI import RedditBotGUI  # Assuming your GUI class is saved in RedditBotGUI.py
from praw_setup import create_reddit_instance  # For Reddit API interaction

def main():
    # Initialize any prerequisites or perform setup tasks here.
    # For example, create a Reddit instance if needed for global use (optional based on your design):
    reddit = create_reddit_instance()

    # Start the GUI application
    app = RedditBotGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
