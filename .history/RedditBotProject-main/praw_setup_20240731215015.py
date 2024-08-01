# praw_setup.py
import praw

def create_reddit_instance():
    # jmf's Reddit Bot Setup
    # Make sure to replace the placeholders below with your actual Reddit API credentials

    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',  # Replace 'YOUR_CLIENT_ID' with your actual client_id
        client_secret='YOUR_CLIENT_SECRET',  # Replace 'YOUR_CLIENT_SECRET' with your actual client_secret
        password='YOUR_REDDIT_PASSWORD',  # Replace 'YOUR_REDDIT_PASSWORD' with your Reddit account password
        user_agent='Script by jmf for Reddit automation and engagement',  # Describe your script
        username='YOUR_REDDIT_USERNAME'  # Replace 'YOUR_REDDIT_USERNAME' with your Reddit username
    )
    return reddit

# Test the connection to ensure everything is set up correctly
if __name__ == '__main__':
    reddit = create_reddit_instance()
    print(f"Logged in as: {reddit.user.me()}")  # This should print your Reddit username if the setup is correct
