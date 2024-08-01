# praw_setup.py
import praw

def create_reddit_instance():
    # jmf's Reddit Bot Setup
    # Make sure to replace the placeholders below with your actual Reddit API credentials

  import praw

def create_reddit_instance(client_id, client_secret, user_agent, username, password):
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password
    )

    return reddit

# Test the connection to ensure everything is set up correctly
if __name__ == '__main__':
    reddit = create_reddit_instance()
    print(f"Logged in as: {reddit.user.me()}")  # This should print your Reddit username if the setup is correct
